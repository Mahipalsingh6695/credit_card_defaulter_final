import os
import sys
import pandas as pd
from src.CreditCardDefaulter.exception import customexception
from src.CreditCardDefaulter.logger import logging
from src.CreditCardDefaulter.utils.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    
    
    def predict(self,features):
        try:
            print("inside predict funtion")
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")
            
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            print("model loaded path", model_path)
            
            scaled_data=preprocessor.transform(features)
            print("scaled_data",scaled_data)
            
            pred=model.predict(scaled_data)
            print("prediction successful", pred)
            
            return pred
        
        except Exception as e:
            raise customexception(e,sys)
    

class CustomData:
    def __init__(self,
                 LIMIT_BAL:float,
                 SEX:float,
                 EDUCATION:float,
                 MARRIAGE:float,
                 AGE:float,
                 PAY_0:float,
                 PAY_2:float,
                 PAY_3:float,
                 PAY_4:float,
                 PAY_5:float,
                 PAY_6:float,
                 BILL_AMT1:float,
                 BILL_AMT2:float,
                 BILL_AMT3:float,
                 BILL_AMT4:float,
                 BILL_AMT5:float,
                 BILL_AMT6:float,
                 PAY_AMT1:float,
                 PAY_AMT2:float,
                 PAY_AMT3:float,
                 PAY_AMT4:float,
                 PAY_AMT5:float,
                 PAY_AMT6:float):
        
        self.LIMIT_BAL=LIMIT_BAL
        self.SEX=SEX
        self.EDUCATION=EDUCATION
        self.MARRIAGE=MARRIAGE
        self.AGE=AGE
        self.PAY_0=PAY_0
        self.PAY_2=PAY_2
        self.PAY_3=PAY_3
        self.PAY_4=PAY_4
        self.PAY_5=PAY_5
        self.PAY_6=PAY_6
        self.BILL_AMT1=BILL_AMT1
        self.BILL_AMT2=BILL_AMT2
        self.BILL_AMT3=BILL_AMT3
        self.BILL_AMT4=BILL_AMT4
        self.BILL_AMT5=BILL_AMT5
        self.BILL_AMT6=BILL_AMT6
        self.PAY_AMT1=PAY_AMT1
        self.PAY_AMT2=PAY_AMT2
        self.PAY_AMT3=PAY_AMT3
        self.PAY_AMT4=PAY_AMT4
        self.PAY_AMT5=PAY_AMT5
        self.PAY_AMT6=PAY_AMT6
            
                
    def get_data_as_dataframe(self):
            try:
                custom_data_input_dict = {
                    'LIMIT_BAL':[self.LIMIT_BAL],
                    'SEX':[self.SEX],
                    'EDUCATION':[self.EDUCATION],
                    'MARRIAGE':[self.MARRIAGE],
                    'AGE':[self.AGE],
                    'PAY_0':[self.PAY_0],
                    'PAY_2':[self.PAY_2],
                    'PAY_3':[self.PAY_3],
                    'PAY_4':[self.PAY_4],
                    'PAY_5':[self.PAY_5],
                    'PAY_6':[self.PAY_6],
                    'BILL_AMT1':[self.BILL_AMT1],
                    'BILL_AMT2':[self.BILL_AMT2],
                    'BILL_AMT3':[self.BILL_AMT3],
                    'BILL_AMT4':[self.BILL_AMT4],
                    'BILL_AMT5':[self.BILL_AMT5],
                    'BILL_AMT6':[self.BILL_AMT6],
                    'PAY_AMT1':[self.PAY_AMT1],
                    'PAY_AMT2':[self.PAY_AMT2],
                    'PAY_AMT3':[self.PAY_AMT3],
                    'PAY_AMT4':[self.PAY_AMT4],
                    'PAY_AMT5':[self.PAY_AMT5],
                    'PAY_AMT6':[self.PAY_AMT6]
                }    
                df = pd.DataFrame(custom_data_input_dict)
                logging.info('Dataframe Gathered')
                return df
            except Exception as e:
                logging.info('Exception Occured in prediction pipeline')
                raise customexception(e,sys)