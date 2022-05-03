# mlnotes
Machine Learning Notes

## Overfitting vs. Underfitting
- When the Machine Learning model performs well on the training data with a low error rate (e.g. low training MSE) but when applied on the test data it results in a higher error rate (e.g. high test MSE) we can this overfitting. Overfitting occurs when the ML model follows the training data too closely and takes into account the noise in the data.
- When the opposite is ture, that is the ML model fails to follow the data closely and to accurately capture relationships between a dataset's features and a target variable, we call it underfitting.

![image](https://user-images.githubusercontent.com/60702562/161606098-fbc9b3e4-6359-4a6a-87f3-422b341e1d69.png)

- To solve overfitting problem we have two options:
  1. Choose another model that is less flexible (e.g. models that are known for being less flexible have higher bias but lower variance)
  2. Adjust the model to make it less flexiblee (Regularization)

## Irreducible Error
The accuracy of yˆ as a prediction for y depends on two quantities, which we can call the reducible error and the irreducible error. In general, fˆ will not be a perfect estimate for f, and this inaccuracy will introduce some errors. This error is reducible since we can potentially improve the accuracy of fˆ by using the most appropriate Machine Learning model to estimate f. However, even if it was possible to find a model that would estimate f perfectly so that the estimated response took the form yˆ = f(x), our prediction would still have some amount of error in it. This happens because y is also a function of the error term ε, which, by definition, cannot be predicted using predictor x.
![image](https://user-images.githubusercontent.com/60702562/161607752-6db58271-14c3-4163-a65d-6e0c4bc231d8.png)

Therefore, variability associated with error ε also affects the accuracy of the predictions. This is known as the irreducible error because no matter how well we estimate f, we cannot reduce the error introduced by ε. Hence, irreducible error in the model is the variance of the error terms ε and can be expressed as follows:
![image](https://user-images.githubusercontent.com/60702562/161607822-57f12935-e3e7-44f5-ba65-264ee3ed3141.png)

Unlike reducible error, irreducible error is an error that we cannot avoid nor reduce by choosing a better model which arises due to randomness or natural variability in a system.

## Bias
The inability of the model to capture the true relationship in the data is called bias. Hence, the ML models that are able to detect the true relationship in the data, have low bias. Usually, complex models or more flexible models tend to have a lower bias than simpler models. Mathematically, the bias of the model can be expressed as follows:
![image](https://user-images.githubusercontent.com/60702562/161608186-e51462c5-4a0a-4368-b029-2f6a0a91aff2.png)

## Variance
The variance of the model is the inconstancy level of model performance when applying the model to different data sets. When the same model that is trained using training data performs entirely differently than on test data this means there is a large variance in the model. Complex models or more flexible models tend to have higher variance than simpler models.
![image](https://user-images.githubusercontent.com/60702562/161608566-df7a5a30-7cf8-437b-899b-9cf4d65d7f28.png)

## Bias-Variance Trade-off
It can be mathematically proven that the expected test error rate of the Machine Learning model, for a given value x0, can be described in terms of the Variance of the model, the Bias of the model, and the irreducible error of the model. More specifically, **the error in the supervised Machine Learning model is equal to the sum of the Variance of the model, squared Bias, and the irreducible error of the model.**
![image](https://user-images.githubusercontent.com/60702562/161608702-e86e80f7-2de2-4753-a4ed-813f0de8c174.png)

Complex models or more flexible models tend to have a lower bias but at the same time, these models tend to have higher variance than simpler models.

![image](https://user-images.githubusercontent.com/60702562/161609226-7845f2c2-8846-4144-9eff-9a39ed49495d.png)

Based on the Bias and Variance relationship a Machine Learning model can have 4 possible scenarios:
1. High Bias and High Variance (The Worst-Case Scenario)
2. Low Bias and Low Variance (The Best-Case Scenario)
3. Low Bias and High Variance (Overfitting)
4. High Bias and Low Variance (Underfitting)

## Regularization (Shrinkage) - Solve Overfitting
The idea behind the regularization is to introduce a little bias in the ML model while significantly decreasing the variance. 

The reason why it's called Shrinkage is that this method shrinks some of the estimated coefficients towards zero, so to penalize them for increasing the variance of the model.

The two most popular regularization techniques are the Ridge Regression based on L2 norm and Lasso Regression based on L2 norm.

### Ridge Regression
Let’s look at multiple linear regression examples with p independent variables or predictors that are used to model the dependent variable y. You might also recall that the most popular estimation technique to estimate the parameters of linear regression, assuming its assumptions are satisfied is the **Ordinary Least Squares (OLS)** which finds the optimal coefficients by minimizing the residual sum of squares (RSS) of the model:

![image](https://user-images.githubusercontent.com/60702562/161611129-392ef196-43a8-43d8-872a-6d28e33106b8.png)

where the β represents the coefficient estimates for different variables or predictors(X).

Ridge Regression is pretty similar to OLS, except that the coefficients are estimated by minimizing a slightly different cost or loss function. Namely, the Ridge Regression coefficient estimates βˆR values such that they minimize the following loss function:

![image](https://user-images.githubusercontent.com/60702562/161611238-eaf5ebb3-73f4-4f4c-a41a-b8a9ec469ca4.png)

where λ (lambda, which is always positive, ≥ 0) is the tuning parameter or the penalty parameter, and as can be seen from this formula, in the case of the Ridge, **the L2 penalty or L2 norm is used**. In this way, Ridge Regression will assign a penalty to some variables shrinking their coefficients towards zero, reducing the overall model variance, but these coefficients will never become exactly zero. So, the model parameters are never set to exactly 0, which means that all p predictors of the model are still intact.

**L2 Norm (Euclidean Distance)**
L2 norm is a mathematical term coming from Linear Algebra and it’s standing for a Euclidean norm which can be represented as follows:

![image](https://user-images.githubusercontent.com/60702562/161611524-6698f1b9-fe92-467a-a331-dcdc21cc743e.png)

**Tuning parameter λ**
The tuning parameter λ serves to control the relative impact of the penalty on the regression coefficient estimates. When λ = 0, the penalty term has no effect, and the ridge regression will produce the ordinary least squares estimates. However, as λ → ∞ (gets very large), the impact of the shrinkage penalty grows, and the ridge regression coefficient estimates approach to 0.
![image](https://user-images.githubusercontent.com/60702562/161611686-8d4ce53e-34fc-4cc2-86fd-e59ecc9af866.png)

**Why does Ridge Regression work?**
Ridge regression’s advantage over ordinary least squares is coming from the earlier introduced bias-variance trade-off phenomenon. 
As λ, the penalty parameter, increases, the flexibility of the ridge regression fit decreases, leading to decreased variance but increased bias.

Note: Ridge Regression will assign a penalty (λ) to some variables shrinking their coefficients towards zero but they will never become exactly zero.

**Pros**
- Solves overfitting
- Easy to understand

**Cons**
- low model interpretability if p is large


### LASSO Regression
One of the biggest disadvantages of Ridge Regression is that it will include all p predictors in the final model. Therefore, large lambda will assign a penalty to some variables shrinking their coefficients towards zero but they will never become exactly zero which becomes a problem when your model has a large number of features and your model has low interpretability.

Lasso Regression overcomes this disadvantage of Ridge Regression. Namely, the Lasso Regression coefficient estimates βˆλL are the values that minimize:
![image](https://user-images.githubusercontent.com/60702562/161612344-88f90108-be1b-4b72-bae1-1fe03b8a7f4b.png)

As with Ridge Regression, the Lasso shrinks the coefficient estimates towards zero. However, in the case of the Lasso, the L1 penalty or L1 norm is used which has the effect of forcing some of the coefficient estimates to be exactly equal to zero when the tuning parameter λ is significantly large. Hence, like many feature selection techniques, Lasso Regression performs **variable selection** besides solving the overfitting problem.

![image](https://user-images.githubusercontent.com/60702562/161612648-168b5804-a287-4f17-b281-b3622786da4b.png)

**L1 Norm (Manhattan Distance)**

![image](https://user-images.githubusercontent.com/60702562/161612735-192bb199-e44d-4333-8166-9f8ea15198bd.png)

**Why does Lasso Regression Work?**
Like, Ridge Regression, Lasso Regression’s advantage over ordinary least squares is coming from the earlier introduced bias-variance trade-off. As λ increases, the flexibility of the ridge regression fit decreases, leading to decreased variance but increased bias. Additionally, Lasso also performs feature selection.

**Pros**
- solves overfitting
- easy to understand
- improves model interpretability

**Cons**
- decreases the variance of the model less compared to Ridge Regression

---

## PCA 
- A dimensionality reduction technique (Feature Extration) for data sets with many features or dimentsions. It uses linear algebra to determine the most important features of a dataset. After these features have been identified, you can use only the most important features or those that explain the most variance, to train a machine learning model and improve the computational performance of the model without sacrificing accuracy.
- Each of the "new" variables after PCA are all independent of one another, this is a benefit because the assumptions of a linear model requre our independent variables to be independent of one another. 

**Pros:**
- Removes correlated features: PCA will help you remove all the features that are correlated, a phenomenon known as *multi-collinearity*. Finding features that are correlated is time consuming, especially if the number of features is large.
- Improve machine learning algorithm performance: With the number of features reduced with PCA, the time taken to train your model is now significantly reduced.
- Reduce overfitting: By removing the unnecessary features in your dataset, PCA helps to overcome overfitting.

**Cons:**
- Independent variables are now less interpretable: PCA reduces your features into smaller number of components. Each components is now a linear combination of your orginal features, which makes it less readable and interpretable.
- Information loss: Data loss may occur if you do not exercise care in choosing the right number of components.
- Feature scaling: Because PCA is a *variance maximizing exercise*, PCA requires feature to be scaled prior to processing.


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

## Handling Missing Values
1. Deleting Rows with missing values
**Pros:**

A model trained with the removal of all missing values creates a robust model.

**Cons:**

- Loss of a lot of information.
- Works poorly if the percentage of missing values is excessive in comparison to the complete dataset.

2. Impute missing values for continuous variable
**Pros:**

- Prevent data loss which results in deletion of rows or columns
- Works well with a small dataset and is easy to implement.
**Cons:**

- Works only with numerical continuous variables.
- Can cause data leakage
- Do not factor the covariance between features.

4. Impute missing values for categorical variable
When missing values is from categorical columns (string or numerical) then the missing values can be replaced with the most frequent category. If the number of missing values is very large then it can be replaced with a new category.

**Pros:**

- Prevent data loss which results in deletion of rows or columns
- Works well with a small dataset and is easy to implement.
- Negates the loss of data by adding a unique category

**Cons:**

- Works only with categorical variables.
- Addition of new features to the model while encoding, which may result in poor performance

5. Other Imputation Methods
Depending on the nature of the data or data type, some other imputation methods may be more appropriate to impute missing values.

For example, for the data variable having longitudal behavior, it might make sense to use the last valid observation to fill the missing value. This is known as the *Last Observation Carried Forward (LOCF)* method

6. Using Algorithms that support missing values
All the machine learning algorithms don't support missing values but some ML algorithms are robust to missing values in the dataset. 

- KNN: can ignore a column from a distance measure when a value is missing
- Naive Bayes: can support missing values when making a prediction
- RandomForest: works well on non-linear and categorical data, which adapts to the data structure taking into consideration the high variance or the bias, producing better results on large datasets.

**Pros:**

No need to handle missing values in each column as ML algorithms will handle them efficiently.
**Cons:**

No implementation of these ML algorithms in the scikit-learn library.

9. Prediction of missing values
The regression or classification model can be used for the prediction of missing values depending on the nature (categorical or continuous) of the feature having missing value.

11. Imputation using Deep Learning Library — Datawig
This method works very well with categorical, continuous, and non-numerical features. Datawig is a library that learns ML models using Deep Neural Networks to impute missing values in the datagram.
