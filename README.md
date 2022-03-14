# mlnotes
Machine Learning Notes

## PCA 
- A dimensionality reduction technique (Feature Extration) for data sets with many features or dimentsions. It uses linear algebra to determine the most important features of a dataset. After these features have been identified, you can use only the most important features or those that explain the most variance, to train a machine learning model and improve the computational performance of the model without sacrificing accuracy.
- Each of the "new" variables after PCA are all independent of one another, this is a benefit because the assumptions of a linear model requre our independent variables to be independent of one another. 

- When should I use PCA?
1. Do you want to reduce the number of variables, but aren't able to identify variables to completely remove from consideration?
2. Do you want to ensure your variables are independent of one another?
3. Are you comfortable making your independent variables less interpretable?
   If you answered “yes” to all three questions, then PCA is a good method to use. 
   If you answered “no” to question 3, you should not use PCA.

- PCA is a method that bring together:
1. A measure of how each variable is associated with one another. (Covariance matrix)
2. The directions in which our data are dispersed.(Eigenvectors)
3. The relative importance of these different directions. (Eigenvalues)

Two criteria:
- The maximum vriance
- The minimum error

## Dimension Reduction
- Feature elimination: We reduce the feature space by eliminating features. Advantages of feature elimination methods include simplicity and maintaining interpretability of your variables. Disadvantages include no information from those variables that are dropped.
- Feature extration: We create new independent variable which is a combination of each of the old independent variables by how well they predict our dependent variable.

Reference: 
1. https://medium.com/towards-data-science/principal-component-analysis-pca-explained-visually-with-zero-math-1cbf392b9e7d
2. https://towardsdatascience.com/2-beautiful-ways-to-visualize-pca-43d737e48ff7
3. https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues/140579
4. https://towardsdatascience.com/2-beautiful-ways-to-visualize-pca-43d737e48ff7
5. https://towardsdatascience.com/a-one-stop-shop-for-principal-component-analysis-5582fb7e0a9c

## Decision Tree
The algorithm works based on the decision on the conditions of the features. Nodes are the conditions or tests on an attribute, branch represents the outcome of the tests, and lead nodes are the decisions based on the conditions.

- Advantages
1. Clear visualization of how the predicition happens and thus it's easier to explain to the stakeholders or customers.
2. No feature scaling is required.
3. The non-linearity relationship between the dependent and independent variables does not affect the performance of the decision tree algorithms.
4. Handle outliers automatically.
5. Handle missing values automatically.

- Disadvantages
1. A major risk of overfitting. This can also cause high variance which may lead to many errors in the prediction.
2. Be unstable easily. A little bit of noise in the data or adding one extra piece of data may make the whole tree unstable or may build the tree all over again.
3. Not suitable for large dataset. If the dataset is too large, the algorithm may become too complex and may lead to an overfitting issue.

Reference: https://towardsdatascience.com/simple-explanation-on-how-decision-tree-algorithm-makes-decisions-34f56be344e9

## Poisson Regression Model
We already know about the Linear Regression, which helps us answer questions like “How much will a house with these characteristics cost?”. Or the Logistic Regression, which is used to model the probability of a certain class or event existing such as pass/fail, win/lose, alive/dead or healthy/sick.
But, what happens when the questions are “How many costumers will come today?”, “How many people are in line at the grocery store?”, “How many…”, and one way to answer these questions is using the Poisson Regression Model.

Poisson Regression is used to model count data. For this, we assume the response variable Y has a *Poisson Distribution*, and assumes the logarithm of its expected value can be modeled by a linear combinations of unknown parameters.
The expected value (mean) for a Poisson distribution is λ. Thus in the absence of other information, one should expect to see λ events in any unit time interval such as 1 hour, 1 day, etc. For any interval t, one would expect to see λt events.

- Count based data
Count based data contains events that occur at a certain rate. The rate of occurrence may change over time or from one observation to next. Here are some examples of count based data. 
  - Number of vehicles crossing an intersection per hour
  - Number of people visiting a doctor's office per month
  - Number of earth-like planets spotted per month

A data set of counts has the following characteristics:
  - **Whole number data**: The data consists of *non-negative* integers. Regression techniques such as Ordinary Least Squares Regression may not be appropriate for modeling such data as OLSR works best on real numbers such as -656.0, -0.0000000345,etc.
  - **Skewed Distribution**: The data may contain a large number of data points for just a few values, therefore making the frequency distribution quite skewed.
  - **Sparsity**: The data may reflect the occurrence of a rare event of a rare event such as a gamma ray burst, thereby making the data sparse.
  - **Rate of occurrence**: For the sake of creating a model, it can be assumed that there is a certain rate of occurrence of events λ that drives the generation of such data. The event rate may drift over time.

Refrence: 
1. https://towardsdatascience.com/an-illustrated-guide-to-the-poisson-regression-model-50cccba15958
2. https://medium.com/lcc-unison/how-to-poisson-regression-model-python-implementation-1c672582eb96
