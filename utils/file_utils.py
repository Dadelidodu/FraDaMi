# Importing pandas to extract data from xslx file

import pandas as pd
df = pd.read_excel('bouman_8_members.xlsx')
print(df["Names"])

list_names = (df["Names"]).tolist()
print(list_names)