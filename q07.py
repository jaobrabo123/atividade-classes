class Macaco:
    def __init__(self, nome):  # Correção aqui
        self.nome = nome
        self.bucho = []
    def comer(self, comida):
        self.bucho.append(comida)
        print(f"{self.nome} comeu {comida}.")
    def verBucho(self):
        if self.bucho:
            return f"O bucho do {self.nome} contém:\n{', '.join(self.bucho)}."
        else:
            return f"O bucho do {self.nome} está vazio."
    def digerir(self, item):
        if item in self.bucho:
            self.bucho.remove(item)
            print(f"{self.nome} digeriu {item}.")
        else:
            print(f"{self.nome} não tem {item} no bucho.")


#comando da questão
macaco1 = Macaco("Macaco1")
macaco2 = Macaco("Macaco2")

for _ in range(3):
    comida = input(f"O que {macaco1.nome} deve comer?\n ")
    macaco1.comer(comida)
    print(macaco1.verBucho())

for _ in range(2):
    comida = input(f"O que {macaco2.nome} deve comer?\n ")
    macaco2.comer(comida)
    print(macaco2.verBucho())

macaco1.comer(macaco2.nome)
print(macaco1.verBucho())

item_digerir = input(f"O que {macaco1.nome} deve digerir?\n ")
macaco1.digerir(item_digerir)
print(macaco1.verBucho())