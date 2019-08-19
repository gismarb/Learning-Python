class Jogo:
    def lanca(self, dado1, dado2):
        self.dado1 = dado1
        self.dado2 = dado2
    
    def getResultado(self):
        self.resultado = int(self.dado1) + int(self.dado2)
        if (self.resultado == 7):
            print("")