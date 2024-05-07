from multiprocessing import Process, Value
import time

def funcao_a(indice, counter):
    for i in range (100_000):
        with counter.get_lock():
            counter.value += 1
    print("Termino do processo", indice)

def main():
    start = time.time()
    contador = Value('i', 0)
    lista_de_tarefas = []
    for indice in range(10):
        nova_tarefa = Process(target=funcao_a, args=(indice, contador))
        lista_de_tarefas.append(nova_tarefa)
        nova_tarefa.start()

    print("Antes de aguardar o término das tarefas, o contador está em:", contador.value)

    for tarefa in lista_de_tarefas:
        tarefa.join()

    print("Após a finalização de todas as tarefas, o contador chegou em:", contador.value)
    print(f"Tempo decorrido = {time.time() - start}") ## Tempo aproximado de execução => 20s

if __name__ == "__main__":
    main()


# from multiprocessing import Process
#
# minha_lista = []
#
# def funcao_a(indice):
#     for i in range(100000):
#         minha_lista.append(1)
#         print("Fim do processo", indice)
#
# def main():
#     lista_de_tarefas = []
#     for indice in range(10):
#         nova_tarefa = Process(target=funcao_a, args=(indice,))
#         lista_de_tarefas.append(nova_tarefa)
#         nova_tarefa.start()
#
#     print("Sem aguardar o fim das tarefas a lista de números já adicionou", len(minha_lista), "elementos")
#
#     for tarefa in lista_de_tarefas:
#         tarefa.join()
#
#     print("Agora, tendo aguardado o fim de execução de todas as tarefas e retornado ao fluxo normal do software \n"
#           "a lista de números está com um total de", len(minha_lista), "elementos")
#
# if __name__ == "__main__":
#     main()


