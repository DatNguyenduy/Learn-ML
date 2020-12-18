import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
melbourne_file_path = 'D:/2020/LearnMachineLearningData/2709_38454_bundle_archive/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
y = melbourne_data.Price
melbourne_feathers=['Rooms','Bathroom','Landsize','Lattitude','Longtitude']
X = melbourne_data[melbourne_feathers]
train_X, var_X, train_y,var_y = train_test_split(X,y,random_state=0)
def get_mae(max_leaf_nodes,train_X,train_y,var_X,var_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes,random_state=0)
    model.fit(train_X,train_y)
    val_predict = model.predict(var_X)
    mae = mean_absolute_error(val_predict,var_y)
    return mae
for max_leaf_node in [5,10, 50 ,100 , 500,1000, 5000]:
    my_mae = get_mae(max_leaf_node,train_X,train_y,var_X,var_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" % (max_leaf_node, my_mae))
result = { max_leaf_node : get_mae(max_leaf_node,train_X,train_y,var_X,var_y) for
           max_leaf_node in [5, 10, 50 ,100 , 500,1000, 5000]}
best_tree_size = min(result,key=result.get)
print(best_tree_size)
