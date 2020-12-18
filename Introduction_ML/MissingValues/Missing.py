import pandas as pd
from sklearn.model_selection import train_test_split
# Read the data
train_file_path = 'D:/2020/LearnMachineLearningData/MissingValues/train.csv'
test_file_path = 'D:/2020/LearnMachineLearningData/MissingValues/test.csv'
X_full = pd.read_csv(train_file_path, index_col='Id')
X_test_full = pd.read_csv(test_file_path, index_col='Id')
# Remove rows with missing target, separate target from predictions
X_full.dropna(axis=0, subset=['SalePrice'], inplace = True)
y = X_full.SalePrice
X_full.drop(['SalePrice'], axis=1, inplace = True)
# To keep things simple, we'll use only numerical predictions
X = X_full.select_dtypes(exclude=['object'])
X_test = X_test_full.select_dtypes(exclude=['object'])
# Breaking off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8,test_size=0.2,random_state=0)
print(X_train.head())
# Shape of training data (num_rows, num_columns)
print(X_train.shape)
# Number of missing values in each column of training data
missing_val_count_by_column = (X_train.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
# Function for comparing different approaches
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators= 100, random_state=0)
    model.fit(X_train,y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)
# Get the name of columns with missing values
cols_with_missing = [col for col in X_train.columns if X_train[col].isnull().any()]
# Drop columns in training and validation data
reduced_X_train = X_train.drop(cols_with_missing, axis = 1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis = 1)
print("MAE (Drop columns with missing values):")
print(score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))
from sklearn.impute import SimpleImputer
my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))
print("MAE (Imputation):")
print(score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid))
final_X_train = reduced_X_train
final_X_valid = reduced_X_valid
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(final_X_train, y_train)
preds_valid = model.predict(final_X_valid)
print("MAE (Your approach):")
print(mean_absolute_error(y_valid, preds_valid))
