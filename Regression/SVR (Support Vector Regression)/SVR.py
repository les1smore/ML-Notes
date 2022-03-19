#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:17:33 2021

@author: leslie
"""

# SVR (Support Vector Regression)
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values # "Level" is our independent variable
"""Since we want our independent variable to be matrix all the time in machine learning,
   here we executed [:,1:2] instead of [:,1] as vector."""
y = dataset.iloc[:,2].values.reshape(-1,1) # "Salary" is our dependent variable

# Splitting the dataset into the Training set and Test set
"""from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)"""

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler() # creat two objects sc_X and sc_y from SatandardScaler that are going to scale our x and y
sc_y = StandardScaler()

X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)




# Fitting the SVR to the dataset
# Create your regressor here
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)



# Predicting a new result
import numpy as np
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]])))) # two brackets here is to create an array containing only one feature of 6.5
# inverse the scaled value of y into the original one using inverse_transform

# Visualising the SVR results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue') 
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show() 

# Visualising the SVR results (for higher resolution and smoother curve)
import numpy as np
X_grid = np.arange(min(X), max(X), 0.1) # from level 1-10 (Position level), incremented by 0.1
X_grid = X_grid.reshape((len(X_grid)), 1)

plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue') 
plt.title('Truth or Bluff (SVR Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show() 
