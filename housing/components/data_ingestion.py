from housing.entity.config_entity import DataIngestionConfig
from housing.exception import HousingExeption
import sys,os 
from housing.logger import logging
from housing.entity.artifact_entity import DataIngestionArtifact
# neccesary library for data downloading
import tarfile
from six.moves import urllib


class DataIngestion:
    
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20}")
            self.data_ingestion_config=data_ingestion_config
        except Exception as e: 
            raise HousingExeption(e,sys) 
        
    # create a function for dowload the data
    def download_housing_data(self,)->str:
        try:
            # extracting remote url to download dataset 
            download_url = self.data_ingestion_config.dataset_download_url 
            
            #Folder remote url to download dataset 
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir
            
            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)
            os.makedirs(tgz_download_dir,exist_ok=True)
            
            # this is used for extract file name from url 
            housing_file_name = os.path.basename(download_url)
            
            # now complete file path 
            tgz_file_path=os.path.join(tgz_download_dir,housing_file_name)
            
            # now donload the file
            logging.info(f"Downloading file from :{download_url} into {tgz_file_path}")
            urllib.request.urlretrieve(download_url,tgz_file_path)
            logging.info(f"File :[{tgz_file_path}] has been downloaded succesfully")
            
            return tgz_file_path
            
        
        except Exception as e:
            raise HousingExeption(e,sys) from e 
    
    #create a fucntion for extract the data
    def extract_tgz_file(self,tgz_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            
            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)
            os.makedirs(raw_data_dir,exist_ok=True)
            
            logging.info(f"Extracting tgz file:[{tgz_file_path}] into dir: [{raw_data_dir}]")
            with tarfile.open(tgz_file_path) as housing_tgz_file_obj:
                housing_tgz_file_obj.extractall(path=raw_data_dir)
            
            logging.info("Extraction completed")
            
            
        except Exception as e:
            raise HousingExeption(e,sys) from e  
    
    # create a function for split the data into train and test
    def split_data_as_train_test(self)->DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
        except Exception as e:
            raise HousingExeption(e,sys) from e 
        
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            tgz_file_path = self.download_housing_data()
            
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
        except Exception as e:  
            raise HousingExeption(e,sys) from e 