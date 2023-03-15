from random import randint

class Forca:
    def __init__(self):
        self.palavra = self.definir_palavra()           #palavra a ser sorteada 
        self.lista_tracos = ["_"] * len(self.palavra)   #lista de traços
        self.chute = ""                                 #declarei a variavel do chute
        self.lista_chutes = []                          #lista de chutes que vao ser chutado(ela tem o append na funçao 'input_chute()'
        self.credito = 6                                #creditos


    def definir_palavra(self):
        lista = ["carro", "melancia", "escola", "elefante", "elevador", "alface", "computador", "telefone", "apartamento", "bermuda"]
        return lista[randint(0, 9)]

    def input_chute(self):
        while True:
            chute = input("Digite o chute: ").strip()
            try:
                chute = int(chute)
            except:
                if (len(chute) != 1):
                    print("ERROR: Digite somemte uma LETRA")
                else:
                    self.chute = chute
                    break
            else:
                print("ERROR: Digite somemte uma LETRA")
                
    def verifica_chute(self): # return True se já chutou, se n return false e tira um do credito
        if (self.chute in self.lista_chutes):
            self.credito -= 1
            return True
        else:
            self.lista_chutes.append(self.chute)
            return False
    
    

