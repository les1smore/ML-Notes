#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 20:08:43 2021

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

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X) # Adding additional polynomial matrix of x

lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly, y)

# Visualising the Linear Regression results 
plt.scatter(X, y, color = 'red') #Real observation"""
plt.plot(X, lin_reg.predict(X), color = 'blue') #Prediction
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show() 

# Visualising the Polynomial Regression results
import numpy as np
X_grid = np.arange(min(X), max(X), 0.1) # from level 1-10 (Position level), incremented by 0.1
X_grid = X_grid.reshape((len(X_grid)), 1)

plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_reg2.predict(poly_reg.fit_transform(X_grid)), color = 'blue') # Here we don't use X_poly directly because we don't want to add another matrix
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show() 

# Predicting a new result with Linear Regression 
lin_reg.predict(6.5)

# Predicting a new result with Polynomial Regression
lin_reg2.predict(poly_reg.fit_transform(6.5))
