
class Instruccion():

    def __init__(self,nombreDron,posicion):
        self.nombreDron = nombreDron
        self.posicion = posicion
       
    def getNombreDron(self):
        return self.nombreDron
    
    def getPosicion(self):
        return self.posicion
