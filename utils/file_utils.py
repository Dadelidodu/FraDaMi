# Importing pandas to extract data from xslx file

import pandas as pd
df = pd.read_excel('../FraDaMi/utils/bouman_8_members.xlsx')

name_list = (df["Names"]).tolist()
