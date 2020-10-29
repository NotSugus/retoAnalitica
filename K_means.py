import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['figure.figsize'] = (10, 6)
plt.style.use('ggplot')

dataframe = pd.read_csv('avocado.csv')
sb.pairplot(dataframe.dropna(), hue='year', height=4, vars=["AveragePrice", "Total Volume", "Total Bags"], kind='scatter')

X = np.array(dataframe[["AveragePrice", "Total Volume", "Total Bags"]])
Y = np.array(dataframe['year'])
print(X.shape)
fig = plt.figure()
ax = Axes3D(fig)
colores = ['blue', 'red', 'green', 'orange']
asignar = []
for row in Y:
    asignar.append(colores[row-2015])
ax.scatter(X[:,0], X[:, 1], X[:, 2], c=asignar, s=60)

Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]
score
plt.plot(Nc,score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')

kmeans = KMeans(n_clusters=4).fit(X)
centroids = kmeans.cluster_centers_
print(centroids)

# Predicting the clusters
labels = kmeans.predict(X)
# Getting the cluster centers
C = kmeans.cluster_centers_
colores = ['red', 'green', 'blue', 'cyan']
asignar = []
for row in labels:
    asignar.append(colores[row])

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=asignar, s=60)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c=colores, s=1000)

#Getting the values and plotting it
f1 = dataframe["AveragePrice"].values
f2 = dataframe["Total Volume"].values

plt.scatter(f1, f2, c=asignar, s=70)
plt.scatter(C[:, 0], C[:, 1], marker='*', c=colores, s=1000)
plt.show()

f1 = dataframe["AveragePrice"].values
f2 = dataframe["Total Bags"].values

plt.scatter(f1, f2, c=asignar, s=70)
plt.scatter(C[:, 0], C[:, 2], marker='*', c=colores, s=1000)
plt.show()

f1 = dataframe["Total Volume"].values
f2 = dataframe["Total Bags"].values

plt.scatter(f1, f2, c=asignar, s=70)
plt.scatter(C[:, 1], C[:, 2], marker='*', c=colores, s=1000)
plt.show()

copy =  pd.DataFrame()
copy['region']=dataframe['region'].values
copy['year']=dataframe['year'].values
copy['label'] = labels;
cantidadGrupo =  pd.DataFrame()
cantidadGrupo['color']=colores
cantidadGrupo['cantidad']=copy.groupby('label').size()
print(cantidadGrupo)

group_referrer_index = copy['label'] == 0
group_referrals = copy[group_referrer_index]

diversidadGrupo = pd.DataFrame()
diversidadGrupo['year'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
diversidadGrupo['cantidad'] = group_referrals.groupby('year').size()
print(diversidadGrupo)

