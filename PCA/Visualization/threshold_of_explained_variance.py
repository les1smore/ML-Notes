scaler = StandardScaler()
data_rescaled = scaler.fit_transform(X)

pca = PCA().fit(data_rescaled)

plt.rcParams['figure.figsize'] = (8,5)

fig,ax = plt.subplots()
xi = np.arange(1, 14, step = 1) # 13 components in total
y = np.cumsum(pca.explained_variance_ratio_)

plt.ylim(0.0,1.1)
plt.plot(xi, y, marker = 'o', linestyle = '-', color = 'black')

plt.xlabel('Number of Components')
plt.xticks(np.arange(1,14,step = 1))
plt.ylabel('Cumulative variance (%)')
plt.title('The number of components needed to explain variance')

# Add a threshold line at 95%
plt.axhline(y=0.95, color = 'grey',linestyle ='--')
plt.text(1.1, 1, '95% cut-off threshold', color = 'black', fontsize = 16)

ax.grid(axis = 'x')
plt.tight_layout()
plt.show()
