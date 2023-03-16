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

            
                

                        

"""
jogo = Forca()
v = False

while True:
    #verifica lista de traços
    '''if ("_" not in jogo.lista_tracos):
        v = True
        break'''

    
    #verifica credito

    #printa 'lista_tracos", 'credito', e a lista_chutes

    #input do chute
    jogo.input_chute() 

    #verifica letras_repitidas
    #se ja tiver chuteado-> diminui o credito e retorna True
    #se n tiver chuteado -> return false e adiciona na lista self.lista_chutes
            

    #verifica imput (ver foto no grupo do esquema)




if v:
    print("Voce ganhou")
else:
    print("voce perdeu")
"""


