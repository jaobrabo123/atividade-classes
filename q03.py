class Retangulo():
    def __init__(self,lado1,lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    def mudarValores(self, novo1, novo2):
        self.lado1 = novo1
        self.lado2 = novo2
    def valores(self):
        print(f'Comprimento: {self.lado1}; Largura: {self.lado2}')
    def area(self):
        area = self.lado1 * self.lado2
        return area
    def perimetro(self):
        perimetro = 2*self.lado1 + 2*self.lado2
        return perimetro

comprimento = float(input('Digite o comprimento do espaço em metros: '))
largura = float(input('Digite o largura do espaço em metros: '))
piso = float(input('Digite o tamanho do piso em metros quadrados: '))

espaco = Retangulo(comprimento, largura)

print(f'Você precisará de {espaco.area()/piso} pisos e {espaco.perimetro()} metros de rodapé.')