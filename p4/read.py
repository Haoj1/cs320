from cmath import nan
from numpy import NaN
import pandas as pd

df = pd.read_csv('main.csv')
age = {}
for i in range(len(df['age'])):
    # if df['obese'][i] >= 0:
    #     print(df['obese'][i])
    if df['age'][i] not in age:
        if df['obese'][i] >= 0:
            age[df['age'][i]] = df['obese'][i]
        else:
            age[df['age'][i]] = 0
    else:
        if df['obese'][i] >= 0:
            age[df['age'][i]] += df['obese'][i]
print(age)