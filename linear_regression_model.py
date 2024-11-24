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

# R squared
r2 = r2_score(y_test, y_pred)

# Adjusted R-Sqaured
k = X_test.shape[1]
n = X_test.shape[0]

adj_r2 = 1-(1-r2)*(n-1)/(n-k-1)

# Scattered Plot of Actual vs. Predicted Values
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, alpha=0.5) # plot actual vs. predicted
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)],color='red',linewidth='2')
plt.xlabel('actual value')
plt.ylabel('predicted value')
plt.title('Actual vs Predicted Values')
plt.show()

#  save the train model to a .pkl file
joblib.dump(model, "model/model.pkl")










