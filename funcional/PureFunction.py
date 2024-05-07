# # lista_original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # def increase1(lista, ammount=1):
# #    def increase(n):
# #       return n + ammount
# #    nova_lista = list(map(increase, lista)) # NÃO UTILIZA LOOP
# #    return nova_lista
# #
# # lista_modificada = increase1(lista_original)
# # lista_modificada2 = increase1(lista_original, 3)
# # print(lista_original) # NÃO ALTERA O DADO
# # print(lista_modificada) # FAZ A ALTERAÇÃO APENAS DEPENDENDO DOS ARGUMENTOS DE ENTRADA
# # print(lista_modificada2)
#
#
# lista_original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# def increase1(lista):
#     for i in lista:
#         lista[i] = i + 1
#         return lista
#     # A função fere um dos princípios da programação funcional que é conter um loop
#
# lista_modificada = increase1(lista_original)
#
# print()
# print(f'Lista original: {lista_original}')
# print(f'Lista modificada: {lista_modificada}')
# # Altera o valor da lista original


# def multipica(factor, value=20):
#     result = value * factor
#     print(result)
#     return result
#     # Depende apenas dos valores de entrada,
#     # Não altera nem um valor externo
#     # Tem o método de retorno
#
# multipica(5)
# multipica(5)
# multipica(10, 10)
# multipica(10, 10)
##Gera os mesmos resultados para os mesmos valores de entrada


# valor = 20
#
# def multipica(fator):
#     global valor
#     valor = valor * fator
#     print('Resultado: ', valor)
#     # A função altera uma variável fora do escopo,
#     # não depende apenas dos valores de entrada
#     # e não tem nem um retorno
#
#
# multipica(10)
# multipica(10)
##Gera valores diferentes a cada execução