# Random Forest Regression

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3] # Select the second column "Level" and the third column "Salary" only

# Splitting the data set into the Training set and Test set
#library(caTools)
#set.seed(123)
#split = sample.split(dataset$Profit, SplitRatio = 0.8)
#training_set = subset(dataset, split == TRUE)
#test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)


# Fitting the Random Forest Regression Model to the dataset
install.packages('randomForest')
library(randomForest)
set.seed(1234) # equals to random_state = 0
regressor = randomForest(x = dataset[1],
                         y = dataset$Salary,
                         ntree = 500)# dataset[1] will result in a dataframe, dataset$Salary will result in a vector

# Predicting a new result with Random Forest Regression
y_pred = predict(regressor, data.frame(Level = 6.5)) # make sure the 6.5 value showed in dataframe


# Visualizing the Random Forest Regression results (for higher resolution ans smoother curve)
# Non-linear and Non-continuous Regression Model
# install.packages('ggplot2')
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01) # from 1-10 incremented by 0.01

ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),#transform x_grid vector to a data frame
            color = 'blue') +
  ggtitle('Truth or Bluff (Random Forest Regression)') +
  xlab('Level') +
  ylab('Salary')