from abc import ABC, abstractmethod
from ContaHeranca import Conta

class ContaCliente(ABC):

    def __init__(self, number, IOF, IR, investment_value, yield_rate, balance):
        self.number = number
        self.balance = balance
        self.iof = IOF
        self.ir = IR
        self.investment_value = investment_value
        self.yield_rate = yield_rate

    @abstractmethod
    def calculate_yield(self):
        pass

    def extract(self):
        print(f'O saldo atual da conta {self.number} é {self.investment_value:10.2f}')


class ContaComum(ContaCliente):
    def __init__(self, number, IOF, IR, investment_value, yield_rate, balance=0):
        super().__init__(number, IOF, IR, investment_value, yield_rate, balance)
        self.account_type = 'Conta Comum'

    def calculate_yield(self):
        self.investment_value += self.investment_value * self.yield_rate


class ContaRemunerada(ContaCliente):
    def __init__(self, number, IOF, IR, investment_value, yield_rate, balance=0):
        super().__init__(number, IOF, IR, investment_value, yield_rate, balance)
        self.account_type = 'Conta Remunerada'

    def calculate_yield(self):
        self.investment_value += self.investment_value * self.yield_rate
        self.investment_value -= self.investment_value * self.iof


