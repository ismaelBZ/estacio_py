# from ContaPolimorfismo import ContaCliente, ContaComum, ContaRemunerada
# class Banco():
#     def __init__(self, code, name):
#         self.code = code
#         self.name = name
#         self.accounts = []
#
#     def add_account(self, account):
#         self.accounts.append(account)
#
#     def calculate_return_mensal(self):
#         for account in self.accounts:
#             account.calculate_yield()
#
#     def print_balance_all_accounts(self):
#         for account in self.accounts:
#             print(f'n0: {account.number:4d} \t Rendimento: {account.investment_value:8.2f} \t {account.account_type:20s} ')
#
#
# def main():
#     bancoLS = Banco(999, 'Los Santos Bank')
#     contaComum = ContaComum(202, 0.01, 0.1, 1000, 0.05)
#     contaRemunerada = ContaRemunerada(303, 0.01, 0.1, 1000, 0.05)
#
#     contaComum.extract()
#
#     bancoLS.add_account(contaComum)
#     bancoLS.add_account(contaRemunerada)
#
#     bancoLS.calculate_return_mensal()
#     bancoLS.print_balance_all_accounts()
#
# main()



# class Argentina:
#     def capital(self):
#         print('A capital da Argentina é Buenos Aires')
#     def lingua_oficial(self):
#         print('A lingua oficial do país é Espanhol')
# class Brasil:
#     def capital(self):
#         print('A capital da Brasil é Brasilia')
#     def lingua_oficial(self):
#         print('A lingua oficial do país é Portugues')
#
# arg = Argentina()
# br = Brasil()
# for pais in (arg, br):
#     print()
#     pais.capital()
#     pais.lingua_oficial()

