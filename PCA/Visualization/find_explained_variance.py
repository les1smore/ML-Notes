# The first step is to find the explained variance for each principal component. 
# We calculate explained variance by first scaling our data with the StandardScalar and fitting a PCA model to the scaled data.

# The StandardScalar is a simple transformation that normalizes the data to have a mean of 0 and 0 unit variance, or a standard deviation of 1.

# You will also notice that the total number of Principal Components equals the number of features in your dataset. However, one important thing to note is that the Principal Components are not the dataset’s columns; rather, PCA is constructing new features that best explain the data.

def get_variance(X,n):
  scaler = StandardScaler()
  pca = PCA(n_components = n)
  pca.fit(scaler.fit_transform(X))

  return pca.explained_variance_ratio_.cumsum()[-1:] # return the value except the last one

for i in range(1,14):
  print('Components:\t', i, '=\t', get_variance(X, i), '\tCumulative Variance')
