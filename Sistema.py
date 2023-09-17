from Lista_Simple import ListaSimple
from Dron import Dron

class Sistema():

    def __init__(self,nombre,AlturaMax,CantidadDrones):
        self.nombre = nombre
        self.alturamax = AlturaMax
        self.cantidadDrones = CantidadDrones
        self.listaDrones = ListaSimple()
        self.CrearListaAlturas()
        #self.imprimir()

    def getNombre(self):
        return self.nombre
    
    def getalturaMax(self):
        return self.alturamax

    def getCantidadDrones(self):
        return self.cantidadDrones
    
    def CrearListaAlturas(self):
        for i in range (1, int(self.cantidadDrones)+1):          #Creando la lista de tiempos hasta tiempo maximo
            objdron = Dron(i,self.alturamax)            #Creando los objeto dron
            self.listaDrones.agregarFinal(objdron)               #Insertando el objeto a la lista de Drones

    def imprimir(self):
        print("_____Drones para sistema: ", self.getNombre(), "________")
        ObjDron = self.listaDrones.getInicio()

        while ObjDron != None:
            print(ObjDron.getDato().getnumerodron())
            ObjDron = ObjDron.getSiguiente()