class Veiculo:
    def __init__(self, nome, velocidade_maxima, consumo_kpl):
        self.nome = nome
        self.velocidade_maxima = velocidade_maxima
        self.consumo_kpl = consumo_kpl

    def toStr(self):
        print(f'\nVeículo: {self.nome} \n'
              f'Consumo: {self.consumo_kpl}km/l \n'
              f'Velocidade Máxima: {self.velocidade_maxima}km/h')

class Onibus(Veiculo):
    pass
    def __init__(self, nome, velocidade_maxima, consumo_kpl, quantidade_de_assentos = 70):
        super().__init__(nome, velocidade_maxima, consumo_kpl)
        self.quantidade_de_assentos = quantidade_de_assentos

    def toStr(self):
        super().toStr()
        print(f'Quantidade de assentos: {self.quantidade_de_assentos}')

fusca = Veiculo('Fusca', 120, 6)
fusca.toStr()

diplomata = Onibus('Nelson Diplomata 380', 160, 0.7)
diplomata.toStr()