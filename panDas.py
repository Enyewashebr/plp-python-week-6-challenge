import pandas as pd
import numpy as np
# This file is part of the PLP Python Week 6 Challenge
# It contains the pandas library import and a sample DataFrame creation
# data={
#     "Name":["Enyew", "Allexiander", "Alemayehu", "Abebe"],
#     "Age":[25, 30, 22, 28],
#     "City":["Addis Ababa", "Dire Dawa", "Mekelle", "Bahir Dar"]
# } 
# dataframe = pd.DataFrame(data)
# print(dataframe)
# series=pd.Series(dataframe["Nmae"])
# print(series)

data={
    "Name":["Enyew", "Allexiander", "Alemayehu"],
    "Age":[25, 30, 22],
    "grade":[67,90,45]
    # "is_passed":[True, Fa, True]
}
df=pd.DataFrame(data)
df["is_passed"]=np.where(df["grade"]>=50, "Passed", "Failed")
print(df)
