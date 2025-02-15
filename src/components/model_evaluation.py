import os
import sys
import pandas as pd
from src.logger import logging
from src.utils import load_object
from sklearn.metrics import r2_score
from src.exception import CustomException
from src.components.model_training import ModelTrainer


class ModelEvaluation:
    def __init__(self):
        '''
        This method fetches the model, transformer and test data path
        '''
        self.model_path = ModelTrainer().model_trainer()
        self.test_data_path = os.path.join(os.path.abspath('artifacts/test.csv'))
        self.transformer_path = os.path.join(os.path.abspath('artifacts/transformer.pkl'))
        logging.info("Fetched the test data, transformer and model path")

    def test_evaluation(self):
        '''
        This method performs Evaluation on test_data set
        Returns: r2_score
        '''
        try:
            logging.info("Evaluating the model on test set (kept aside from the start)")

            transformer = load_object(self.transformer_path)
            model = load_object(self.model_path)
            test_data = pd.read_csv(self.test_data_path)
            logging.info("Test data, Transformer and Model loaded")

            #Splitting data into input features and target attribute
            x_test,y_test = test_data.iloc[:,:-1], test_data.iloc[:,-1]

            #Transforming and predicting test_data
            processed_test_data = transformer.transform(x_test)
            test_pred = model.predict(processed_test_data)
            logging.info("Test data processed and prediction completed")

            r2 = r2_score(y_test,test_pred)
            logging.info(f"Score of prediction on test data: {r2}")

            return f"Score(r_score) of the final selected model on test data is: {r2} "

        except Exception as e:
            raise CustomException(e,sys)
