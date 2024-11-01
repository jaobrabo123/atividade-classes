class Bola():
    def __init__(self, cor, circun, mat):
        self.cor = cor
        self.circun = circun
        self.mat = mat

    def trocaCor(self, novaCor):
        self.cor = novaCor

    def mostraCor(self):
        print(f"A cor da bola é {self.cor}.")

bola = Bola("Verde", 20, "Madeira")

bola.trocaCor("Azul")

bola.mostraCor()