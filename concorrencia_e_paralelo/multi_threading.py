from threading import Thread, Lock
import time

contador = 0
lock = Lock()
print_lock = Lock()


def funcao_a(indice):
    global contador
    for i in range(1_000_000):
        lock.acquire() ## tem um peso muito alto no tempo de processamento
        contador += 1
        lock.release() ## tem um peso muito alto no tempo de processamento
    print_lock.acquire()
    print("Fim da Thread", indice)
    print_lock.release()

def main():
    start = time.time()
    lista_de_tarefas = []
    for indice in range(10):
        nova_tarefa = Thread(target=funcao_a, args=(indice,))
        lista_de_tarefas.append(nova_tarefa)
        nova_tarefa.start()
    print(f"Com todas as tarefas iniciadas e indexadas na lista o contador está em {contador/10_000_000 * 100:.4f}%")

    for tarefa in lista_de_tarefas:
        tarefa.join() # Retorna ao fluxo procedural, aguarda o fim da tarefa, e da continuidade

    print(f"Após aguardar o término de todas as tarefas, o contador chegou a {contador/10_000_000 * 100}%")
    print(f"Tempo decorrido = {time.time() - start}") ## Tempo médio de execução = 54s

if __name__ == "__main__":
    main()


# from threading import Thread
# from multi_processing import Process
#
# contador = 0
#
# def funcao_a(indice):
#     global contador
#     for i in range(1_000_000):
#         contador += 1
#     print("Fim da Thread", indice)
#
# def main():
#     lista_de_tarefas = []
#     for indice in range(10):
#         nova_tarefa = Thread(target=funcao_a, args=(indice,))
#         lista_de_tarefas.append(nova_tarefa)
#         nova_tarefa.start()
#     print(f"Com todas as tarefas iniciadas e indexadas na lista o contador está em {contador/10_000_000 * 100:.4f}%")
#
#     for tarefa in lista_de_tarefas:
#         tarefa.join() # Retorna ao fluxo procedural, aguarda o fim da tarefa, e da continuidade
#
#     print(f"Após aguardar o término de todas as tarefas, o contador chegou a {contador/10_000_000 * 100}%")
#
# if __name__ == "__main__":
#     main()



# from threading import Thread
#
# minha_lista = []
# def funcao_a(indice):
#     for i in range(100000):
#         minha_lista.append(1)
#     print('Fim da Thread ', indice)
#
# def main():
#     lista_de_tarefas = []
#     for indice in range(1, 11):
#         novaTarefa = Thread(target=funcao_a, args=(indice, ))
#         lista_de_tarefas.append(novaTarefa)
#         novaTarefa.start()
#
#     print("Antes de finalizar as tarefas, a lista de números está com:", len(minha_lista), "elementos 1")
#
#     for tarefa in lista_de_tarefas:
#         tarefa.join() #Aguarda a finalização da Thread (tarefa) e retorna ao fluxo de execução do software
#
#     print("Após de aguardar o termino das taregas, a lista de números está com", len(minha_lista), "elementos 1")
#
# main()
