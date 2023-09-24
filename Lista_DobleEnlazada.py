from Nodo import NodoD

class Lista_doble():
    id = 0

    def __init__(self):
        self.nodoInicio = None
        self.nodoFin = None
        self.nodoubicacion = None
        self.size = 0

    def getInicio(self):
        return self.nodoInicio
    
    def getFin(self):
        return self.nodoFin
    
    def getPosicion(self):
        return self.nodoubicacion
    
    def setPosicion(self,nodonuevo):
        self.nodoubicacion = nodonuevo

    def AgregarInicio(self,Dato):
        if self.nodoInicio is None:
            self.nodoInicio = NodoD(dato=Dato,id=self.id)
            self.nodoFin = self.nodoInicio
        else:     
            nuevo = NodoD(dato = Dato, id=self.id )
            self.id += 1
            nuevo.setSiguiente(self.nodoInicio)
            self.nodoInicio.setAnterior(nuevo)
            self.nodoInicio = nuevo
        self.size += 1

    
    def AgregarFinal(self,Dato):
        if self.nodoInicio is None:
            nuevo = NodoD(dato=Dato,id=self.id)
            self.nodoFin = nuevo
            self.nodoInicio = nuevo
            #self.nodoubicacion = nuevo
        else:     
            nuevo = NodoD(dato = Dato, id=self.id )
            self.id += 1
            nuevo.setAnterior(self.nodoFin)
            self.nodoFin.setSiguiente(nuevo)
            self.nodoFin = nuevo
        self.size += 1
        

    def imprimir_Adelante_atras(self):
        tmp = self.nodoInicio
        while tmp != None:
            print(tmp.getDato())
            tmp = tmp.getSiguiente()


    def imprimir_Atras_adelante(self):
        tmp = self.nodoFin
        while tmp != None:
            print(tmp.getDato())
            tmp = tmp.getAnterior()
