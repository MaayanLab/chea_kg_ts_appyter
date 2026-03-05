import pandas as pd
import mygene
import requests
import time

def clean_and_name_raw_data(input_path, tissue, out_prefix = ''):
    """
    Cleaning: ensuring that each row contains the right number and type of entries, ensuring no duplicate gene IDs.
    Naming: Converting gene IDs to gene names.
    """
    output_path = f"{out_prefix}{tissue}_rna-seq_cleaned.txt"
    output_path_2 = f"{out_prefix}{tissue}_rna-seq_named.txt"

    with open(input_path, 'r', encoding='utf-8', errors='ignore') as infile, \
        open(output_path, 'w', encoding='utf-8') as outfile:

        header = infile.readline()
        outfile.write(header)

        delimiter = '\t' # tab delimiter for .txt files
        num_columns = len(header.strip().split(delimiter))

        for line_num, line in enumerate(infile, start=2):
            samp_title_parts = line.strip().split(delimiter)
            if len(samp_title_parts) >= num_columns:
                trimmed = samp_title_parts[:num_columns]
                try:
                    float_vals = [float(x) for x in trimmed[1:]]
                    outfile.write(delimiter.join(trimmed) + '\n')
                except ValueError:
                    print(f"Skipping line {line_num}: non-float value encountered in {trimmed}")
            else:
                print(f"Skipping line {line_num}: only {len(samp_title_parts)} columns (expected {num_columns})")

    raw_data = pd.read_csv(output_path, delimiter='\t')
    ensembl_ids = raw_data["gene_id"].tolist()
    mg = mygene.MyGeneInfo()
    results = mg.querymany(ensembl_ids, scopes='ensembl.gene', fields='symbol', species='rat')

    id_to_symbol = {}
    for item in results:
        if 'symbol' in item:
            id_to_symbol[item['query']] = item.get('symbol', item['query']).upper()
        else:
            id_to_symbol[item['query']] = item['query']

    raw_data['gene_id'] = raw_data['gene_id'].map(lambda x: id_to_symbol.get(x, x))
    raw_data = raw_data.drop_duplicates(subset='gene_id', keep='first')
    raw_data.to_csv(output_path_2, index=False) # outputs a .txt file with comma delimiters...
    print("Finished cleaning and naming raw RNA-seq data.")

def generate_metadata(rna_seq_data, annotations, tissue, alias=None):
    """
    Generates formatted metadata CSV files that can be paired with RNA-seq data for use
    in the Appyter.
    """
    raw_data = pd.read_csv(rna_seq_data)
    col_names = raw_data.columns.to_list()
    sample_ids = col_names[1:]

    combined_metadata = pd.DataFrame(columns=["sample_name", "time_pt_annotation"])
    combined_metadata["sample_name"] = sample_ids

    annotations_df = pd.read_csv(annotations)

    def make_prefix_from_id(annot_df, input_id):
        for sample_title in annot_df["Title"]:
            sample_name, sample_id = sample_title.rsplit("_", 1)
            if sample_id == input_id:
                fields = sample_name.split("_")
                if len(fields) >= 4 and fields[-6] == "training":
                    return f"{fields[-5]}_{fields[-4]}"
                elif len(fields) >= 4 and fields[-6] == "control":
                    return f"{fields[-5]}_sedentary"

    for sample_id in sample_ids:
        prefix = make_prefix_from_id(annotations_df, sample_id)
        combined_metadata.loc[combined_metadata["sample_name"] == sample_id, "time_pt_annotation"] = prefix
    combined_metadata.to_csv(f"{tissue}_metadata.csv", index=False)

    male_metadata = combined_metadata.dropna(subset=["time_pt_annotation"])
    male_metadata = male_metadata[male_metadata["time_pt_annotation"].str.startswith("male")]

    female_metadata = combined_metadata.dropna(subset=["time_pt_annotation"])
    female_metadata = female_metadata[female_metadata["time_pt_annotation"].str.startswith("female")]

    time_order_1 = {'male_sedentary': 0, 'male_1w': 1, 'male_2w': 2, 'male_4w': 3, 'male_8w': 4}
    time_order_2 = {'female_sedentary': 0, 'female_1w': 1, 'female_2w': 2, 'female_4w': 3, 'female_8w': 4}

    male_sorted = male_metadata.sort_values(by='time_pt_annotation', key=lambda col: col.map(time_order_1))
    female_sorted = female_metadata.sort_values(by='time_pt_annotation', key=lambda col: col.map(time_order_2))

    male_sorted.to_csv(f"{tissue}_male_samples.csv", index=False)
    female_sorted.to_csv(f"{tissue}_female_samples.csv", index=False)
    print(f"Finished creating formatted CSV files for {tissue} samples.")
    
