import pandas as pd
import numpy as np
df = pd.DataFrame({'a':[1,2]*3,'b':[True,False]*3,'c':[1.0,2.0]*3})
print(df)
df_1 = df.select_dtypes(include='bool')
print(df_1)
df_2 = df.select_dtypes(include = ['float64'])
print(df_2)
df_3 = df.select_dtypes(exclude=['int64'])
print(df_3)