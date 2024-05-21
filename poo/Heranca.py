### ORDEM DE PRIORIDADES | ORDEM DE PRIORIDADES | ORDEM DE PRIORIDADES |
# class FirstClass:
#
#     def __init__(self, param1, param2):
#         self.param1 = param1
#         self.param2 = param2
#
#     def printOrder(self):
#         print(f'Printing params from first class {self.param1} {self.param2}')
#
# class SecondClass:
#
#     def __init__(self, param3, param4):
#         self.param3 = param3
#         self.param4 = param4
#
#     def printParams(self):
#         print(f'Print params from second class {self.param3} {self.param4}')
#
# class conclusionClass(FirstClass, SecondClass):
#     def __init__(self, param1, param2, param3, param4):
#         FirstClass.__init__(self, param1, param2)
#         SecondClass.__init__(self, param3, param4)

##--## The order of declaration params in __init__ not interfere


# class FirstClass:
#     def printOrder(self):
#         print(f'The priority is for de first class')
#
# class SecondClass:
#     def printOrder(self):
#         print(f'The priority is for de second class')
#
# class conclusionClass(SecondClass, FirstClass):
#     def __init__(self):
#         FirstClass.__init__(self)
#         SecondClass.__init__(self)
#
# def main():
#     conclusion = conclusionClass()
#     conclusion.printOrder()
#
# main()
##--## The order of params in class declaration not interfere
##--## indicate the methods order of precedence


# from ContaHeranca import Conta, Client
# import datetime
#
# class ContaEspecial(Conta):
#
#     def __init__(self, number, clients, balance=0, limit=1000):
#         Conta.__init__(self, number, clients, balance)
#         self.limit = limit
#
#     def draw(self, value):
#         if value <= self.balance + self.limit:
#             self.balance -= value
#             self.statement.history.append(['Saque:', value, 'Data:', datetime.datetime.now()])
# def main():
#     print(issubclass(ContaEspecial, Conta))
#     client1 = Client('Marluzi', '000.000.000-00')
#     c1 = ContaEspecial(101, client1)
#     c1.deposit(5000)
#     c1.draw(2000)
#     c1.draw(2500)
#     c1.draw(800)
#     c1.draw(500)
#     c1.draw(500)
#     c1.draw(500)
#     c1.draw(500)
#     c1.draw(500)
#     c1.get_statement()
#
# main()