import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas

dados = pandas.read_csv('dengue_data.csv')
anos = dados[['ano']]
numero_casos = dados[['casos']]

lin_regr = LinearRegression()
lin_regr.fit(X=anos, y=numero_casos)

ano_previsao = [[2018]]
casos_previstos = lin_regr.predict(ano_previsao)

print(f'Casos de dengue previstos para 2018 chega á {int(casos_previstos)}')

plt.scatter(anos, numero_casos, color='black')
plt.scatter(ano_previsao, casos_previstos, color='red')
plt.plot(anos, lin_regr.predict(anos), color='blue')

plt.xlabel('Anos')
plt.ylabel('Casos de Dengue')
plt.xticks([2018])
plt.yticks([int(casos_previstos)])

plt.show()