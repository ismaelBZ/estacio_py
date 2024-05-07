# try:
#     global userCode
#     userCode = eval(input('Digite o código recebido'))
# except NameError:
#     print('Código incorreto!')
# except ValueError:
#     print('Valor Inválido!')
# except:
#     print('Entre em contato com o desenvolvedor!')
# else:
#     print(f'Código {userCode} validado')
# finally:
#     print('Fim da verificação!')

# import test
# test.exemple()

# from tkinter import *
#
# def clickou():
#     print('Clickou')
#
# janelaPrincipal = Tk()
# texto = Label(master=janelaPrincipal, text='Minha primeira janela')
# texto.place(x=50, y=100)
#
# pic = PhotoImage(file="../../estacio")
# logo = Label(master = janelaPrincipal, image = pic)
# logo.pack()
#
# botao = Button(master=janelaPrincipal, text='Clique aqui', command=clickou)
# botao.pack()
# botao.place(x=70, y=150)
# janelaPrincipal.mainloop()


# import time
# import datetime
# import calendar
#
# calendar.setfirstweekday(6)
# month = calendar.month(2024,4)
# print(month)
#
# now = time.asctime(time.localtime())
# now = time.ctime(time.time())
# print(now)

# #import dos pacotes necessários
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib
#
# #criação de um objeto de mensagem
# msg = MIMEMultipart()
# texto = "Estou enviando um email com Python"
#
# #parâmetros
# senha = "SUA SENHA"
# msg['From'] = "SEU E-MAIL"
# msg['To'] = "E-MAIL DESTINO"
# msg['Subject'] = "ASSUNTO"
#
# #criação do corpo da mensagem
# msg.attach(MIMEText(texto, 'plain'))
#
# #criação do servidor
# server = smtplib.SMTP('smtp.gmail.com: 587')
# server.starttls()
#
# #Login na conta para envio
# server.login(msg['From'], senha)
#
# #envio da mensagem
# server.sendmail(msg['From'], msg['To'], msg.as_string())
#
# #encerramento do servidor
# server.quit()
#
# print('Mensagem enviada com sucesso')

import random
# a = random.random()
# b = random.randint(5, 8)
# c = random.uniform(5, 8)
# print(a, b, c)
# sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
# d = random.choice(sequence)
# e = random.sample(sequence,5)
# f = sequence.copy()
# random.shuffle(f)
# print(sequence)
# print(d)
# print(e)
# print(f)


# import math
# x = 16/3
# y = math.ceil(16/3)
# z = math.floor(16/3)
# print(x, y, z)

# def somaDeGaus(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n+somaDeGaus(n-1)
# print(somaDeGaus(5))

# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*fatorial(n-1)
# print(fatorial(3))

# def regressao(x):
#     if x >= 0:
#         print(x)
#         regressao(x-1)
# regressao(10)

# def taximetro (distancia):
#     preco = 1.20
#
#
#     def calcMultiplicador(multiplier):
#         multiplicador = 2
#         for km in range(10, distancia, 5):
#             multiplicador **= multiplier
#         return multiplicador
#
#
#     multiplicador = calcMultiplicador(1)
#     if distancia > 50:
#         multiplicador = calcMultiplicador(1.001)
#     if distancia > 30:
#         multiplicador = calcMultiplicador(1.005)
#     elif distancia > 5:
#         multiplicador = calcMultiplicador(0.9)
#
#
#     valorFinal = distancia * preco * multiplicador
#     print(f'{valorFinal:.2f}')
#     return valorFinal
#
#
# taximetro(10)
# taximetro(15)
# taximetro(20)
# taximetro(30)
# taximetro(50)
# taximetro(100)


# def func1():
#     global x
#     x = 10      # Local -> Global
#     print(f'Na função func1, x = {x}')


# def func2():
#     global x
#     x = 20      # Local -> Global
#     print(f'Na função func1, x = {x}')
#
#
# x = 0       # Global -> Local
# print(f'No programa principal, x = {x}')
# func1()
# print(f'No programa principal, agora x = {x}')
# func2()
# print(f'No programa principal, agora x = {x}')


# def taximetro(distancia, multiplicador=1):
#     preco = 10
#     return preco*distancia*multiplicador
# print(f'Valor da corrida: R${taximetro(15, 3)}')
# print(f'Valor da corrida: R${taximetro(3)}')

# isTest('Yes')
# def isTest(answer):
#     print(f'Is a test: {answer}')

# for number in range(10):
#   if number < 5:
#     pass
#   elif number > 5:
#     pass
#   else:
#     print(f'Number {number}')

# for number in range(5):
#   if number == 3:
#     continue
#   print(number)

# while True:
#     print('Você está no primeiro laço.')
#     opcao1 = input('Deseja sair dele? Digite SIM para isso. \n')
#     if opcao1 == 'SIM':
#         break  # este break é do primeiro laço
#     else:
#         while True:
#             print('Você está no segundo laço.')
#             opcao2 = input('Deseja sair dele? Digite SIM para isso. \n')
#             if opcao2 == 'SIM':
#                 break  # este break é do segundo laço
#         print('Você saiu do segundo laço.')
# print('Você saiu do primeiro laço')

# for number in range(99):
#     if number < 5:
#         print(number)
#     else:
#         print('Break')
#         break

# userInput = 'enter while'
# while userInput != 'sair':
#     userInput = input('Digite sair: ')

# name = input('Digite o seu nome')
# splitedName = []
# for letter in name:
#     splitedName.append(letter)
# print(splitedName)

# colors = ['amarelo', 'azul', 'branco', 'laranja', 'preto', 'rosa', 'verde', 'vermelho']
# userInput = input('Digite uma cor: ').lower()
# disponivel = False
# for color in colors:
#     if color == userInput:
#         disponivel = True
# if disponivel:
#     print('Tinta disponível no estoque!')
# else:
#     print('Escolha outra cor')

# idade = eval(input('Informe a sua idade: '))
# estaAcompanhado = False
# if idade >= 18:
#     print('Entrada autorizada')
# elif idade < 18 & estaAcompanhado:
#     print('Entrada autorizada')
# else:
#     print('Volte com um acompanhante')
# print('Proibida entrada de menores não acompanhados)

# color = input('Digite uma cor: ').upper()
# if color == 'AZUL':
#     print('A cor escolhida é azul')
# elif color == 'VERMELHO':
#     print('A cor escolhida é vermelho')
# elif color == 'AMARELO':
#     print('A cor escolhida é amarelo')
# elif color == 'VERDE':
#     print('A cor escolhida é verde')
# elif color == 'PRETO':
#     print('A cor escolhida é preto')
# elif color == 'BRANCO':
#     print('A cor escolhida é branco')
# else:
#     print('Escolha outra cor')

# a,b = 1,2
# a,b = b,a
# print(a,b)
