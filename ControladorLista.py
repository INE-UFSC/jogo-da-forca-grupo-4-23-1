from Lista import Lista
class ControladorLista:

    def __init__(self, listas = []):
        self._listas = listas [:]

    def inserir(self, lista = []):
        self._listas.append(lista)

    
    def atualizar(self, nome, novo_nome, lista = []):
        for _lista in self._listas:
            if _lista.get_nome() == nome:
                _lista.set_nome(novo_nome)
                _lista.set_palavras(lista)
        
    def consultar(self):
        return self._listas[:]
    
    def deletar(self, nome):
        for _lista in self._listas:
            if _lista.get_nome() == nome:
        
                self._listas.remove(_lista)
