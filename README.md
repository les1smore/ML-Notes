# mlnotes
Machine Learning Notes

## PCA
A technique that transforms high-dimensional data into lower dimensions while retaining as much information as possible.

Reference: https://medium.com/towards-data-science/principal-component-analysis-pca-explained-visually-with-zero-math-1cbf392b9e7d

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
