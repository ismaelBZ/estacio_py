from threading import Thread
from multiprocessing import Process
def funcao_a(nome):
    print(nome)

def main():
    p = Process(target=funcao_a, args=('Meu Processo',))
    p.start()

    t = Thread(target=funcao_a, args=('Minha Thread',))
    t.start()


if __name__ == '__main__':
    main()