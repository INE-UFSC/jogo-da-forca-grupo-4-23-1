from random import randint

class Forca:
    def __init__(self, lista: list()):
        self.palavra = self.definir_palavra(lista)           #palavra a ser sorteada
        self.lista_palavra = list(self.palavra)         #lista que contém como elemento as letras da palavra
        self.lista_tracos = ["_"] * len(self.palavra)   #lista de traços
        self.chute = ""                                 #declarei a variavel do chute
        self.lista_chutes = []                          #lista de chutes que vao ser chutado(ela tem o append na funçao 'input_chute()'
        self.credito = 6                                #creditos


    def definir_palavra(self, lista: []):
        #lista = ["carro", "melancia", "escola", "elefante", "elevador", "alface", "computador", "telefone", "apartamento", "bermuda"]

        return lista[randint(0, (len(lista)-1))]

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
            if not (self.chute in self.lista_palavra):
                self.credito -= 1

            self.lista_chutes.append(self.chute)

            return False
        
        
    def imprime_palavra(self): # imprime a palavra 
        str_palavra = ''
        contador_letras_palavra = 0
        for elemento in self.lista_tracos:
            if(contador_letras_palavra != len(self.lista_tracos)-1):
                str_palavra += elemento + ' '
            else:
                str_palavra += elemento

            contador_letras_palavra += 1
        return str_palavra
    

    def atualiza_lista_tracos(self): #atualiza a lista que contem os tracos, colocando no lugar a letra chutada pelo jogador, caso ela exista na palavra
        lista_palavra_copy = self.lista_palavra.copy()

        contador_letras_palavra = 0
        for letra in self.lista_palavra:
            if letra == self.chute:
                lista_palavra_copy.remove(self.chute)
                self.lista_tracos[contador_letras_palavra] = self.chute
            contador_letras_palavra += 1

        return self.lista_tracos
    
    def verifica_lista_tracos(self): # Retorna falso caso ainda exista letra nao descoberta, e verdadeiro caso o jogador tenha descoberto todas as letras da palavra
        for elemento in self.lista_tracos:
            if(elemento == '_'):
                return False
        return True
        




    
    

