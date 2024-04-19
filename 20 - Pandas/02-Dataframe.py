import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.DataFrame(data=randn(3,3), index=["A","B","C"], columns=["Column1","Column2","Column3"])

# print(df)
# Çıktı: Random veriler
#     Column1   Column2   Column3
# A -1.321287 -0.741208 -2.275920
# B -1.500490 -0.162819  0.679766
# C  1.079289  0.848171 -0.671818

# print(df["Column1"])
# Çıktı:
# A -1.321287
# B -1.500490
# C  1.079289
# Name: Column1, dtype: float64

# print(type(df["Column1"])) # Çıktı: <class 'pandas.core.series.Series'>

# print(df.loc["A"])
# Çıktı:
# Column1 -1.321287 
# Column2 -0.741208 
# Column3 -2.275920
# Name: A, dtype: float64

# df["Column4"] = pd.Series(data=randn(3), index = ["A","B","C"])
# print(df) # Yeni sütun ekler

# df["total"] = df["Column1"] + df["Column2"] + df["Column3"]
# print(df) # Sütunları toplar ve toplamından yeni sütun oluşturur
# df.drop("total",axis = 1,inplace=True) # inplace -> Dataframe günceller ve değişiklikler yansır.
# print(df) # total sütununu siler

# print(df.iloc[0]) # indekse göre alır.

# print(df.loc[["A","B"],["Column1","Column2"]]) # A, B ve Column1, Column2 alır