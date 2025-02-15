import os
import sys
from src.logger import logging
from xgboost import XGBRegressor
from dataclasses import dataclass
from sklearn.svm import LinearSVR
from sklearn.metrics import r2_score
from catboost import CatBoostRegressor
from src.exception import CustomException
from src.utils import root_dir, save_object
from sklearn.linear_model import SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from src.components.data_transformation import DataTransformation
from sklearn.ensemble import (AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor)


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join(root_dir,'artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        '''
        This method initializes the config files used for model training
        '''
        self.model_trainer_config = ModelTrainerConfig()

    def model_trainer(self):
        '''
        This method unger-go model training and selection.
        Returns: Path of the model saved in pickle file format
        '''
        try:
            logging.info("Models has been listed")

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Linear SVM" : LinearSVR(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "SGD Regressor": SGDRegressor(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "XG-Boost Regressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
            logging.info("Models has been listed")

            params = {
                "Random Forest": {
                    'n_estimators': [8, 16, 32, 64, 128, 256,500],
                    'max_depth': [2, 3, 4, 5],
                    'max_features': [4, 5, 6]
                },
                "Decision Tree": {
                    'criterion': ['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    'max_depth': [2, 3, 4,5],
                    'max_features' : [4,5,6]
                },
                "Linear SVM":{
                    'C': [1,50,100,1000],
                    'epsilon': [0,1,5,10,20]
                },
                "Gradient Boosting": {
                    'learning_rate': [.1, .01, .05, .001],
                    'subsample': [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                },
                "Linear Regression": {},
                "SGD Regressor":{
                    'penalty':['l2', 'l1', 'elasticnet'],
                    'alpha':[0.0001, 0.0005,0.001,0.0015,0.0020]
                },
                "K-Neighbors Regressor": {
                    'n_neighbors': [3, 5, 7, 9, 12, 15],
                    'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
                },
                "XG-Boost Regressor": {
                    'learning_rate': [.1, .01, .05, .001],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                },
                "CatBoosting Regressor": {
                    'depth': [6, 8, 10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor": {
                    'learning_rate': [.1, .01, 0.5, .001],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                }
            }
            logging.info("Parameters has been listed")

            #Fetching data
            train_data,valid_data,x = DataTransformation().transform_data(os.path.abspath('artifacts/train.csv'))
            x_train, y_train = train_data[:,:-1], train_data[:,-1]
            x_valid, y_valid = valid_data[:, :-1], valid_data[:, -1]
            logging.info("Data is loaded and split")

            logging.info("Training started....")
            report = {}
            # Training models over iteration
            for i in range(len(list(models))):
                model =  list(models.values())[i]
                para = params[list(models.keys())[i]]

                gs = GridSearchCV(model,para,cv=10)
                gs.fit(x_train,y_train)

                logging.info(f"Iteration no.{i} found best params/estimator as: {gs.best_estimator_}")

                model.set_params(**gs.best_params_)
                model.fit(x_train,y_train)

                y_train_pred = model.predict(x_train)
                y_valid_pred = model.predict(x_valid)

                train_model_score = r2_score(y_train,y_train_pred)
                valid_model_score = r2_score(y_valid, y_valid_pred)

                logging.info(f"Iteration no.{i}: train_score-{train_model_score},valid_score-{valid_model_score}")

                report[list(models.keys())[i]] = valid_model_score

            logging.info("Model Training Completed")

            logging.info("Now, findig best model out of all models")

            # Getting best score of all models
            best_model_score = max(sorted(report.values()))

            # Getting best model's params of all models
            best_model_name = list(report.keys())[
                list(report.values()).index(best_model_score)
            ]

            if best_model_score < 0.6:
                raise CustomException("No best model found")

            best_model = gs.best_estimator_
            logging.info(f"Found best model:{best_model} with score of {best_model_score}")

            logging.info("Now, saving the model in to pickle file")
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            logging.info("Pickle file saved successfully")

            return self.model_trainer_config.trained_model_file_path

        except Exception as e:
            raise CustomException(e,sys)

