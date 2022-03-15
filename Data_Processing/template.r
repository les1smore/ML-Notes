# Importing the dataset
# Click on the dataset you want to import at the right below pattern and clcick "more" - "Set as working directory"
dataset = read.csv('Data.csv')

# Taking care of missing data 
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age,FUN = function(x) mean(x, na.rm = TRUE)), # if there's NaN in the column, remove it and replace it with average value of all columns
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)
# Encoding categorical data
dataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))
dataset$Purchased = factor(dataset$Purchased,
                           levels = c('No', 'Yes'),
                           labels = c(0, 1))

# Splitting the dataset into the Training set and Test set
  # install.packages('caTools') 
  # library(caTools)
set.seed(123) # we can choose a random number and make a split
split = sample.split(dataset$Purchased, SplitRatio = 0.8) #0.8 is the 80% observation put in the training set
training_set = subset(dataset, split == TRUE) # split == True if the observation is going to the training set
test_set = subset(dataset, split == FALSE) # split == False if the observation is going to the test set

# Feature Scaling
training_set[,2:3] = scale(training_set[,2:3]) # since our first and last column are categorical variables, we can't scale the x_train or x_test directly 
  # Therefore, we would only scale the second and third column, which are "Age" and "Salary", index starts at 2 and ends at 3.
test_set[,2:3] = scale(test_set[,2:3])