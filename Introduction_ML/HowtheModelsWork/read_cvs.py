# read file csv by pandas
import pandas as pd
file_path = '../folder_name/data.csv'
data = pd.read_csv(file_path)
# describe the data in the variable data on the screen
print(data.describe())
train_data_path = 'D:/2020/LearnMachineLearningData/train.csv'
train_data = pd.read_csv(train_data_path)
print("length of the train_data" , len(train_data))
print(train_data.keys())
print(train_data['LotArea'].sum()/len(train_data))
a=(train_data['YrSold']).max()
print('Most recently year sold', a)
