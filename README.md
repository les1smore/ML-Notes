# mlnotes
Machine Learning Notes

## PCA 
A dimensionality reduction technique for data sets with many features or dimentsions. It uses linear algebra to determine the most important features of a dataset. After these features have been identified, you can use only the most important features or those that explain the most variance, to train a machine learning model and improve the computational performance of the model without sacrificing accuracy.

Two criteria:
- The maximum vriance
- The minimum error


Reference: 
1. https://medium.com/towards-data-science/principal-component-analysis-pca-explained-visually-with-zero-math-1cbf392b9e7d
2. https://towardsdatascience.com/2-beautiful-ways-to-visualize-pca-43d737e48ff7
3. https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues/140579
4. https://towardsdatascience.com/2-beautiful-ways-to-visualize-pca-43d737e48ff7

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
The Poisson distribution has the following *Probability Mass Function*
![image](https://user-images.githubusercontent.com/60702562/157318921-b2435859-c0e6-47cb-9a84-c97df2ddd4c3.png)

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

Refrence: https://towardsdatascience.com/an-illustrated-guide-to-the-poisson-regression-model-50cccba15958
