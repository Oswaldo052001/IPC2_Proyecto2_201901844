from Lista_Simple import ListaSimple


class Dron():

    def __init__(self,alturasMax):
        self.nombre = None
        self.alturasmax = alturasMax
        self.posicion = 0
        self.ListaAlutras = ListaSimple()
        self.ListaInstrucciones = ListaSimple()
        self.ListaMovimientos = ListaSimple()

    def getNombreDron(self):
        return self.nombre
    
    def setNombreDron(self,name):
        self.nombre = name
    
    def getPosicionDron(self):
        return self.posicion
    
    def setPosicionDron(self,posi):
        self.posicion = posi
    
    def agregarInstruccion(self):
        pass

    def agregarMovimiento(self):
        pass
    
    def asignaciondeAlturas(self):
        for i in range (1, int(self.alturasmax)+1):          #Creando la lista de tiempos hasta tiempo maximo
            pass


