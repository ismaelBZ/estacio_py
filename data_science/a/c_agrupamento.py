from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

######### Pré-processamento

#### Coleta e integração
iris = load_iris()
# print(iris)
#iris.data = flowers_caracteristhics
#iris.target = flowers_classification
caracteristicas_das_amostras = iris.data


######### Mineração
grupos = KMeans(n_clusters=3) # Número de grupos ou subdivisões (espécies da amostra)
grupos.fit(X=caracteristicas_das_amostras)
labels = grupos.labels_ # Cria um rotulo para as amostas

######### Pós-processamento
fig = plt.figure(1)
axes = Axes3D(fig)
axes.set_xlabel('Comprimento da Sépala')
axes.set_ylabel('Largura da Sépala')
axes.set_zlabel('Comprimento da Pétala')
axes.scatter(caracteristicas_das_amostras[:, 0], caracteristicas_das_amostras[:, 1], caracteristicas_das_amostras[:, 2],
             c=grupos.labels_, edgecolor='k')

target = iris.target
fig = plt.figure(2)
axes = Axes3D(fig)
axes.set_xlabel('Comprimento da Sépala')
axes.set_ylabel('Largura da Sépala')
axes.set_zlabel('Comprimento da Pétala')
axes.scatter(caracteristicas_das_amostras[:, 0], caracteristicas_das_amostras[:, 1], caracteristicas_das_amostras[:, 2],
             c=target, edgecolors='k')

plt.show()


