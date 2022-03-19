 q# Import the dataset
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values # the first three variables as independent variables
y = dataset.iloc[:,3].values  # the last variable as dependent variable y

# Taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean', verbose = 0) # axis = 0 refers to columns
imputer = imputer.fit(X[:,1:3]) 
X[:,1:3] = imputer.transform(X[:, 1:3]) #replace the missing value in the two columns with mean of the whole column


# Encoding categorical data (Dunmmy Encoding method)
"""Dividing the three categories to 3 columns, and 1 respres yes, 0 represents no.
   First column - France, second column - Spain, third column - Germany"""
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])

onehotencoder = OneHotEncoder(categorical_features = [0]) # 0 refers to the categorical data is the first column
X = onehotencoder.fit_transform(X).toarray() 
 
"""Encoding the dependent variable"""
labelencoder_y = LabelEncoder() #0 refers to no, 1 refers to 1
y = labelencoder_y.fit_transform(y) # Since we've already specify the y metric, there's no need to use brackets


# Splitting the Dataset into the Training set and Test set
"""training set is for tools to do the machine learning, 
   while test set is for tools to predict based on the learning results from training set""" 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0) # 0.2 means 20% observations in the dataset will be chosen into the test set, and the left 80% is for the train set


# Feature Scaling - make all variables within the same scale
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train) # Only training set needs to use fit_transform()
X_test = sc_X.transform(X_test) # test set only needs transform()  
