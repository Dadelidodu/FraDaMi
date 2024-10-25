# Importing pandas to extract data from xslx file

import pandas as pd
df = pd.read_excel('../FraDaMi/utils/bouman_8_members.xlsx')
print(df["Names"])

name_list = (df["Names"]).tolist()
print(name_list)