#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:05:30 2021

@author: leslie
"""

# Importing the libraries
import numpy as py
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values

# Encoding categorical data
"""Encoding the independant variable"""
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,3] = labelencoder_X.fit_transform(X[:,3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray() 

"""Since the caregorical data <state> is one of the independant variables (x),
   we don't need to encode dependant variable (y) here"""

# Avoiding the Dummy Variable Trap
X = X[:,1:] # drop the fist columns representing "California" to avoid redundance
"""Since we have 3 categorical data in <state>, 
   we need to drop one column and keep the other two"""

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Building the optimal model using Backward Elimination 
import statsmodels.api as sm
import numpy as np
X = np.append(arr =np.ones((50,1)).astype(int), values = X, axis = 1)
X = X.drop[:,0]
"""Creating 50 x 1 columns as X-0 with the value 1, and make sure this column appears as the first column of X"""

"""Fit the full model with all possible predictors"""
X_opt = X[:,[0, 1, 2, 3, 4, 5]] # Including all independent variables for the dataset
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()

"""Consider the predictor with the highest P-value. If P > SL ( e.g. Sl = 0.05), then remove the predictor
   Otherwise, our model is ready"""
regressor_OLS.summary() # Execute this line to see the regression results

"""According to the summary results above, we're going to remove x2, which is index 2 in X matrix"""
X_opt = X[:,[0, 1, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

"""According to the summary results above, we're going to remove x1, which is index1 in X matrix"""
X_opt = X[:,[0, 3, 4, 5]] 
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() 
regressor_OLS.summary()

"""According to the summary results above, we're going to remove the index4 in matrix X"""
X_opt = X[:,[0, 3, 5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary() 

"""According to the summary results above, we're going to remove the index5 in matrix X"""
X_opt = X[:,[0, 3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary() 
