"""How to choose the number of components?"""
"""A: Don't do it. Don't choose the number of components mannually."""
"""Instead of that, use the option that allows you to set the variance of the input that is supposed to be exlained by the generated components."""

# Remember to scale the data to the range between 0 and 1 before using PCA!
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
data_rescaled = scaler.fit_transform(data)

# Typically, we want the explained variance to be between 95%-99%.
# 95% of variance
from sklearn.decomposition import PCA
pca = PCA(n_components = 0.95)
pca.fit(data_rescaled)
reduced = pca.transform(data_scaled)

# 99% of variance
from sklearn.decomposition import PCA
pca = PCA(n_components = 0.99)
pca.fit(data_rescaled)
reduced = pca.transform(data_scaled)
