# ChEA-KG Time Series Appyter
Given either raw time series RNA-seq data or pre-computed DEGs at each time point, the ChEA-KG-TS Appyter visualizes on a regulatory subnetwork how the enriched TFs at one time point regulate the enriched TFs at the subsequent time point, therefore enabling users to understand how the TF landscape governing a biological process evolves over time. The Appyter also determines which modules of TFs may be targeting similar genes at each time point by visualizing how the enriched TFs cluster on a UMAP plot. The Appyter also outputs the average rank of each enriched TF within the ChEA3 gene set libraries, enabling users to see which TFs may play a more substantial role in dictating the gene expression changes at each time point.

## Development
`cp .env.example .env`

`pip install -r requiements.txt`

`appyter chea_kg_ts_appyter.ipynb --extras=ipywidgets --extras=toggle-code`

View the site at <http://localhost:5000>

## Deploy
`docker compose build chea-kg-timeseries # build the container`

`docker compose up -d # verify that it works the way you expect at http://localhost:5050`

`docker compose push` # push container

`sshkube run kube-compose up` # run on server
