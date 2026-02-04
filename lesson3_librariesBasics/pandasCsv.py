import pandas as pd

file = "/home/taya/PycharmProjects/financialFraud/final.csv"
df = pd.read_csv(file)
print(df.head())
df.dropna()
print(df.size)
dfFiltered = df.drop(df["amount"] > 1000)
