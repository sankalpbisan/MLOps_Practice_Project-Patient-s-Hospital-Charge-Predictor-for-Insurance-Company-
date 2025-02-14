import os
import sys
from xgboost import XGBRegressor
from dataclasses import dataclass
from sklearn.svm import LinearSVR
from sklearn.metrics import r2_score
from catboost import CatBoostRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import (AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor)

from src.utils import root_dir
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join(root_dir,'artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def get_model_details














# transformation = DataTransformation()
# transformation_result_set = transformation.transform_data(os.path.abspath("artifacts/train.csv"))
#
# print(transformation_result_set)
# print(type(transformation_result_set))
