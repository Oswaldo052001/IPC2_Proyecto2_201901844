from Lista_Simple import ListaSimple
from Lista_DobleEnlazada import Lista_doble
from Alturas import Alturas
from Cola import Cola

class Dron():

    def __init__(self,numero,alturasMax):
        self.numerodron = numero
        self.nombre = None
        self.posicion = 0
        self.alturasmax = alturasMax
        self.ListaAlturas = Lista_doble()
        self.ListaInstrucciones = Cola()
        self.ListaMovimientos = Cola()
        self.asignaciondeAlturas()
        #self.imprimir()

    def getnumerodron(self):
        return self.numerodron
    
    def getNombreDron(self):
        return self.nombre
    
    def setNombreDron(self,name):
        self.nombre = name

    def getposicion(self):
        return self.posicion
    
    def setposicion(self,pos):
        self.posicion = pos
    
    def agregarInstruccion(self):
        pass

    def agregarMovimiento(self):
        pass
    
    def asignaciondeAlturas(self):
        for i in range (1, int(self.alturasmax)+1):          #Creando la lista de tiempos hasta tiempo maximo
            objaltura = Alturas(i)            #Creando los objeto dron
            self.ListaAlturas.AgregarFinal(objaltura)               #Insertando el objeto a la lista de Drones


    def imprimir(self):
        print("_____Alturas para dron: ", self.getnumerodron(), "________")
        ojbAlturas = self.ListaAlturas.getInicio()

        while ojbAlturas != None:
            print(ojbAlturas.getDato().getAltura())
            ojbAlturas = ojbAlturas.getSiguiente()


