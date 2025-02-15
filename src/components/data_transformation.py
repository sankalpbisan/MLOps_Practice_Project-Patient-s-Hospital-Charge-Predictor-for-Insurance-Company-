import os
import sys
import numpy as np
import pandas as pd
from src.logger import logging
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from src.exception import CustomException
from src.utils import root_dir,save_object
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder


@dataclass()
class DataTransformationConfig:
    transformer_obj_file_path = os.path.join(root_dir,'artifacts','transformer.pkl')

class DataTransformation:
    def __init__(self):
        '''
        This function initializes the config files needed for DataTransformation
        '''
        self.data_transformer_config = DataTransformationConfig()

    def get_transformer(self):
        '''
        This function create the Column Transformer object for numerical and categorical columns
        Returns: Column Transformer Object
        '''
        try:
            cat_cols = ['sex', 'smoker', 'region']
            num_cols = ['age',	'bmi',	'children']

            num_pipeline = Pipeline(
                steps = [
                    ("scaler",StandardScaler())
                ]
            )
            logging.info("Numerical Pipeline Created")

            cat_pipeline = Pipeline(
                steps=[
                    ("one_hot_enc",OneHotEncoder())
                ]
            )
            logging.info("Categorical Pipeline Created")

            col_transformer = ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,num_cols),
                    ("col_pipeline",cat_pipeline,cat_cols)
                ]
            )
            logging.info("Column Transformer Created and returned")

            return col_transformer

        except Exception as e:
            raise CustomException(e,sys)


    def transform_data(self,train_data_path):
        '''
        This method is responsible for all the modifications that needs to be done to the dataset.
        Returns: Preprocessed data for training and validation set and Data Transformer Object path
        '''
        try:
            logging.info("Data Transformation begin...")
            target_col = "charges"

            train_data = pd.read_csv(train_data_path)
            train_d,valid_d = train_test_split(train_data, random_state=None)

            train_input_features = train_d.drop(target_col,axis=1)
            valid_input_features = valid_d.drop(target_col,axis=1)
            logging.info("Train and Validation set created")

            #Getting the transformer object
            transformer_obj = self.get_transformer()
            logging.info("Transformer object grabbed")

            #Applying transformation on train and validation data
            processed_train_inp_features = transformer_obj.fit_transform(train_input_features)
            processed_valid_inp_features = transformer_obj.fit_transform(valid_input_features)
            logging.info("Training and validation data processed successfully")

            #Concateneting Data
            processed_train_data = np.c_[processed_train_inp_features,np.array(train_d[target_col])]
            processed_valid_data = np.c_[processed_valid_inp_features, np.array(valid_d[target_col])]
            logging.info("Training and validation data has been prepared.")

            save_object(
                file_path = self.data_transformer_config.transformer_obj_file_path,
                obj = transformer_obj
            )
            logging.info("Transformation is completed and the transformer is loaded and stored as pickle file")

            return(
                processed_train_data,
                processed_valid_data,
                self.data_transformer_config.transformer_obj_file_path
            )

        except Exception as e:
            raise CustomException(e,sys)
