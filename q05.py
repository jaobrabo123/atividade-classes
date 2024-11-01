class Conta():
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome
        self.saldo = 0
    def alterarNome(self, novoNome):
        self.nome = novoNome
    def deposito(self, dep):
        self.saldo += dep
    def saque(self, saq):
        self.saldo -=saq

pessoa1 = Conta(12345678, 'Joao')

print(pessoa1.nome)
print(pessoa1.numero)

pessoa1.deposito(500)

print(pessoa1.saldo)

pessoa1.saque(300)

print(pessoa1.saldo)

pessoa1.alterarNome('Alec')

print(pessoa1.nome)