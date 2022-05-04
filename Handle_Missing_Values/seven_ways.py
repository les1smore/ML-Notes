# Impute missing values with Mean/Median:
data['Age'].replace(np.NaN, data['Age'].mean())

# Imputation method for categorical columns:
data['Cabin'] = data['Cabin'].fillna('U')

# LOCF method
data['Age'] = data['Age'].fillna(method='ffill')

# For time-series dataset variables, it makes sense to use the interpolation of the variable before and after a timestamp for a missing value
data['Age'] = data['Age'].interpolate(method='linear', limit_direction='forward', axis=0)

# Prediction of missing values
from sklearn.linear_model import LinearRegression
import pandas as pd

data = pd.read_csv("train.csv")
data = data[["Survived", "Pclass", "Sex", "SibSp", "Parch", "Fare", "Age"]]

data['Sex'] = [1 if x=='male' else 0 for x in data['Sex']]

test_data = data[data['Age'].isnull()]
data.dropna(inplace=True)

y_train = data['Age']
X_train = data.drop('Age',axis=1)
X_test = test_data.drop('Age'. axis=1)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

# Deep Learning Library - Datawig
"""This methods works very well with categorical, continuous, and non-numerical features.
   Datawig is a library that learns ML models using Deep Neural Networks to impute missing values in the datagram
"""

# Install datawig library
pip3 install datawig

import pandas as pd
pip install datawig
import datawig

data = pd.read_csv('train.csv')

df_train, df_test = datawig.utils.random_split(data)

# Initialize a SimpleImputer model
imputer = datawig.SimpleImputer(input_columns = ['Pclass', 'SibSp','Parch'],# columns containing information about the column we want to impute
                               output_columns = 'Age', # the columns we'd like to impute values for
                               output_path = 'imputer_model') # stores model data and metrics
                               
# Fit an imputer model on the training data
imputer.fit(train_df = df_train, num_epochs=50)

# Impute missing values and return original dataframe with predictions
imputed = imputer.predict(df_test)
                                                 
