

class Pessoa:
#estrtura da questão
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)
    def engordar(self, ganho_peso):
        self.peso += ganho_peso
    def emagrecer(self, perda_peso):
        self.peso -= perda_peso
    def crescer(self, aumento_altura):
        self.altura += aumento_altura
#comando da questão
pessoa = Pessoa(nome="João Azevedo", idade=16, peso=63, altura=1.75)


for _ in range(3):
    pessoa.envelhecer()

print("João Azevedo terá")
print("Idade:", pessoa.idade)
print("Altura:", pessoa.altura)

pessoa.engordar(5)
print("Peso após engordar:", pessoa.peso)
pessoa.emagrecer(2)
print("Peso após emagrecer:", pessoa.peso)