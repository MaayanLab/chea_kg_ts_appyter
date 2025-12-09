# ChEA-KG Time Series Appyter
Given either raw time series RNA-seq data or pre-computed DEGs at each time point, the ChEA-KG-TS Appyter visualizes on a regulatory subnetwork how the enriched TFs at one time point regulate the enriched TFs at the subsequent time point, therefore enabling users to understand how the TF landscape governing a biological process evolves over time. The Appyter also determines which modules of TFs may be targeting similar genes at each time point by visualizing how the enriched TFs cluster on a UMAP plot. The Appyter also outputs the average rank of each enriched TF within the ChEA3 gene set libraries, enabling users to see which TFs may play a more substantial role in dictating the gene expression changes at each time point.

## Development
```
cp .env.example .env
python3.9 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

appyter main.ipynb --extras=ipywidgets --extras=toggle-code --profile=bootstrap
```
View the site at <http://localhost:5000>

## Deploy
```
docker compose build chea-kg-timeseries # build the container

docker compose up -d
# verify that it works the way you expect at http://localhost:5050

docker compose push # push container

sshkube run kube-compose up # run on server
```

## Network Visualization
The notebook used to build the D3 network visualization is available here: https://observablehq.com/@anna26/chea-kg-cytoscape-network
