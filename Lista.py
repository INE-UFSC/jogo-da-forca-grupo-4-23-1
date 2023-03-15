class Lista:
    def __init__(self, nome, palavras = []):
        self.nome = nome
        self._palavras = palavras[:]
    
    def get_nome(self):
        return self.nome

    def get_palavras(self):
        return self._palavras
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def set_palavras(self, novas_palavras):
        self._palavras = novas_palavras[:]
    
    def __str__(self):
        return f'Lista: {self.nome}, Palavras: {self._palavras}'
