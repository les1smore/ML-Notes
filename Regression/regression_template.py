#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 21:18:10 2021

@author: leslie
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values # "Level" is our independent variable
"""Since we want our independent variable to be matrix all the time in machine learning,
   here we executed [:,1:2] instead of [:,1] as vector."""
y = dataset.iloc[:,2].values # "Salary" is our dependent variable

# Splitting the dataset into the Training set and Test set
"""from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""


# Fitting the Regression Model to the dataset
# Create your regressor here


# Predicting a new result
y_pred = regressor.predict(6.5)

# Visualising the Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue') 
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show() 


# Visualising the Regression results (for higher resolution and smoother curve)
import numpy as np
X_grid = np.arange(min(X), max(X), 0.1) # from level 1-10 (Position level), incremented by 0.1
X_grid = X_grid.reshape((len(X_grid)), 1)

plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue') # Here we don't use X_poly directly because we don't want to add another matrix
plt.title('Truth or Bluff (SVR Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show() 
