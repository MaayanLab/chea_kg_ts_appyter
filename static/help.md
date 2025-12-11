# ChEA-KG-TS Tutorial

## Abstract
Transcription factors (TFs) are key regulators of gene expression. Understanding the complex ways in which they interact is critical to unravel how biological pathways such as disease, aging, and development are controlled. TF modules can change over time, for example in response to perturbations including exercise or chemical treatments. Time series experiments measure these temporal changes in cellular state by performing molecular assays at multiple time points. RNA sequencing (RNA-seq) data from these experiments can be combined with differential gene expression to identify the genes that are significantly up- or down-regulated in response to the perturbation at each time point. To identify enriched TF modules for an input gene set, we previously developed ChEA-KG. ChEA-KG is a TF enrichment analysis tool that serves a background human gene regulatory network of 1,559 human TF nodes connected by 131,181 signed and directed edges. Here, we adapt ChEA-KG to create ChEA-KG Time Series (ChEA-KG-TS), an automated workflow to identify TF regulatory modules from time series RNA-seq data. The workflow automatically calculates  up- and down-regulated gene sets between time points using Characteristic Direction or DESeq2. The gene sets are submitted to ChEA3, a TF enrichment analysis tool, to predict the likely TF regulators for each comparison. The enriched TFs are queried in ChEA-KG to identify regulatory interactions between each comparison. The results are summarized in an automatically generated report including interactive visualizations of the enrichment analysis results and regulatory subnetworks as well as UMAP projections of the enriched TFs at each time point. We apply ChEA-KG-TS to two use cases. First, we identify master regulatory networks in the liver that control gene expression in response to exercise, using data from the Molecular Transducers of Physical Activity Consortium (MoTrPAC). Next, we use time series data from triple negative breast cancer (TNBC) treated with the TRAIL cytokine to reveal mechanisms underlying tumor cell response to treatment.


## Input Types
ChEA-KG-TS offers two input options. Example files are available for both input types by clicking on the download button next to "Load Example" (Fig 1, 2).

### Option 1: RNA-seq Data
This input type enables users to automatically generate up/down gene sets. Two files are required, an RNA-seq file and sample metadata (Fig 1).

<div style="display: flex; gap: 40px; justify-content: center; max-width: 1200px; margin: 0 auto;">
<img src="static/fig1.png" alt="The RNA-seq upload page" width=600>
</div>

**Figure 1.** RNA-seq file upload page. The red boxes highlight where the example files can be downloaded.

RNA-seq file requirements:
- Must be in the form of a gene count matrix
- Counts must be raw
- Gene column **must** be named "gene_id" or "gene_name"
- Acceptable gene names: ENSG and Entrez gene symbols

Sample metadata requirements:
- Each row should list a sample and its corresponding time point
- Columns **must** be named "sample_name" and "time_pt_annotation"

<div style="display: flex; gap: 40px; justify-content: center; max-width: 1200px; margin: 0 auto;">
<div>

**Example gene count matrix:**   

| Gene | Sample 1 | Sample 2 | Sample 3 |
|------|-------|-------|-------|
| ENSG000... | 525 | 509 | 551 |
| ENSG000... | 0 | 0 | 0 |
| ENSG000...| 941 | 875 | 980 |

</div>
<div>

**Example sample metadata:**   

| sample_name | time_pt_annotation |
|------|-------|
| Sample1 | hour_0 | 
| Sample2 | hour_1 | 
| Sample1 | hour_0 | 
| Sample3 | hour_1 | 

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


- Gene sets should compare either adjacent time points (eg hour 1 vs hour 2), or each time point versus a baseline (usually t=0). Only one GMT is required, but both may be provided
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

1. TF Enrichment Analysis results
2. Enriched Transcription Factor Regulatory Subnetwork
3. Interactive UMAP visualization

