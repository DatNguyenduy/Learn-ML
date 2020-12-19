import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(12).reshape(3,4),columns = ['A','B','C','D'])
print(df)
# Drop columns
df_1 = df.drop(['B','C'], axis=1)
df_2 = df.drop(columns=['B','C'])
print(df_1)
print(df_2)
# Drop a row by index
df_3 = df.drop([0,1])
print(df_3)
# Drop columns and/ or rows of MultiIdex DataFrame
midx = pd.MultiIndex(levels=[['lama','cow','falcon'],['speed','weight','length']],codes=[[0,0,0,1,1,1,2,2,2],[0,1,2,0,1,2,0,1,2]])
dfm = pd.DataFrame(index=midx, columns = ['big','small'],data=[[45,30],[200,100],[1.5,1],[30,20],[250,150],[1.5,0.5],[320,250],[1,0.8],[0.3,0.2]])
print("dataframe_new")
print(dfm)
dfm_1 = dfm.drop(index='cow',columns='small')
print("drop columns and rows")
print(dfm_1)
dfm_2 = dfm.drop(index='length',level=1)
print(dfm_2)