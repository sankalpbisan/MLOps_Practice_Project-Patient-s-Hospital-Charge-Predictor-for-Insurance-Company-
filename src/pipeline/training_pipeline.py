import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTrainer
from src.components.model_evaluation import ModelEvaluation


class TrainPipeline:
    def __init__(self):
        pass

        '''
        This methods initializes all the required config files
        
        ingest_config = DataIngestion().data_ingestion_config
        transf_config = DataTransformation().data_transformer_config
        model_config = ModelTrainer().model_trainer_config
        '''

    def ingestion(self):
        '''
        This method executes the Data Ingestion process
        '''
        try:
            logging.info("Data-Ingestion started")
            ingest_obj = DataIngestion()
            train_data_path,test_data_path = ingest_obj.get_data()
            logging.info("DataIngestion Completed")
            return train_data_path,test_data_path
        except Exception as e:
            raise CustomException(e,sys)

    def transformation(self,train_data_path):
        '''
        This method calls and executes the Data Transformation process
        '''
        try:
            logging.info("Data Transformation Started")
            transf_obj = DataTransformation()
            processed_train_data, processed_valid_data,transf_obj_file_path = transf_obj.transform_data(train_data_path)
            logging.info("Data Transformation Ended")
            return processed_train_data, processed_valid_data,transf_obj_file_path
        except Exception as e:
            raise CustomException

    def training(self):
        '''
        This method calls and execute the Model Training module
        '''
        try:
            logging.info("Model Training Started")
            model_trainer_obj = ModelTrainer()
            model_obj_path = model_trainer_obj.model_trainer()
            logging.info("Model Training Ended")
            return model_obj_path
        except Exception as e:
            raise CustomException(e,sys)

    def evaluation(self):
        '''
        This method runs test set on selected model
        '''
        try:
            logging.info("Model Evaluation Started")
            eval_model = ModelEvaluation()
            r2 = eval_model.test_evaluation()
            logging.info("Model Evaluation Ended")
            return r2
        except Exception as e:
            raise CustomException(e,sys)

    def run_pipeline(self):
        '''
        This method runs all methods defined in this pipeline
        '''
        try:
            logging.info("Pipeline Execution has Started...")
            train_data_path,test_data_path = self.ingestion()
            self.transformation(train_data_path)
            self.training()
            self.evaluation()
            logging.info("Pipeline Execution has Ended...")
        except Exception as e:
            raise CustomException(e,sys)


pipeline_obj = TrainPipeline()
pipeline_obj.run_pipeline()



