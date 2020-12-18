#Building a Model
from sklearn.tree import DecisionTreeRegressor
import pandas as pd
melbourne_file_path='D:/2020/LearnMachineLearningData/2709_38454_bundle_archive/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_features=['Rooms','Bathroom','Landsize','Lattitude','Longtitude']
X = melbourne_data[melbourne_features]
y = melbourne_data.Price
# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=2)
# Fit model
melbourne_model.fit(X,y)
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))
from sklearn.metrics import mean_absolute_error
house_predictions = melbourne_model.predict(X)
print(mean_absolute_error(y,house_predictions))
from sklearn.model_selection import train_test_split
# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
train_X, var_X, train_y, var_y = train_test_split(X,y, random_state=0)
melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(train_X,train_y)
validation_predict = melbourne_model.predict(var_X)
print(mean_absolute_error(validation_predict,var_y))
