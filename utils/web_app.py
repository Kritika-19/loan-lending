import pickle
import os
import numpy as np
from utils.feature_engg import preprocess, preprocess_and_standardize

# Load the model
MODEL_NAME = "naive_bayes"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", MODEL_NAME+".pkl")
MODEL = pickle.load(open(MODEL_PATH, "rb"))

def predict_defaulter_or_payer(loan_amnt, int_rate, installment, issue_d, grade, sub_grade, 
                                purpose, debt_settlement_flag, earliest_cr_line,
                                home_ownership, fico_range_low, fico_range_high, dti):
        features = [loan_amnt, int_rate, installment, issue_d, purpose, 
                    debt_settlement_flag, earliest_cr_line, home_ownership,
                    fico_range_low, fico_range_high, dti, grade, sub_grade]
        if "naive_bayes" in MODEL_NAME:
            # Preprocess the data
            data = preprocess(features)
            data = [[float(x) for x in data]]
        else:
            # Preprocess and standardize the data
            data = preprocess_and_standardize(features)
            data = [[float(x) for x in data]]
        # Predict the data
        prediction = MODEL.predict(data)[0]
        # Process it to Defaulter/Payer
        prediction = "Defaulter" if prediction == 1 else "Payer"

        return prediction