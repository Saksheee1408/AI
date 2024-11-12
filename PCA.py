import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

X=pd.read_csv('/content/iris.csv')
X.head()
features=X.drop('species',axis=1)
target=X['species']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

pca=PCA(n_components=2)
X_pca=pca.fit_transform(X_scaled)

plt.figure(figsize=(10, 5))
plt.bar(['PC1', 'PC2'], pca.explained_variance_ratio_)
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance Ratio by Principal Components')
plt.show()

plt.subplot(1,2,1)
scatter=plt.scatter(X_pca[:,0],X_pca[:,1],c=pd.Categorical(target).codes,cmap='rainbow')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('PCA Space')
plt.legend(target.unique())  # Use unique species names
plt.tight_layout()
plt.show()