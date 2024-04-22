import pandas as pd

# CSV Okuma
dataset = pd.read_csv("dataset.csv")
print(dataset)

# Excel Okuma
excelset = pd.read_excel("excelfile.xlsx")
print(excelset)

# Html Okuma
new = pd.read_html("web_adresi",header = 0)
print(new[0])