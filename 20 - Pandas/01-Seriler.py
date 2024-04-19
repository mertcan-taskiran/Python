# Pandas, Python programlama dili için geliştirilmiş, veri analizi ve manipülasyonu için kullanılan açık kaynaklı bir kütüphanedir. 
# Pandas, veri işleme ve analizinde yaygın olarak kullanılan veri yapılarını ve araçlarını sağlar.

import numpy as np
import pandas as pd

# labels_list = ["Mertcan","Mert","Can","Taş"]
# data_list = [10,20,30,40]
# series = pd.Series(data_list, labels_list)
# print(series)
# Çıktı:
# Mertcan    10
# Mert       20
# Can        30
# Taş        40
# dtype: int64

# npArray = np.array([10,20,30,40,50])
# series = pd.Series(npArray)
# print(series)
# Çıktı:
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int32

# dataDict = {"Mert":100,"Can":200} 
# series = pd.Series(dataDict)
# print(series)
# Çıktı:
# Mert    100
# Can     200
# dtype: int64

# p1 = pd.Series([1,2,4,8], ["bir", "iki", "dört", "sekiz"])
# p2 = pd.Series([1,2,5,9], ["bir", "iki", "beş", "dokuz"])

# print(p1+p2)
# Çıktı: 
# beş      NaN
# bir      2.0
# dokuz    NaN
# dört     NaN
# iki      4.0
# sekiz    NaN
# dtype: float64

# total = p1+p2
# print(total["iki"]) # Çıktı: 4.0