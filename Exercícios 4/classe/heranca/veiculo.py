class veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.atributo = 'Desligado'
    def __str__(self):
        return f'{self.marca} {self.modelo} - {self.atributo}'
    