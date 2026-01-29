import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
from config import MODEL_PARAMS

def train_churn_model(rfm_df):

    X = rfm_df[['Frequency','Monetary','IPT']].apply(np.log1p)
    y = rfm_df['Churn']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    smote = SMOTE(random_state=42)
    X_res, y_res = smote.fit_resample(X_train, y_train)

    model = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', XGBClassifier(**MODEL_PARAMS, random_state=42))
    ])

    model.fit(X_res, y_res)

    return model
