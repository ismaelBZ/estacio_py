class End_simples(object):
    def __init__(self, rua, num, bairro):
        self.rua = rua
        self.num = num
        self.bairro = bairro

    def Endereco(self):
        return self.rua + ", " + self.num + " " + self.bairro

class End_com(End_simples):
    def __init__(self, rua, num, bairro, complemento):
        End_simples.__init__(self, rua, num, bairro)
        self.complemento = complemento

    def Endereco(self):
        return super(End_com, self).Endereco() + ", " + self.complemento

a = End_simples("Av Brasil", "243", "Floresta")
b = End_com("Av Miracema", "12", "Centro", "apto 3")

print(a.Endereco())
print(b.Endereco())






