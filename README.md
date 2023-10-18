# Deep-Learning_Kidney-Disease-Classification

In this project we have used google drive to store the dataset which is in ".zip" format. We have used "gdown" module to download the data from google drive

# Workflows

1. Update config.yaml
2. update params.yaml
3. update the entity/config_entity
4. update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the dvc.yaml

ML flow is an open source platform to manage the ML lifecycle, including experimentation, reproducibility, deployment and a central model registry. ML flow currently offers four components: -

1. ML flow tracking: - Record and query experiments: code, data, config and results. 
2. ML flow projects: -Package data science code in a format to reproduce runs on any platform.
3. ML flow Models: -Deploy machine learning models in diverse serving environments
4. Model Registry: - Store, annotate, discover, and manage models in a central repository. 


MLFLOW_TRACKING_URI=https://dagshub.com/sambhavm22/Deep-Learning_Kidney-Disease-Classification.mlflow \
MLFLOW_TRACKING_USERNAME=sambhavm22 \
MLFLOW_TRACKING_PASSWORD=6d1de6019148e45b06aecdca12063b4dabffa0ae \
python script.py