import datetime

class Client:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf

class Statement:
    def __init__(self):
        self.history = []

    def get_statement(self, account):
        for t in self.history:
            print(f'{t[0]:12s} {t[1]:22.2f} \n'
                  f'{t[2]:16s} {t[3].strftime("%d/%b/%y %H:%M:%S")}'
                  f'\n')

class Conta:

    def __init__(self, number, clients, balance=0):
        self.number = number
        self.clients = clients
        self.balance = balance
        self.statement = Statement()
        self.created = datetime.datetime.today().strftime('%d/%b/%Y at %H:%M:%S')

    def deposit(self, value):
        self.balance += value
        self.statement.history.append(['Depósito:', value, 'Data:', datetime.datetime.today() ])

    def draw(self, value):
        if value > 0 and value <= self.balance:
            self.balance -= value
            self.statement.history.append(['Saque:', value, 'Data', datetime.datetime.today()])

    def transfer(self, value, account):
        if value > 0 and value <= self.balance:
            self.balance -= value
            self.statement.history.append(['Transferencia:', value, 'Data', datetime.datetime.today()])
            account.deposit(value)

    def get_statement(self):
        print('')
        print(f'Conta: {self.number:28d}')
        print(f'Saldo: {self.balance:28d}')
        print('-----------------------------------')
        print('Lista de titulares:')
        print('-----------------------------------')
        if type(self.clients) == Client:
            print(f'{"Nome:":5s} \t\t\t\t {self.clients.name:>14s} \n'
                  f'{"Cpf:":5s}  \t\t\t\t {self.clients.cpf}')
            print('-----------------------------------')
        else:
            for client in self.clients:
                print(f'{"Nome:":5s} \t\t\t\t {client.name:>14s} \n'
                      f'{"Cpf:":5s}  \t\t\t\t {client.cpf}')
                print('-----------------------------------')
        self.statement.get_statement(self)
        print('-----------------------------------')
        print(f'Saldo: {self.balance:28d}')


class Poupanca:
    def __init__(self, return_rate):
        self.return_rate = return_rate
        self.created = datetime.datetime.today().strftime("%d/%b/%Y at %H:%M:%S")

