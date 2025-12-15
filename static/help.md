# ChEA-KG-TS Tutorial

## Abstract
Transcription factors (TFs) are key regulators of gene expression. Understanding the complex ways in which they interact is critical to unravel how biological pathways such as disease, aging, and development are controlled. TF modules can change over time, for example in response to perturbations including exercise or chemical treatments. Time series experiments measure these temporal changes in cellular state by performing molecular assays at multiple time points. RNA sequencing (RNA-seq) data from these experiments can be combined with differential gene expression to identify the genes that are significantly up- or down-regulated in response to the perturbation at each time point. To identify enriched TF modules for an input gene set, we previously developed ChEA-KG. ChEA-KG is a TF enrichment analysis tool that serves a background human gene regulatory network of 1,559 human TF nodes connected by 131,181 signed and directed edges. Here, we adapt ChEA-KG to create ChEA-KG Time Series (ChEA-KG-TS), an automated workflow to identify TF regulatory modules from time series RNA-seq data. The workflow automatically calculates  up- and down-regulated gene sets between time points using Characteristic Direction or DESeq2. The gene sets are submitted to ChEA3, a TF enrichment analysis tool, to predict the likely TF regulators for each comparison. The enriched TFs are queried in ChEA-KG to identify regulatory interactions between each comparison. The results are summarized in an automatically generated report including interactive visualizations of the enrichment analysis results and regulatory subnetworks as well as UMAP projections of the enriched TFs at each time point.

## Input Types
ChEA-KG-TS offers two input options. Example files are available for both input types by clicking on the download button next to "Load Example" (Fig 1, 2).

### Option 1: RNA-seq Data Matrix
This input type enables users to automatically generate up/down gene sets based on an RNA-seq data matrix and sample metadata (Fig 1). The RNA-seq file provides the raw gene counts for multiple samples measured at various time points. Each time point must have at least 2 replicates in order to perform differential expression analysis. 

<div style="display: flex; gap: 40px; justify-content: center; max-width: 1200px; margin: 0 auto;">
<img src="static/fig1.png" alt="The RNA-seq upload page" width=600>
</div>

**Figure 1.** RNA-seq file upload page. The red boxes highlight where the example files can be downloaded.

RNA-seq file requirements:
- Must be in the form of a gene count matrix
- Counts must be raw (unnormalized)
- Gene column **must** be named "gene_id" or "gene_name" (Table 1A)
- Acceptable gene names: ENSG and Entrez gene symbols

Sample metadata requirements:
- Each row should list a sample and its corresponding time point
- Each time point must have at least two replicates
- Columns **must** be named "sample_name" and "time_pt_annotation"
- **Please ensure your metadata is listed in ascending order with respect to "time_pt_annotation". The first time point will be the baseline, the next will be time point 1, etc. (Table 1B)**

<div style="display: flex; gap: 40px; justify-content: center; max-width: 1200px; margin: 0 auto;">
<div>

**Table 1A. Example gene count matrix:**   

| gene_id | Sample 1 | Sample 2 | Sample 3 |
|------|-------|-------|-------|
| ENSG000... | 525 | 509 | 551 |
| ENSG000... | 0 | 0 | 0 |
| ENSG000...| 941 | 875 | 980 |

</div>
<div>

**Table 1B. Example sample metadata:**   

| sample_name | time_pt_annotation |
|------|-------|
| H00_S1 | hour_0 | 
| H00_S2 | hour_0 | 
| H01_S1 | hour_1 | 
| H01_S2 | hour_1 | 

</div>
</div>

#### Associated parameters:
The following parameters apply to RNA-seq file uploads (Fig 1A)
1. **Differential expression method:** Users may choose to identify up/down gene sets using DESeq2 [(read more here)](https://doi.org/10.1186/s13059-014-0550-8) or the Characteristic Direction method [(read more here)](https://doi.org/10.1186/1471-2105-15-79), or both. 
2. **Number of top enriched TFs:** Choose to view the top 5 or top 10 most highly ranked enriched TFs from ChEA3. 
3. **Study title:** Optionally, provide a title for your study
4. **Study description:** Optionally, provide a description of your study 

<div style="display: flex; gap: 40px; justify-content: center; max-width: 1200px; margin: 0 auto;">
<img src="static/fig1a.png" alt="The RNA-seq upload page" width=600>
</div>

**Figure 1a.** RNA-seq file upload associated parameters.

### Option 2: GMT Files
Allows users to upload precomputed up and down gene sets (Fig 2)

<div style="display: flex; gap: 40px; justify-content: center; max-width: 1200px; margin: 0 auto;">
<img src="static/fig2.png" alt="The GMT file upload page" width=600>
</div>

**Figure 2.** GMT file upload page. The red boxes highlight where the example files can be downloaded.


- Gene sets should compare either adjacent time points (eg hour 1 vs hour 2), or each time point versus a baseline (eg hour 0). Only one GMT is required, but both may be provided
- GMT files should be formatted as:

<div style="display: flex; gap: 40px; justify-content: center; max-width: 1200px; margin: 0 auto;">
<div>

**Example GMT, Time Points vs T0**

| Term | Genes |
|------|-------|
| T1_vs_T0_up | TP53, MYC, BRCA1 |
| T2_vs_T0_up | STAT3, JUN, FOS |
| T3_vs_T0_up | VEGFA, HIF1A, BCL2 |

</div>
<div>

**Example GMT, Adjacent Time Points**

| Term | Genes |
|------|-------|
| T1_vs_T0_up | TP53, MYC, JUN |
| T2_vs_T1_up | STAT3, IL6, TNF |
| T3_vs_T2_up | VEGFA, HIF1A, LDHA |

</div>
</div>

#### Associated parameters:
The following parameters apply to GMT file uploads (Fig 2A)
1. **Number of top enriched TFs:** Choose to view the top 5 or top 10 most highly ranked enriched TFs from ChEA3. 
2. **Study title:** Optionally, provide a title for your study
3. **Study description:** Optionally, provide a description of your study

<div style="display: flex; gap: 40px; justify-content: center; max-width: 1200px; margin: 0 auto;">
<img src="static/fig1a.png" alt="The RNA-seq upload page" width=600>
</div>

**Figure 2a.** GMT file upload associated parameters. 


## Report execution and accessing your results: 
After submission, ChEA-KG-TS produces an automatically generated report (Fig 3). **Each report is only accessible via its unique URL, unless that URL is shared by the user.** The report may take several minutes to load but can be revisted at any time at the same URL. While results are computing "Executing..." will display at the top of the screen.

<div style="display: flex; gap: 40px; justify-content: center; max-width: 1200px; margin: 0 auto;">
<img src="static/fig3.png" alt="The RNA-seq upload page" width=600>
</div>

**Figure 3.** Example of a report for which the results are still being computed. "Executing..." displays at the top while the report completes. The three black dots indicate which section of the report is currently being computed.

## Results:
The report includes the following components:

#### 0. Differential Expression Results
For RNA-seq data matrix inputs, differential expression is computed using the algorithm selected by the user - either DESeq2, Characteristic Direction, or both. For each method and input dataset, two comparisons are made. The first is between adjacent time point comparisons (Fig 4A; eg hour 1 vs hour 2). The second is between each time point and the baseline, which is assumed to be the first timepoint in the metadata list (Fig 4A). 

<div style="display: flex; gap: 40px; justify-content: center; max-width: 1200px; margin: 0 auto;">
<img src="static/fig0.png" alt="The RNA-seq upload page" width=600>
</div>

**Figure 4A.** Example summary of differential expression results when "DESeq2" is selected as the method. 

#### 1. Enriched Transcription Factor Regulatory Subnetwork 
The JSON file created in step 3 is used to visualize the regulatory network using ball-and-stick diagrams. Blue and red nodes correspond to TFs enriched for upregulated and downregulated gene sets at the given time point, respectively. Activation (green) or inhibition (red) arrows are drawn between TFs at adjacent time points (as determined by ChEA-KG), therefore forming a regulatory subnetwork of all the enriched TFs (Fig 4B).
 
<div style="display: flex; gap: 40px; justify-content: center; max-width: 1200px; margin: 0 auto;">
<img src="static/fig4a.png" alt="The RNA-seq upload page" width=600>
</div>

**Figure 4B.** Example of a transcription factor regulatory subnetwork output. The static image can be downloaded as a PNG or SVG by clicking at the links below the figure.

#### 2. Bar graph representation of enriched TF ranks
The bar graphs below depict the ranks of the top enriched TFs across the TF-target gene set libraries in ChEA3 (Keenan et al., 2019). Bar graphs are shown for the enriched TFs for the "up" and "down" gene sets at each time point (Fig 4C).  

Here, a TF's rank within a given library refers to how well the TF's target genes within that library overlap with the input gene set (e.g. up genes at the "hour 3 vs hour 1" comparison) compared to other TFs within that library. The top enriched TFs are computed by finding the TFs with the lowest average rank across all six ChEA3 libraries (referred to as the MeanRank method).  

<div style="display: flex; gap: 40px; justify-content: center; max-width: 1200px; margin: 0 auto;">
<img src="static/fig4b.png" alt="The RNA-seq upload page" width=600>
</div>

**Figure 4C.** Example of the enriched TF rank bar graph output. The static image can be downloaded as a PNG or SVG by clicking at the links below the figure. 

#### 3. Interactive UMAP visualization of the enriched TFs
The enriched transcription factors from each time point are colored on a UMAP plot of 700 TFs identified by ChEA-KG to be "source TFs" (i.e. they exert regulatory effects on other TFs). The UMAP algorithm was performed using the TF-IDF scores of the TFs' target genes, meaning that TFs are placed in the same cluster if they generally regulate similar genes (Fig 4D).

<div style="display: flex; gap: 40px; justify-content: center; max-width: 1200px; margin: 0 auto;">
<img src="static/fig4c.png" alt="The RNA-seq upload page" width=600>
</div>

**Figure 4D.** Example of the UMAP visualization. The animated GIF is downloadable via the link under the image. 
