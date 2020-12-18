# read file csv by pandas
import pandas as pd
file_path = '../folder_name/data.csv'
data = pd.read_csv(file_path)
# describe the data in the variable data on the screen
print(data.describe())
