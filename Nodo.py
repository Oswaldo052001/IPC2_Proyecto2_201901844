
class Nodo():
    def __init__(self,id, dato):
        self.id = id
        self.dato = dato
        self.siguiente = None

    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id

    def getDato(self):
        return self.dato
    
    def setDato(self, dato):
        self.dato = dato

    def getSiguiente(self):
        return self.siguiente
    
    def setSiguiente(self, siguiente):
        self.siguiente = siguiente


class NodoD():
    def __init__(self,dato, id, siguiente = None, anterior = None):
        self.id = id
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id

    def getDato(self):
        return self.dato
    
    def setDato(self, dato):
        self.dato = dato

    def getSiguiente(self):
        return self.siguiente
    
    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def getAnterior(self):
        return self.anterior
    
    def setAnterior(self, anterior):
        self.anterior = anterior