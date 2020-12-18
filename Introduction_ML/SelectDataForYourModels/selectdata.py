import pandas as pd
melbourne_file_path ='D:/2020/LearnMachineLearningData/2709_38454_bundle_archive/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
print(melbourne_data)
'''
To choose variables/columns, we'll need to see a list of all columns in the dataset. 
That is done with the columns property of the DataFrame (the bottom line of code below).
'''
print(melbourne_data.columns)
#Selecting The Prediction Target
y = melbourne_data.Price
print(y)
#Choosing "Features"
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
print(X)
print(X.head())
