import pandas as pd
import numpy as np
df = pd.DataFrame({"name":['Alfred','Batman','Catwoman'],"toy":[np.nan, 'Batmobile', 'Bullwhip'], "born":[pd.NaT,pd.Timestamp("1940-04-25"),pd.NaT]})
print(df)
#Drop the rows where at least one element is missing
df_1 = df.dropna()
print("version 1")
print(df_1)
print(df)
# Drop the columns where at least one elenment is missing
df_2 = df.dropna(axis=1)
print("version 2")
print(df_2)
print(df)
# Drop the rows where all elements are missing
df_3 = df.dropna(how = 'all')
print("version 3")
print(df_3)
print(df)
# Keep only the rows with at least 2 non-NA values it nhat hai gia tri khong la null thi giu lai
df_4 = df.dropna(thresh = 2)
print("version 4")
print(df_4)
print(df)
# Define in which columns to look for missing values
df_5 = df.dropna(subset=['name', 'born'])
print("version 5")
print(df_5)
print(df)
# Keep the DataFrame with valid entries in the same variable. Lenh nay anh huong den DataFrame df
print("version 6")
df_6 = df.dropna(inplace= True)
print(df)