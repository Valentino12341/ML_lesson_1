# LINEAR REGRESSION USING CSV FILE

# m = sum((xi-mean(x)) * (yi-mean(y))) / sum((xi-mean(x))^2)
# c = mean(y) - m * mean(x)

import pandas as pd

data = pd.read_csv("xy.csv")

x = data["X"].tolist()
y = data["Y"].tolist()

import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array(x).reshape(-1,1)
y = np.array(y).reshape(-1,1)

model = LinearRegression()
model = model.fit(x,y)

print("finding m and c through machine learning algorithm")

print("m =",model.coef_)
print("c =",model.intercept_)
