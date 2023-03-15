from classe_forca import Forca

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


