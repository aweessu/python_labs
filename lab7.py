
import numpy as np
import pandas as pd

#1
sentinels = [None, np.nan, pd.NA, pd.NaT]
for x in sentinels:
    print(x, pd.isna(x))

#2
values = {"NA": pd.NA, "NaN": np.nan, "NULL (SQL)": None, "None": None}
for name, value in values.items():
    print(name, value, pd.isna(value))

#3
data = np.random.standard_normal((10, 6))
print(data)

#4
df = pd.DataFrame(data)
print(df)

#5
df.iloc[:5, 1] = np.nan
df.iloc[-3:, 2] = np.nan
df.iloc[:2, 4] = np.nan
print(df)

#6
print(df.dropna().dropna(axis=1))
print(df.dropna(axis=0))
print(df.dropna(axis=1))

#7
print(df.dropna(how="any"))
print(df.dropna(how="all"))
print(df.dropna(axis=1, how="any"))
print(df.dropna(thresh=5))

#8
print(df.fillna(0))
print(df.fillna({1: 100, 2: 200, 4: 300}))
print(df.fillna(df.mean()))
print(df.ffill(limit=2))

#9
print(df.fillna(value=0, axis=0))
print(df.ffill(axis=0, limit=2))
print(df.ffill(axis=1, limit=2))
print(df.bfill(axis=0, limit=2))
