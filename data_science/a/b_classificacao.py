# """
# Para este exemplo, utilizaremos um conjunto de dados (dataset)
# criado em 1938 e utilizado até hoje: o dataset da Flor de Íris
# ou Iris Dataset. Por ser um dataset muito utilizado e pequeno,
# a bliblioteca do o Scikit-Learn já o disponibiliza internamente.
#
# Para a analise supervisionada de classificação dos dados, serão
# utilizados dois métodos, Arvóre de decisão e Máquina de Vetor de
# Suporte
# """
#
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


##### Pré-processamento #####

# Coleta e integração
iris_db = load_iris()

caracteristicas = iris_db.data
rotulos = iris_db.target

# Partição dos dados
carac_treino, carac_teste, rot_treino, rot_teste = train_test_split(caracteristicas, rotulos)

##### Mineração #####

#--#--#-- Arvore de decisão --#--#--#
arvore = DecisionTreeClassifier(max_depth=2)
arvore.fit(X=carac_treino, y=rot_treino)

rot_previstos = arvore.predict(carac_teste)
acuracia_arvore = accuracy_score(rot_teste, rot_previstos)

#--#--#-- Máquina de Vetor de Suporte --#--#--#
clf = SVC()
clf.fit(X=carac_treino, y=rot_treino)

rot_previstos_svm = clf.predict(carac_teste)
acruracia_svm = accuracy_score(rot_teste, rot_previstos_svm)


##### Pós-Processamento #####
print("Acurácia Árvore de Decisão: ", round(acuracia_arvore, 5))
print("Acurácia Máquina de Vetor de Suporte: ", round(acruracia_svm, 5))

r = export_text(arvore, feature_names=iris_db['feature_names'])
print('Estrutura da Árvore')
print(r)
#
#
# """"
#   As características das flores estão separadas na variável
# características. Ela contém uma lista com 150 itens,
# onde cada item contém outra lista com quatro elementos.
#   No conteúdo dos dois primeiros itens dessa lista no console,
# cada um dos quatro elementos corresponde ao comprimento da sépala,
# largura da sépala, comprimento da pétala e largura da pétalas
# respectivamente.
# """
#
# """"
# Os rótulos (ou classes) na variável rótulo, contém uma lista com 150
# itens que variam entre 0, 1 ou 2. Cada número corresponde a uma
# classe de flor:
#     0: Iris-Setosa;
#     1:Iris-Versicolor;
#     2:Iris-Virginica
# """




##### Treinamento supervisionado - classificação
# from sklearn.tree import DecisionTreeClassifier
#
# lisa = 1
# irregular = 0
# pera = 1
# laranja = 0
#
# pomar = [[120, lisa], [140, lisa], [180, irregular], [200, irregular]]
# resultado = [pera, pera, laranja, laranja]
#
# classificador = DecisionTreeClassifier()
# classificador.fit(pomar, resultado)
#
# peso = 220
# superficie = 0
# resultado = classificador.predict([[peso, superficie]])
# if resultado == 1:
#     print('Pera')
# elif resultado == 0:
#     print('Laranja')