from functools import reduce

def soma(numbers):
    try:
        return reduce((lambda x,y: x + y), numbers)
    except:
        print('Non valid argument found')

print(soma([1, 2, 3, 4, 5]))

# lista_numeros = [9.12345, 9.12345, 9.12345, 9.12345]
# lista_precisao = [2, 2, 3, 3]
#
# def define_list_precision(lista_numeros, lista_precisao):
#     if len(lista_numeros) == len(lista_precisao):
#         try:
#             return list(map((lambda numero, precisao: round(numero, precisao)), lista_numeros, lista_precisao))
#         except:
#             print('Non vallid argument found')
#     else:
#         print('Lists have diferent lenghts')
#
# print(define_list_precision(lista_numeros, lista_precisao))



# lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#
#
# def find_even(lista):
#    return list(filter(lambda number: number % 2 == 0, lista))
#
#
# print(find_even(lista))


# vehicles = ['aviao', 'carro', 'navio', 'onibus']
#
#
# def uppercase(to_upper):
#     try:
#         if type(to_upper) == str:
#             return to_upper.upper()
#         else:
#             return list(map(lambda string: string.upper(), to_upper))
#     except:
#         print('Non string found!')
#
#
# print(uppercase(vehicles))
# print(uppercase('Name'))
# print(uppercase(['Name']))
