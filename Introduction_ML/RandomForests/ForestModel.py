import pandas as pd
melb_file_path = 'D:/2020/LearnMachineLearningData/2709_38454_bundle_archive/melb_data.csv'
melb_data = pd.read_csv(melb_file_path)
from sklearn.ensemble import RandomForestRegressor
forest_model = RandomForestRegressor(random_state=1)
data_feathers=['Rooms','Bathroom','Landsize','Lattitude','Longtitude']
X = melb_data[data_feathers]
y = melb_data.Price
from sklearn.model_selection import train_test_split
train_X, var_X, train_y, var_y = train_test_split(X,y, random_state=0)
forest_model.fit(train_X,train_y)
value_predict = forest_model.predict(var_X)
from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(value_predict,var_y))
