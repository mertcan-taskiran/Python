import numpy as np
import pandas as pd

dataset = {
    "Departman":["Bilişim","İnsan Kaynakları","Üretim","Üretim","Bilişim","İnsan Kaynakları"],
    "Çalışan": ["Personel1","Personel2","Personel3","Personel4","Personel5","Personel6"],
    "Maaş":[30000,35000,25000,45000,40000,20000]
}

df = pd.DataFrame(dataset)

# print(df)

DepGroup = df.groupby("Departman")

print(DepGroup.sum()) # Departman maaş toplamları

print(DepGroup.count()) # Çalışan sayısı

print(DepGroup.max()) # max maaş
print(DepGroup.min()) # min maaş