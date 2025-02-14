import os
import sys
import dill
import pickle
#from src.exception import CustomException

root_dir = os.getcwd()
#root_dir = os.path.dirname(os.getcwd())

def save_object(file_path,obj):
    try:
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    # except AttributeError:
    #     raise AttributeError("Error occurred while dumping object")
    except Exception as e:
        raise f"Error [{e}] occurred while saving model/object" #CustomException(e,sys)

def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)

    # except AttributeError:
    #     raise AttributeError("Error occurred while dumping object")
    except Exception as e:
        raise f"Error [{e}] occurred while loading model/object"



