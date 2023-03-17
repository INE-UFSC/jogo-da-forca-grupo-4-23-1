from ControladorLista import ControladorLista
from Lista import Lista
from jogo_forca import Jogo
import os
class Sistema:
     def __init__(self):
          self._controlador = ControladorLista([Lista('frutas', ['banana', 'goiaba']), Lista('esportes', ['futebol', 'basquete'])])
          self._running = True
    
     #def jogo(self):
          #self.consultar_palavras() retorna a lista de palavras possiveis dado o nome da lista de palavras


     def inserir_lista(self):
          nome_lista = input('Informe o nome da lista de palavras: ')
          lista_palavras = [str(x) for x in input('Informe as palavras que serão adicionadas à lista (em uma unica linha): ').split()]
          nova_lista = Lista(nome_lista, lista_palavras)
          self._controlador.inserir(nova_lista)
    
     def atualizar_lista(self):
          nome = self.verifica_existencia_lista()
          novo_nome = input('Informe o novo nome: ')
          nova_lista = [str(x) for x in input('Informe a nova lista de palavras: ').split()]
          self._controlador.atualizar(nome, novo_nome, nova_lista)

     def deletar_lista(self):
          nome = self.verifica_existencia_lista()
          self._controlador.deletar(nome)
    
     def consultar_listas(self):
          for _lista in self._controlador.consultar_listas():
               print(_lista)
     
     def consultar_palavras(self):
          nome = self.verifica_existencia_lista()
          os.system("cls")
          return self._controlador.consultar_palavras(nome)
     
     def verifica_existencia_lista(self):
          nome_valido = ''
          while nome_valido not in self._controlador.consultar_nomes():
               print("Tipo de listas disponíveis:")
               print(*self._controlador.consultar_nomes())
               print()
               nome_valido = input('Informe o nome da lista: ')
               if nome_valido not in self._controlador.consultar_nomes():
                    print('Erro! Não há nehuma lista com esse nome.')
          return nome_valido
        

     def run(self):

          while self._running:

               os.system('cls')
               
               opcao = 0

               print('\n1 - Jogar')
               print('2 - Inserir lista de palavras')
               print('3 - Atualizar lista de palavras')
               print('4 - Deletar lista de palavras')
               print('5 - Consultar listas de palavras')
               print('6 - Sair do programa')

               while True:
                         try:
                              opcao = int(input("\nInforme uma opcao: "))
                         except:
                              print('Erro! Informe uma opcao valida')

                         else:
                              if opcao < 1 or opcao > 6:
                                   print('Erro! Informe uma opcao valida')
                                   print()
                              else:
                                  break
               os.system('cls')
               
               if opcao == 1:
                    print('------Definindo o tipo da lista------------')
                    jogo = Jogo(self.consultar_palavras())

                               
               
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
                    
               input('Enter para continuar')
                 
        
Sistema().run()

