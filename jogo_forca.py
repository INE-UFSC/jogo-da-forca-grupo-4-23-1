from os import system
from classe_forca import Forca


class Jogo:
    def __init__(self, lista: list()):
        self.lista = lista
        jogo = Forca(lista)
        v = False


        while True:
            
            #verifica credito
            if (jogo.credito <= 0):
                v = False
                break


            
            
            
            #printando dados
            print("-> Créditos........: ", jogo.credito)
            print("-> Letras chutadas.: ", *jogo.lista_chutes)
            print()
            print(jogo.imprime_palavra())


            #Chute    
            jogo.input_chute()

            #verificando chute
            if (not jogo.verifica_chute()):
                jogo.atualiza_lista_tracos()

            print() 
            print("Enter para continuar")
            system('cls')
            
            #Verifica lista traços
            if (jogo.verifica_lista_tracos()):
                v = True
                break

        print("A palavra era: ", jogo.palavra)

        if v:
            print("Voce ganhou!!!")
        else:
            print("Voce perdeu!!!")

            
                

                        



