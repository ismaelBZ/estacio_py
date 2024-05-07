import datetime
#
class Client:
    def __init__(self, name, cpf, address):
        self.__name = name
        self.__cpf = cpf

    @property
    def get_name(self):
        return self.__name

    @property
    def get_cpf(self):
        return self.__cpf


class Statement:
    def __init__(self):
        self.__history = []

    @property
    def get_history(self):
        return self.__history

    def add(self, transaction):
        self.__history.append(transaction)

#   t = transaction
    def getStatement(self):
        for t in self.__history:
            print(f'{t[0]:8s} {t[1]:10.2f} {t[2]:10s} {t[3].strftime("%d/%b/%y")}')


class Conta:
    def __init__(self, number, clients):
        self.__number = number
        self.__clients = clients
        self.__balance = 0
        self.__statement = Statement()
        self.__createdAt = datetime.datetime.now()

    @property
    def get_number(self):
        return self.__number

    @property
    def get_clients(self):
        clientList = []
        for client in self.__clients:
            clientList.append(client)
        return clientList

    @property
    def get_balance(self):
        return self.__balance

    @property
    def statement(self):
        return self.__statement

    @statement.getter
    def statement(self):
        return self.__statement


    def draw(self, value):
        if value > 0 and value <= self.__balance:
            try:
                self.__balance -= value
                self.__statement.add((['Saque', -value, 'Data:', datetime.datetime.now()]))
                return True
            except:
                print('Saque mal sucedido.')
                return False
        else:
            print('Valor indisponível.')
            return False

    def deposit(self, value):
        if value > 0:
            try:
                self.__balance += value
                self.__statement.add(['Depósito', +value, "Data:", datetime.datetime.today()])
                return True
            except:
                print('Erro ao executar o depósito, tente novamente mais tarde.')
        else:
            return False

    def transfer(self, value, account):
        if value > 0 and value <= self.__balance:
            try:
                self.__balance -= value
                self.__statement.add(['Transferência', -value, 'Data:', datetime.datetime.today()])
                account.deposit(value)
                account.statement().add(['Transferência', +value, 'Data:', datetime.datetime.today()])
                return True
            except:
                print('Erro ao executar a transferência, tente novamente mais tarde.')
                return False
        else:
            print('Valor indisponível.')
            return False

    def extract(self, client):
        print(f'\n'
              f'Número da conta: {self.__number} \n'
              f'Cliente: {client.get_name} \n'
              f'Cpf: {client.get_cpf} \n'
              f'Saldo: {self.__balance} \n'
        )
        self.statement.getStatement()

# def main():
#     client1 = Client('Marluzi', '000.000.000-00', 'Rua das flores')
#     client2 = Client('Dalustre', '999.999.999-99', 'Beira mar')
#
#     contaConjunta = Conta(101, [client1, client2])
#     contaConjunta.deposit(5000)
#     contaConjunta.draw(3000)
#     contaConjunta.statement.getStatement()
#
# if __name__ == '__main__':
#     main()



# class Conta:
#
#     __agency = 3000
#
#     def __init__(self, owner, number ):
#         self.__number = number
#         self.__owner = owner
#         self.__balance = 0
#
#     @staticmethod
#     def get_agency():
#         return Conta.__agency
#
#     @staticmethod
#     def set_agency(newNumber):
#         Conta.__agency = newNumber
#
#     @property
#     def number(self):
#         return self.__number
#
#     @property
#     def owner(self):
#         return self.__owner
#
#     @property
#     def getBalance(self):
#         return self.__balance
#
#     def deposit(self, value):
#         if value > 0:
#             try:
#                 self.__balance += value
#                 return True
#             except:
#                 print('--- Error ----')
#                 return False
#         return False
#
#     def __decreaseBalance(self, value):
#         if value <= self.__balance:
#             try:
#                 self.__balance -= value
#             except:
#                 print('--- Error ----')
#
#     def transfer(self, value, account):
#         try:
#             self.__decreaseBalance(value)
#             account.deposit(value)
#             return True
#         except:
#                 print('--- Error ----')
#                 return False
#
#     def draw(self, value):
#         try:
#             self.__decreaseBalance(value)
#             return True
#         except:
#             return False
#
#
# def main():
#     c1 = Conta('Ismael', 10354)
#     c2 = Conta('Andressa', 22335)
#     print('\n')
#     print(f'Agência: {Conta.get_agency():26d}')
#     print('-----------------------------------')
#     print(f'Conta c1 - Titular: \t\t{c1.owner:}')
#     print(f'Conta c1 - Número da conta: {c1.number:7d}')
#     print('-----------------------------------')
#     c1.deposit(5000)
#     c1.draw(1000)
#     c1.transfer(3000, c2)
#     print('-----------------------------------')
#     print(f'Conta c1 - Saldo: {c1.getBalance:17.2f}')
#     print(f'Conta c2 - Saldo: {c2.getBalance:17.2f}')
#     print('-----------------------------------')
#
# if __name__ == '__main__':
#     main()

# Class Atribute | @classMethod | Class Atribute
# class Circulo:
#     __total_circulos = 0
#
#     def __init__(self, radius, positionX, positionY):
#         self._positionX = positionX
#         self._positionY = positionY
#         self._radius = radius
#         type(self).__total_circulos += 1
#
#     @property
#     def posX(self):
#         return self._positionX
#
#     @posX.setter
#     def posX(self, newPosition):
#         self._positionX = newPosition
#
#     @property
#     def posY(self):
#         return self._positionY
#
#     @posY.setter
#     def posY(self, newPosition):
#         self._positionY = newPosition
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, newRadius):
#         self._radius = newRadius
#
#     @classmethod
#     def get_total_circulos(cls):
#         return cls.__total_circulos
#
# def main():
#     c1 = Circulo(10, 10, 10)
#     c2 = Circulo(5,  10, 10)
#     c3 = Circulo(3,  10, 10)
#     c4 = Circulo(1,  10, 10)
#     print(Circulo.get_total_circulos)
#     print(c1.get_total_circulos())
#     print(c3.get_total_circulos())
#     print(c4.get_total_circulos())
#
# if __name__ == '__main__':
#     main()


# class Circulo:
#     _total_circulos = 0
#
#     def __init__(self, radius, positionX, positionY):
#         self._radius = radius
#         self._positionX = positionX
#         self._positionY = positionY
#         Circulo._total_circulos += 1
#
# def main():
#     c1 = Circulo(10, 10, 10)
#     c2 = Circulo(10, 8, 8)
#     c3 = Circulo(10, 6, 6)
#     c4 = Circulo(10, 4, 4)
#     c5 = Circulo(10, 2, 2)
#     print(Circulo._total_circulos)
#     print(c1.__class__._total_circulos)
#
#
# main()


# GETTERS AND SETTERS | GETTERS AND SETTERS | GETTERS AND SETTERS
# class Conta:
#
#     def __init__(self, accountnumber, owner):
#         self._accountnumber = accountnumber
#         self._owner = owner
#
#     @property
#     def accountNumber(self):
#         return self._accountnumber
#
#     @property
#     def owner(self):
#         return self._owner
#
#     @owner.setter
#     def owner(self, newOwner):
#         self._owner = newOwner
#
#
# def main():
#     c1 = Conta(101, 'Marluzi')
#     print('\n')
#     print(c1.accountNumber)
#     print(c1.owner)
#     c1.owner = 'Iluztree'
#     print(c1.owner)
#
# if __name__ == '__main__':
#     main()


# def main():
#     c1 = Conta(101)
#     print(f'\n{c1._Conta__numero}')
#
# main()

# import datetime
#
# class Cliente:
#     def __init__(self, name, cpf, address):
#         self.name = name
#         self.cpf = cpf
#
# class Statement:
#     def __init__(self):
#         self.history = []
#
#     # ta = transaction argument
#     def getStatement(self):
#         for ta in self.history:
#             print(f'{ta[0]:8s} {ta[1]:10.2f} {ta[2]:10s} {ta[3].strftime("%d/%b/%y")}')
#
#
# class Conta:
#     def __init__(self, number, clients):
#         self.number = number
#         self.clients = clients
#         self.balance = 0
#         self.statement = Statement()
#         self.createdAt = datetime.datetime.now()
#
#     def draw(self, value):
#         if value > 0 and value <= self.balance:
#             self.balance -= value
#             self.statement.history.append(['Saque', -value, 'Data:', datetime.datetime.now()])
#             return True
#         else:
#             return False
#
#     def deposit(self, value):
#         if value > 0:
#             self.balance += value
#             self.statement.history.append(['Depósito', +value, "Data:", datetime.datetime.today()])
#             return True
#         else:
#             return False
#
#     def transfer(self, value, account):
#         if value > 0 and value <= self.balance:
#             self.balance -= value
#             self.statement.history.append(['Transferência', -value, 'Data:', datetime.datetime.today()])
#             account.deposit(value)
#             account.statement.history.append(['Transferência', +value, 'Data:', datetime.datetime.today()])
#             return True
#         else:
#             return False
#
#     def extract(self, client):
#         print(f'\n'
#               f'Número da conta: {self.number} \n'
#               f'Cliente: {client.name} \n'
#               f'Cpf: {client.cpf} \n'
#               f'Saldo: {self.balance} \n'
#         )
#
# def main():
#     client1 = Cliente('Marluzi', '000.000.000-00', 'Rua das flores')
#     client2 = Cliente('Dalustre', '999.999.999-99', 'Beira mar')
#
#     contaConjunta = Conta(101, [client1, client2])
#     contaConjunta.deposit(5000)
#     contaConjunta.draw(3000)
#     contaConjunta.statement.getStatement()
#
# if __name__ == '__main__':
#     main()

# class Conta:
#     def __init__(self, number, owner, cpf):
#         self.number = number
#         self.owner = owner
#         self.cpf = cpf
#         self.balance = 0
#
#     def deposit(self, value):
#         if value > 0:
#             self.balance += value
#             return True
#         else:
#             return False
#
#     def draw(self, value):
#         if value > 0 and value <= self.balance:
#             self.balance -= value
#             return True
#         else:
#             return False
#
#     def transfer(self, value, account):
#         if value > 0 and value <= self.balance:
#             self.balance -= value
#             account.deposit(value)
#             return True
#         else:
#             return False
#
#     def printBalance(self):
#         print(f'\n'
#               f'Número da conta: {self.number} \n'
#               f'Titular: {self.owner} \n'
#               f'Cpf: {self.cpf} \n'
#               f'Saldo: R${self.balance:.2f} \n'
#         )
#
#
# def main():
#     conta_001 = Conta(101, 'Marluzi', '000.000.000-00')
#     conta_002 = Conta(202, 'Dalustre', '111.111.111-11')
#
#     conta_001.deposit(3000)
#     conta_001.transfer(1200, conta_002)
#     conta_001.draw(500)
#
#     conta_001.printBalance()
#     conta_002.printBalance()
#
#
# if __name__ == '__main__':
#     main()

# class Conta:
#     def __init__(self, number, owner, cpf):
#         self.number = number
#         self.owner = owner
#         self.cpf = cpf
#         self.balance = 0
#
#     def deposit(self, value):
#         if value > 0:
#             self.balance += value
#             return True
#         else:
#             return False
#
#     def printBalance(self):
#         print(f'\n'
#               f'Número da conta: {self.number} \n'
#               f'Titular {self.owner} \n'
#               f'Cpf: {self.cpf} \n'
#               f'Saldo: {self.balance:.2f} \n'
#         )
#
# def main():
#     c1 = Conta(101, 'Marluzi', '000.000.000-00')
#     c2 = c1
#     c2.deposit(200)
#     c1.printBalance()
#     print(c1)
#     print(c2)
#
# if __name__ == '__main__':
#     main()


# class Conta:
#     def __init__(self, number, owner, cpf):
#         self.number = number
#         self.owner = owner
#         self.cpf = cpf
#         self.balance = 0
#
#     # def deposit(self, value):
#         if value > 0:
#             self.balance += value
#             return True
#         else:
#             return False
#
#     def draw(self, value):
#         if value <= self.balance and value > 0:
#             self.balance -= value
#             return True
#         else:
#             return False
#     def printBalance(self):
#         print(f'Número da conta: {self.number} \n'
#               f'Titular: {self.owner} \n'
#               f'Cpf: {self.cpf} \n'
#               f'Saldo: {self.balance:.2f} \n'
#         )
#
# def main():
#     c1 = Conta(101, 'Marluzi', '000.000.000-00')
#     c1.deposit(100)
#     c1.draw(75)
#     c1.printBalance()
#
#
# if __name__ == '__main__':
#     main()

# class Conta:
#     def __init__(self, number, name, cpf):
#         self.number = number
#         self.name = name
#         self.cpf = cpf
#         self.balance = 0
#
#     def deposit(self, value):
#         if value >= 0:
#             self.balance += value
#         else:
#             return
#
# def main():
#     c1 = Conta(101, 'Marluzi', '000.000.000-000')
#     c1.deposit(50.50)
#     print(f'Conta: {str(c1.number).zfill(5)}')
#     print(f'{c1.name}')
#     print(f'{c1.cpf}')
#     print(f'Saldo: R${c1.balance:.2f}')
#
# if __name__ == '__main__':
#     main()

# class A:
#     def f(self):
#         print('foo')
#
# def main():
#     obj_A = A()
#     obj_A.f()
#
# if __name__ == '__main__':
#     main()

# class Conta:
#     def __init__(self, number, cpf, name, balance):
#         self.number = number
#         self.cpf = cpf
#         self.name = name
#         self.balance = balance
#
# def main():
#     c1 = Conta(101, '000.000.000-00', 'Marluzi', 500)
#     print(f'Conta: {str(c1.number).zfill(5)}')
#     print(f'{c1.name}')
#     print(f'{c1.cpf}')
#     print(f'Saldo: R${c1.balance:.2f}')
#
# main()

# class Conta:
#     pass
