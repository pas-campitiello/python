import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error

def trainAndReturnErrors(df, y_var):
	# Split our data into a training and test set. 
    X_train, X_test, y_train, y_test = train_test_split(df, y_var, test_size = 0.20, random_state = 0)

    # -------- Linear Regression -----------
    print("\n---Linear Regression")
    errors = []
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    errors.append(rmse)

    r_squared = r2_score(y_test, y_pred)
    errors.append(r_squared)

    mae = mean_absolute_error(y_test, y_pred)
    errors.append(mae)

    print("errors ", errors)

    # -------- Decision Tree -----------
    print("---Decision Tree")
    errors = []
    dt_regressor= DecisionTreeRegressor()
    dt_regressor.fit(X_train, y_train)
    y_pred = dt_regressor.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    errors.append(rmse)

    r_squared = r2_score(y_test, y_pred)
    errors.append(r_squared)

    mae = mean_absolute_error(y_test, y_pred)
    errors.append(mae)

    print("errors ", errors)

    # -------- Random Forest -----------
    print("---Random Forest")
    errors = []
    rf_regressor= RandomForestRegressor()
    rf_regressor.fit(X_train, y_train)
    y_pred = rf_regressor.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    errors.append(rmse)

    r_squared = r2_score(y_test, y_pred)
    errors.append(r_squared)

    mae = mean_absolute_error(y_test, y_pred)
    errors.append(mae)

    print("errors ", errors)

    return errors


# Read CSV and show some data
data = pd.read_csv('lifeData.csv')
df = pd.DataFrame(data)

print("\n---DATA")
print(df)
print("\n---INFO")
print(df.info())
print("\n--- DESCRIBE")
print(df.describe())
print("\n--- CORRELATION")
print(df.corr())

# Select features
df_1 = df[['D']]
df_2 = df[['D', 'SW']]
df_3 = df[['L', 'SE']]
df_4 = df[['D', 'SW', 'ST']]
df_5 = df[['L', 'SC', 'SE']]
y = df['SQ']

# Train and return errors
print("\n--- TRAIN AND RETURN ERRORS")
print("\n---df_1 - D")
trainAndReturnErrors(df_1, y)
print("\n---df_2 - D SW")
trainAndReturnErrors(df_2, y)
print("\n---df_3 - L SE")
trainAndReturnErrors(df_3, y)
print("\n---df_4 - D SW ST")
trainAndReturnErrors(df_4, y)
print("\n---df_5 - L SC SE")
trainAndReturnErrors(df_5, y)
