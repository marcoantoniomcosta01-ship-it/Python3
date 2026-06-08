from veiculo import veiculo

class carro(veiculo):
    def __init__(self, marca, modelo, porta):
        super().__init__(marca, modelo)
        self.porta = porta

    def __str__(self):
        return f'{super().__str__()} - Portas: {self.porta}'