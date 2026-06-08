class Pessoa:
    def __init__(self, nome, idade):
        self._idade = idade  # atributo "protegido"

    @property
    def idade(self):
        return self._idade

    def nameida(self):
        print(self.idade)
Pessoa.idade(25)