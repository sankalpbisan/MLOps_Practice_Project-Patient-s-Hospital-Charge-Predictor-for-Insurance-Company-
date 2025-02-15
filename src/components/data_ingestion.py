import os
import sys
import pandas as pd
from src.utils import root_dir
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split


class DataIngestionConfig:
    '''
    Initializes the parameters that store the path of the artifacts
    '''
    def __init__(self):
        self.raw_data_path = os.path.join(os.getcwd(),'artifacts','raw.csv')
        self.train_data_path = os.path.join(os.getcwd(),'artifacts','train.csv')
        self.test_data_path = os.path.join(os.getcwd(),'artifacts','test.csv')
    
class DataIngestion:
    def __init__(self):
        '''
        This method initializes the config files needed for Data-Ingestion
        '''
        logging.info("Data Ingestion initiated")
        self.data_ingestion_config = DataIngestionConfig()

    def read_data(self):
        '''
        This method reads the data from existing csv file
        Returns: Dataframe of csv data
        '''
        try:
            df = pd.read_csv(os.path.join(root_dir,'notebook','insurance.csv'))
            os.makedirs('artifacts',exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False)
            logging.info("Raw Data read and saved to \"artifacts\" dir successfully")
            return df
        except Exception as e:
            raise CustomException(e,sys)

    def get_data(self):
        '''
        This method split data into train and test file
        Returns: path of the train and test file
        '''
        try:
            data = self.read_data()
            train_set,test_set = train_test_split(data,test_size=0.2,random_state=0)
            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False)
            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False)
            # logging.info("Data split into train and test set and saved to \"artifacts\" dir successfully")
            logging.info("Data Ingestion Completed")
            return self.data_ingestion_config.train_data_path,self.data_ingestion_config.test_data_path
        except Exception as e:
            raise CustomException(e,sys)
        
