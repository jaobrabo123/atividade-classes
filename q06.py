class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 10

    def mudar_canal(self):
        novo_canal = int(input("Digite o número do canal (1-100): "))
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
            print(f"Canal alterado para: {self.canal}")
        else:
            print("Número de canal inválido, inexistente, não existe, porque escolheu esse canal?. Escolha entre 1 e 100.")
    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume: {self.volume}")
        else:
            print("Volume já está no máximo.")
    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume: {self.volume}")
        else:
            print("Volume já está no mínimo.")

# Comando para teste
tv = TV()

while True:
    print("\nEscolha uma opção:")
    print("1. Mudar Canal")
    print("2. Aumentar Volume")
    print("3. Diminuir Volume")
    print("4. Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        tv.mudar_canal()
    elif opcao == "2":
        tv.aumentar_volume()
    elif opcao == "3":
        tv.diminuir_volume()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")