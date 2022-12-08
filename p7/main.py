# project: p7
# submitter: hbian8
# partner: none
# hours: 100

import pandas as pd
import geopandas as gpd 
import sqlite3
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import PolynomialFeatures, OneHotEncoder

class UserPredictor:
    def __init__(self):
        self.model = Pipeline([("poly", PolynomialFeatures(degree=1, include_bias=False)),("lr", LogisticRegression())])
        self.train = None
    
    def fit(self, train_users, train_logs, train_y):
        train = train_users.merge(train_y).merge(train_logs.groupby("user_id").sum().reset_index(), how="left")
        train['seconds'] = train['seconds'].fillna(0)
        self.train = train
        self.model.fit(self.train[["age","past_purchase_amt","seconds"]], self.train["y"])
        # scores = cross_val_score(self.model, train_users[self.xcols], train_y["y"])
        # print(f"AVG: {scores.mean()}, STD: {scores.std()}\n")

    def predict(self, test_users, test_logs):
        test = test_users.merge(test_logs.groupby("user_id").sum().reset_index(), how="left")
        test['seconds'] = test['seconds'].fillna(0)
        predict = self.model.predict(test[["age","past_purchase_amt","seconds"]])
        return predict

if __name__=="__main__":
    model = UserPredictor()
    train_users = pd.read_csv("data/train_users.csv")
    train_logs = pd.read_csv("data/train_logs.csv")
    train_y = pd.read_csv("data/train_y.csv")
    model.fit(train_users, train_logs, train_y)
    test_users = pd.read_csv("data/test1_users.csv")
    test_logs = pd.read_csv("data/test1_logs.csv")
    y_pred = model.predict(test_users, test_logs)
