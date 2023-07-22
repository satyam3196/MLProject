import os
import sys
from dataclasses import dataclass
import numpy as np 

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            model = LinearRegression()
            model.fit(X_train, y_train)
            logging.info(f"Model trained on the dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=model
            )

            predicted=model.predict(X_test)
            predicted_rounded = np.round(predicted, 2)
            r2_square = r2_score(y_test, predicted_rounded)
            return r2_square
            
        except Exception as e:
            raise CustomException(e,sys)
