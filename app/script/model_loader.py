import pickle
import os
from config import config
class Model:
    def __init__(self,model_name,version_no) -> None:
        self.model_name=model_name
        self.version_no=version_no
        self.load()
    def load(self,):
        self.model =pickle.load(open(os.path.join(os.getcwd(),config.MODEL_DIRCTORY,self.model_name),"rb"))
    def predict(self,data):
        return self.model.predict(data)