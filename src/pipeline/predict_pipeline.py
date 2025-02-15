import os
import sys

import pandas as pd

#from src.logger import logging
from src.exception import CustomException
from src.utils import load_object


class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self,feature):
        try:
            # logging.info("Prediction Initiated")
            transformer = load_object(os.path.abspath('artifacts/transformer.pkl'))
            model = load_object(os.path.abspath('artifacts/model.pkl'))
            raw_data = feature
            prep_data = transformer.transform(raw_data)
            pred = model.predict(prep_data)
            return pred
        except Exception as e:
            raise CustomException(e,sys)

class LoadData:
    def __init__(self,
                 age:int,
                 sex:str,
                 bmi:float,
                 children:int,
                 smoker:str,
                 region:str):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region

    def load_data(self):
        try:
            data_df = {
                "age":      [self.age],
                "sex":      [self.sex],
                "bmi" :     [self.bmi],
                "children": [self.children],
                "smoker":   [self.smoker],
                "region":   [self.region]
            }
            return pd.DataFrame(data_df)
        except Exception as e:
            raise CustomException(e,sys)