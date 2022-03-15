#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 22:54:15 2021

@author: leslie
"""

# Simple Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values # the independent variable is "salary" - x (matrix)
y = dataset.iloc[:,1].values # the dependent variable is "year of experience" - y(vector) 

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
""" 1/3 means 10% observation would be divided to Test set and 20% would be divided to Training set  """

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

# Fitting Simple Linear Regression to the Trainig set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train) # fit a linear model between x_train and y_train

# Predicting the Test set results￼
y_pred = regressor.predict(X_test) 

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue') # y is the prediction of training set
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary') 
plt.show() 

# Visualising the Test set result
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show() 
