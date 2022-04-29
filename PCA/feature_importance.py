"""Obtain importances from PCA loading scores"""
from sklearn.decomposition import PCA

pca = PCA().fit(X_train_scaled)

plt.plot(pca.explained_variance_ratio_.cumsum(), lw=3, color = '#087E8B')
plt.title('Cumulative explained variance by number of principal components', size=20)
plt.show()

"""Convert every coefficient to a dataframe"""
loadings = pd.DataFrame(data = pca.components_.T * np.sqrt(pca.explained_variance_),
                        columns = [f'PCA{i}' for i in range(1, len(X_train.columns) + 1)],
                        index = X_train.columns
                       )
loadings

"""Pick out one principal component that explains as much variance in the dataset"""
# Here I picked the third one
pca3_loadings = loadings.sort_values(by='PCA3', ascending=False)[['PCA3']]
pca3_loadings = pca3_loadings.reset_index()
pca3_loadings.columns = ['Attribute', 'CorrelationWithPC1']

plt.figure(figsize=(12,10))
plt.bar(x=pca3_loadings['Attribute'], height=pca3_loadings['CorrelationWithPC1'], color='#087E8B')
plt.title('PCA loading scores (first principal component)', size=20)
plt.xticks(rotation='vertical')
plt.show()
