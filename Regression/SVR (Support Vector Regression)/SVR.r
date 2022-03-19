# SVR
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


# Fitting the SVR Model to the dataset
install.packages('e1071')
library(e1071)
regressor = svm(formula = Salary ~. ,
                data = dataset,
                type = 'eps-regression')

# Predicting a new result with Polynomial Regression
y_pred = predict(regressor, data.frame(Level = 6.5)) 

# Visualizing the SVR results
library(ggplot2)
ggplot() + 
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
                      color = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
            color = 'blue') +
  ggtitle('Truth or Bluff (SVR)') +
  xlab('Level') +
  ylab('Salary')


# Visualizing the Polynomial Regression results (for higher resolution ans smoother curve)
# install.packages('ggplot2')
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1) # from 1-10 incremented by 0.1

ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),#transform x_grid vector to a data frame
            color = 'blue') +
  ggtitle('Truth or Bluff (Rgeression Model)') +
  xlab('Level') +
  ylab('Salary')