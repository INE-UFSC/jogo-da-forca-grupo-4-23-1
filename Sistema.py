from ControladorLista import ControladorLista
from Lista import Lista
class Sistema:
    def __init__(self):
        self._controlador = ControladorLista([Lista('frutas', ['banana', 'goiaba']), Lista('esportes', ['futebol', 'basquete'])])
        self._running = True
    
    #def jogo(self):


    def inserir_lista(self):
         nome_lista = input('Informe o nome da lista de palavras: ')
         lista_palavras = [str(x) for x in input('Informe as palavras que serão adicionadas à lista: ').split()]
         nova_lista = Lista(nome_lista, lista_palavras)
         self._controlador.inserir(nova_lista)
    
    def atualizar_lista(self):
         nome = input('Informe o nome da lista a ser atualizada: ')
         novo_nome = input('Informe o novo nome: ')
         nova_lista = [str(x) for x in input('Informe a nova lista de palavras: ').split()]
         self._controlador.atualizar(nome, novo_nome, nova_lista)

    def deletar_lista(self):
         nome = input('Informe o nome da lista a ser deletada: ')
         self._controlador.deletar(nome)
    
    def consultar_listas(self):
         for _lista in self._controlador.consultar():
              print(_lista)

    def run(self):

        while self._running:
            
            opcao = 0

            print('\n1 - Jogar')
            print('2 - Inserir lista de palavras')
            print('3 - Atualizar lista de palavras')
            print('4 - Deletar lista de palavras')
            print('5 - Consultar listas de palavras')
            print('6 - Sair do programa')

            while opcao < 1 or opcao > 6:
                    opcao = int(input("\nInforme uma opcao: "))
                    if opcao < 1 or opcao > 6:
                        print('Erro! Informe uma opcao valida')
                    print()
            
            if opcao == 1:
                 print('.')
            
            elif opcao == 2:
                 self.inserir_lista()
                 
            elif opcao == 3:
                 self.atualizar_lista()
                 
            elif opcao == 4:
                 self.deletar_lista()
            
            elif opcao == 5:
                 self.consultar_listas()
            
            else:
                 print('Fim do programa')
                 self._running = False
                 
                 
        
Sistema().run()

