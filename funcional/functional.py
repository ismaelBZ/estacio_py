
#### Advancing | Attgeter, Colection and Partial
# import collections
# from operator import attrgetter
# from functools import partial

# pessoa = collections.namedtuple('pessoa', 'nome idade')
# pessoas = [pessoa('João', 40), pessoa('Ana', 29), pessoa('Renata', 25)]
# print(sorted(pessoas, key=attrgetter('nome')))
# print(sorted(pessoas, key=attrgetter('idade')))

# pessoa = collections.namedtuple('pessoa', 'nome idade')
# pessoas = [pessoa('Jõao', 40), pessoa('Ana', 29), pessoa('Renata', 25)]
# sort_nome = partial(sorted, key=attrgetter('nome'))
# sort_idade = partial(sorted, key=attrgetter('idade'))
# print(sort_nome(pessoas))
# print(sort_idade(pessoas))



#### Advancing | Operator, Reduce and Partial
# import operator
# print(operator.add(10,29))
# print(operator.concat('Ismael ', 'Bet Zoletti'))
#
# from functools import reduce
# print(reduce(operator.concat, ['Ismael ', 'Bet ', 'Zoletti']))
#
# from functools import partial
# add_one = partial(operator.add, 1) ## Partial retorna uma função
# print(add_one(5))



#### Mutabilidade
# def sum(numeros): #Fazer um destructuring da lista, pegando apenas os valores de interesse
#     if not numeros: #criterio de parada
#         return 0
#     primeiro = numeros[0]
#     resto = numeros[1:]
#     return primeiro + sum(resto)
#
# print(sum([1,2,3,4]))
#
# def joinList(lista1, lista2):
#     nova_lista = lista1 + lista2
#     return nova_lista
# lista = ['Ferrarri']
# nova_lista = lista + ['Porsche']
# print(nova_lista)
# print(joinList(lista, ['Porsche']))



#### O que você quer
# numbers = [1, 2, 3, 4]
# print('O total é', sum(numbers))
# print('Tudo certo!' if True else 'Ops') ## Ternary | Short Hand | Conditional Expression
