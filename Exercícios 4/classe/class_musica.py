class musica():
    def __init__(self, nome, artista, duraçao):
        self.duraçao = duraçao
        self.artista = artista
        self.nome = nome

        
    def info(self):
        print(f'nome:{self.nome}, artista:{self.artista},duração:{self.duraçao}')

musica('mamute', 'sobrenatural', 8.25).info()
