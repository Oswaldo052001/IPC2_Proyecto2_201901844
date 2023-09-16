from Lista_Simple import ListaSimple

class Sistema():

    def __init__(self,nombre,AlturaMax,CantidadDrones):
        self.nombre = nombre
        self.alturamax = AlturaMax
        self.cantidadDrones = CantidadDrones
        self.listaDrones = ListaSimple()

    def getNombre(self):
        return self.nombre
    
    def getalturaMax(self):
        return self.alturamax

    def getCantidadDrones(self):
        return self.cantidadDrones
    
    def CrearListaAlturas(self):
        for i in range (1, int(self.cantidadDrones)+1):          #Creando la lista de tiempos hasta tiempo maximo
            pass
            #objAltura  = Tiempo(i, self.alturamax)       #Creando los objetos tiempos
            #self.listaDrones.agregarFinal(objTiempo)       #Insertando los objetos a la lista de tiempos
    

