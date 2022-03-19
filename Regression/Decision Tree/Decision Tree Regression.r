# Decision Tree Regression

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


# Fitting the Regression Model to the dataset
# install.packages('rpart')
library(rpart)
regressor = rpart(formula = Salary ~ .,
                  data = dataset,
                  control = rpart.control(minsplit = 1)) # Adding the split intervals

# Predicting a new result with Decision Tree Regression
y_pred = predict(regressor, data.frame(Level = 6.5)) # make sure the 6.5 value showed in four levels 


# Visualizing the Decision Tree Regression results (for higher resolution ans smoother curve)
# Non-linear and Non-continuous Regression Model
# install.packages('ggplot2')
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01) # from 1-10 incremented by 0.01

ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),#transform x_grid vector to a data frame
            color = 'blue') +
  ggtitle('Truth or Bluff (Decision Tree Rgeression)') +
  xlab('Level') +
  ylab('Salary')