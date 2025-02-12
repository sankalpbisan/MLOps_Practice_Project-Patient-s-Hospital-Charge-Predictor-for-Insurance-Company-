import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
#from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

#@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.raw_data_path = os.path.join(os.getcwd(),'artifacts','raw.csv')
        self.train_data_path = os.path.join(os.getcwd(),'artifacts','train.csv')
        self.test_data_path = os.path.join(os.getcwd(),'artifacts','test.csv')
    
class DataIngestion:
    def __init__(self):
        logging.info("Data Ingestion initiated")
        self.data_ingestion_config = DataIngestionConfig()

    def read_data(self):
        try:
            df = pd.read_csv(os.path.join('notebook','insurance.csv'))
            os.makedirs('artifacts',exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False)
            logging.info("Raw Data read and saved to \"artifacts\" dir successfully")
            return df
        except Exception as e:
            raise CustomException(e,sys)

    def get_data(self):
        try:
            data = self.read_data()
            train_set,test_set = train_test_split(data,test_size=0.2,random_state=0)
            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False)
            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False)
            # logging.info("Data split into train and test set and saved to \"artifacts\" dir successfully")
            logging.info("Data Ingestion Completed")
            return self.data_ingestion_config.train_data_path,self.data_ingestion_config.train_data_path
        except Exception as e:
            raise CustomException(e,sys)
        
# if __name__ == "__main__":
#     data_ingestion_obj = DataIngestion()
#     train,test = data_ingestion_obj.get_data()
#     # logging.info("Data Ingestion completed successfully")
#     print(train,test)
