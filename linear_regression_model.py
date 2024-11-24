import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import joblib

# import dataset
df = pd.read_excel("data/data.xlsx")
# print(df)

# Independent, dependent features
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# creating the train set and data set
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=42)

# Building and training the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Inference
y_pred = model.predict(X_test)
print(y_pred)

# making the prediction a single data point with AT = 15, V = 40, AP
print(model.predict([[15, 40, 1000, 75]]))








