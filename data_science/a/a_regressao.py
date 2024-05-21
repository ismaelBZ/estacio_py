# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# import pandas
#
# dados = pandas.read_csv('dengue_data.csv')
# anos = dados[['ano']]
# numero_casos = dados[['casos']]
#
# lin_regr = LinearRegression()
# lin_regr.fit(X=anos, y=numero_casos)
#
# ano_previsao = [[2018]]
# casos_previstos = lin_regr.predict(ano_previsao)
#
# print(f'Casos de dengue previstos para 2018 chega á {int(casos_previstos)}')
#
# plt.scatter(anos, numero_casos, color='black')
# plt.scatter(ano_previsao, casos_previstos, color='red')
# plt.plot(anos, lin_regr.predict(anos), color='blue')
#
# plt.xlabel('Anos')
# plt.ylabel('Casos de Dengue')
# plt.xticks([2018])
# plt.yticks([int(casos_previstos)])
#
# plt.show()










# import numpy as np
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt
#
# x = np.array([5, 10, 15, 20, 25, 30]).reshape((-1, 1))
# y = np.array([6, 12, 14, 23, 27, 32])
#
# model = LinearRegression().fit(x, y)  # regression line
#
# y_predict = model.predict(x) # passing x params again to compare real to predict
#
# print('Dados do teste: ', y)
# print('Dados da predição: ', y_predict)
#
# plt.scatter(x, y, c='blue')
# plt.plot(x, y_predict, c='red')
# plt.legend(['Real', 'Predição'])
# plt.show()