import os
import sys
import dill

from src.exception import CustomException
#from src.logger import logging

root_dir =os.getcwd()
#root_dir = os.path.dirname(os.getcwd())

def save_object(file_path,obj):
    try:
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)


