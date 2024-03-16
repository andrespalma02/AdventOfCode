import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

from sklearn.decomposition import PCA
iris = pd.read_csv('data_mutations7.csv')
df2 = iris[iris.columns[:-1]]
X = df2
PCA = PCA(n_components=20)
sns.heatmap(X.corr())
components = PCA.fit_transform(X)
print(components)
#PCA.components_