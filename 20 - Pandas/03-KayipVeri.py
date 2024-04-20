import numpy as np
import pandas as pd

arr = np.array([[10,20,np.nan],[5,np.nan,np.nan],[25,np.nan,10]])
df = pd.DataFrame(arr,index=["Index1","Index2","Index3"],columns = ["Column1","Column2","Column3"])
# print(df)

# print(df.dropna(axis=1)) # Nan olan sütunlar silinir.

# print(df.dropna(thresh=2)) # Minimum 2 Nan olmayan varsa silme.

# print(df.fillna(value = 10)) # Nan değerleri 10 yapar.

# print(df.sum()) # Tüm satırların ortalamasını alır.

# print(df.sum().sum()) # Tüm df ortalaması.

# print(df.size()) # df toplam eleman sayısı

# print(df.isnull().sum().sum()) # Toplam NaN sayısı

def calculateMean(df):
    totalSum = df.sum().sum()
    totalNum = df.size - df.isnull().sum().sum()
    return totalSum / totalNum

df = df.fillna(value = calculateMean(df))
print(df)