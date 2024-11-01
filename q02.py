class Quadrado:
#estrutura da questão
    def __init__(self, lado):
        self.lado = lado
    def mudar_lado(self, novo_lado):
        self.lado = novo_lado
    def retornar_lado(self):
        return self.lado
    def calcular_area(self):
        return self.lado ** 2
#comando da questão 
quadrado = Quadrado(6)
quadrado.mudar_lado(9)

print("Lado:", quadrado.retornar_lado())
print("Área:", quadrado.calcular_area())