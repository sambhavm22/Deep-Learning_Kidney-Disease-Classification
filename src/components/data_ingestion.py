import zipfile
from src import logger
import os 
from pathlib import Path
from src.utils.common import get_size
from src.constants import *
from src.entity.config_entity import DataIngestionConfig
from zipfile import ZipFile
import urllib.request as request
import gdown
import requests
from io import BytesIO


class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        
        try: 
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_download_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e 
        
    def extract_zip_file(self):

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)


    def download_and_extract_zip(zip_url, destination_folder):
        """
        Download a zip file from a URL and extract its contents to a specified folder.

        Parameters:
        - zip_url (str): The URL of the zip file.
        - destination_folder (str): The local folder where the contents will be extracted.

        Returns:
        - bool: True if the zip file is downloaded and extracted successfully, False otherwise.
        """
        try:
            # Send a GET request to the URL
            response = requests.get(zip_url)
            response.raise_for_status()  # Raise an exception for bad responses (e.g., 404 Not Found)

            # Extract the contents of the zip file
            with zipfile.ZipFile(BytesIO(response.content), 'r') as zip_ref:
                zip_ref.extractall(destination_folder)

            print(f"Zip file downloaded and extracted to '{destination_folder}'.")
            return True
        except Exception as e:
            print(f"Error downloading and extracting zip file: {e}")
            return False

    # Example Usage:
    zip_url = 'https://example.com/sample.zip'
    destination_folder = 'path/to/extracted/folder'
    success = download_and_extract_zip(zip_url, destination_folder)

    if success:
        print("Download and extraction successful.")
    else:
        print("Failed to download and extract zip file.")
            