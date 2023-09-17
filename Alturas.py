

class Alturas():

    def __init__(self, altura):
            self.altura = altura
            self.valor = None
            #self.imprimir()

    def getAltura(self):
        return self.altura
    
    def getValor(self):
        return self.valor
    
    def setValor(self,valor):
        self.valor = valor
    
    def imprimir(self):
        print(self.altura, self.valor)