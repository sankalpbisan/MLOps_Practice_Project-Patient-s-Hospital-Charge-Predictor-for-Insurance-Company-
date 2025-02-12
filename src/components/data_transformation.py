import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion

try:
    data_ingestion_obj = DataIngestion()
    train,test = data_ingestion_obj.get_data()
    logging.info("Data Ingestion completed successfully")
except Exception as e:
    raise CustomException(e,sys)

print(train,test)

'''
class DataTransformationConfig:
    def __init__(self):
        pass
'''
