import pandas as pd
import numpy as np
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTEFACTS_PATH = os.path.join(BASE_DIR, "data", "artefacts")

def preprocess(features):
    
    # Preprocess date colums(issue_d, earliest_cr_line)
    min_issue_d = pd.to_datetime("2007-06-01")
    features[3] = (features[3] - min_issue_d) / (np.timedelta64(1, 'D') * 30)
    min_earliest_cr_line = pd.to_datetime("1933-03-01")
    features[6] = (features[6] - min_earliest_cr_line) / (np.timedelta64(1, 'D') * 30)

    # Preprocess grade/sub-grade
    ## Collect grade and sub-grade
    grade_val = features[-2]
    subgrade_num = int(features[-1][1])
    features = features[:-2]

    ## Create dummy variables for grade/sub-grade
    grade_dummies = [0 for _ in range(7)]
    grade_dummies[ord(grade_val) - ord('A')] = subgrade_num
    features = np.concatenate((features, grade_dummies), axis=0)

    # Preprocess categorical variables
    ## Read dictionary json from artifact
    cat_cols = ['home_ownership', 'debt_settlement_flag', 'purpose']
    label_encoders = []

    for col in cat_cols:
        with open(ARTEFACTS_PATH + f'/{col}_dictionary.json', 'r') as f:
            label_encoders.append(json.load(f))
    ## Encode categorical variables
    features[7] = label_encoders[0][features[7]]
    features[5] = label_encoders[1][features[5]]
    features[4] = label_encoders[2][features[4]]
    
    return features

# TODO: Add one-hot encoding featres, standardization
def preprocess_and_standardize(features):

    return []