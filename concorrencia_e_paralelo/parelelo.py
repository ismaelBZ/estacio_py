# from threading import Thread
# import urllib3
# from time import time
#
# start = time()
# urls_list = ['https://www.google.com', 'https://www.apple.com', 'https://www.microsoft.com', 'https://www.instagram.com']
#
# def teste_url(url):
#     start = time()
#     response = urllib3.request('GET', url)
#     print(f'Loading time = {time() - start :5.2f} \t {url} \t Response: {response.status}')
#
#
# threads = [Thread(target=teste_url, args=(url, )) for url in urls_list]
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()
#
# print(f'All process time = {time() - start:5.2f}')

# from threading import Thread
# from time import sleep
#
# def append1(lista):
#     for i in range(1, 6):
#         print(i)
#         lista.append(i)
#         sleep(0.4)
#
# def append2(lista):
#     for i in range(6, 11):
#         print(i)
#         lista.append(i)
#         sleep(0.5)
#
#
# a_lista = []
# a_thread = Thread(target=append1, args=(a_lista,))
# a_thread.start()
#
# b_lista = []
# b_thread = Thread(target=append2, args=(b_lista,))
# b_thread.start()
#
# a_thread.join()
# b_thread.join()
#
# lista = a_lista + b_lista
# print(lista)




# from threading import Thread
# from time import sleep
#
# lista = []
#
#
# def append1():
#     for i in range(1, 6):
#         print(i)
#         lista.append(i)
#         sleep(0.4)
#
#
# def append2():
#     for i in range(6, 11):
#         print(i)
#         lista.append(i)
#         sleep(0.5)
#
# a_thread = Thread(target=append1)
# a_thread.start()
# a_thread.join()
#
# b_thread = Thread(target=append2)
# b_thread.start()
# b_thread.join()
#
# print(lista)



# from threading import Thread
# from time import sleep
#
# lista = []
#
# def append1():
#     for i in range(1, 6):
#         print(i)
#         lista.append(i)
#         sleep(0.4)
#
# def append2():
#     for i in range(6, 11):
#         print(i)
#         lista.append(i)
#         sleep(0.5)
#
# a_thread = Thread(target=append1)
# a_thread.start()
#
# b_thread = Thread(target=append2)
# b_thread.start()
#
# a_thread.join()
# b_thread.join()
#
# print(lista)



# from threading import Thread
# from time import sleep
#
# lista = []
#
# def append1():
#     for i in range (1, 6):
#         print(i)
#         lista.append(i)
#         sleep(0.4)
#
# def append2():
#     for i in range(6, 11):
#         print(i)
#         lista.append(i)
#         sleep(0.5)
#
# a_thread = Thread(target=append1)
# a_thread.start()
#
# b_thread = Thread(target=append2)
# b_thread.start()
#
# print(lista)

#
# from threading import Thread
# from time import sleep, time
# from functools import partial
#
# def task(exponential, await_time, task_name, number):
#     await_seconds = 1
#     start = time()
#     print(f'Thread {task_name} start!')
#     result = number ** exponential
#     for i in range(await_time + 1):
#         print(f'{task_name} \t - Await - {await_seconds}s')
#         await_seconds += 1
#         sleep(1)
#     print(f'Thread {task_name} ends in {time() - start:5.2f}s! \n'
#           f'Operation {number} exp {exponential} = {result}')
#
#
# exp2 = partial(task, 2, 2)
# exp3 = partial(task, 3, 3)
#
# a_thread = Thread(target=exp3, args=('A', 5))
# a_thread.start()
#
# b_thread = Thread(target=exp2, args=('B', 5))
# b_thread.start()
#
# a_thread.join()
# b_thread.join()

# from threading import Thread
# from time import sleep
#
# def task(await_time):
#     print('Thread start!')
#     await_seconds = 1
#     for time in range(1, await_time + 1):
#         print(f'Await {await_seconds}s')
#         sleep(1)
#         await_seconds += 1
#     print('Thread ends!')
#
# thread = Thread(target=task, args=(2,))
# thread.start()



# from threading import Thread
# from time import sleep
#
# def function(mensage):
#     for i in range(3):
#         print(i, mensage)
#         sleep(1.5)
#
# print('Iniciando o programa!')
# thread = Thread(target=function, args=('Executando!',))
# thread.start()
# # thread.join()
# # sleep(2)
# print('Finalizando o programa!')



# from threading import Thread
# import time
#
# def function():
#     for i in range(3):
#         print(i, 'Executando Thread!')
#         time.sleep(3)
#
# print('Iniciando o programa!')
# thread = Thread(target=function)
# thread.start()
# thread.join()
# print('Finalizando o programa!')



# from threading import Thread
# import time
#
# def function():
#     for i in range(3):
#         print(i, 'Executando Thread!')
#         time.sleep(3)
#
# print('Iniciando o programa!')
# Thread(target=function).start()
# print('Finalizando o programa!')