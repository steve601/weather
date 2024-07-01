import sys
import pandas as pd
from source.commons import load_object
from source.exception import UserException
from source.logger import logging
from sklearn.preprocessing import LabelEncoder


class PredicPipeline:
    def __init__(self):
        pass
    
    logging.info('Preprocessing user input and making predictions')
    def predict(self,features):
        model_path = 'elements\model.pkl'
        preprocessor_path = 'elements\preprocessor.pkl'
        # loaeding objects
        model = load_object(model_path)
        preprocessor = load_object(preprocessor_path)
        data_scaled = preprocessor.transform(features)
        prediction = model.predict(data_scaled)
        
        return prediction
logging.info('This class is responsible for mapping all the inputs from html to flask')
class UserData:
    def __init__(self,
                 temperature,humidity,wind,precipitation,cloud,atmospheric,
                 uv,season,visibility,location):
        self.temp = temperature
        self.hum = humidity
        self.wind = wind
        self.prec = precipitation
        self.cloud = cloud
        self.atm = atmospheric
        self.uv = uv
        self.season = season
        self.visi = visibility
        self.loca = location
        
    # let's write a function that returns the user input as a numpy array
    def get_data_as_df(self):
        try:
            user_data = {
                'temperature':[self.temp],
                "humidity":[self.hum],
                "wind speed":[self.wind],
                "precipitation (%)":[self.prec],
                "cloud cover":[self.cloud],
                "atmospheric pressure":[self.atm],
                "uv index":[self.uv],
                "season":[self.season],
                "visibility (km)":[self.visi],
                "location":[self.loca]
            }
            return pd.DataFrame(user_data)
        except Exception as e:
            raise UserException(e,sys)
        