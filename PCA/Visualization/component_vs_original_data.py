# We will use the inverse_transform method of the PCA model, and this will take each of the components and transform them back into the original data scale. 
# We will plot the entire range of components from 1-13 and overlay them with the original data.

# Function to perform PCA with n-components
def transform_pca(X, n):
  pca = PCA(n_components=n)
  pca.fit(X)
  X_new = pca.inverse_transform(pca.transform(X))
  return X_new

rows = 4
cols = 4
comps = 1

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

fig, axes = plt.subplots(rows, 
                         cols, 
                         figsize=(12,12), 
                         sharex=True, 
                         sharey=True)


for row in range(rows):
    for col in range(cols):
        try:
            X_new = transform_pca(X_scaled, comps) # the orginal data
            ax = sns.scatterplot(x=X_scaled[:, 0], 
                                 y=X_scaled[:, 1], 
                                 ax=axes[row, col], 
                                 color='blue', 
                                 alpha=.3)
            ax = sns.scatterplot(x=X_new[:, 0],  # each PCA component
                                 y=X_new[:, 1], 
                                 ax=axes[row, col], 
                                 color='red',
                                 alpha = .5)
            ax.set_title(f'PCA Components: {comps}');

            comps += 1
        except:
            pass
plt.tight_layout()
