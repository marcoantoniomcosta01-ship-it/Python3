class Carro():
    def __init__(self, cor=input('Cor: '), modelo=input("Modelo: "), ano=input('Ano: ')):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def saida(self):
        print(f'Cor: {self.cor} | modelo: {self.modelo} | ano: {self.ano}')


Carro().saida()
