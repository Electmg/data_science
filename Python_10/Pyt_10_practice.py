import pandas as pd

melb_data = pd.read_csv("C:\Курс DS-3.0\IDE\Python_10\data\melb_data.csv", sep=",")
print(melb_data.loc[15])