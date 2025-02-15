import os
import dill

#Project Root Directory
root_dir = os.getcwd()

#Saving an object into a pickle file
def save_object(file_path,obj):
    try:
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise f"Error [{e}] occurred while saving model/object" #CustomException(e,sys)


#Loading an object from a pickle file
def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise f"Error [{e}] occurred while loading model/object"



