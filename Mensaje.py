from Lista_Simple import ListaSimple

class MensajeS():

    def __init__(self,nombre,nombresistema):
        self.nombre = nombre
        self.nombresistema = nombresistema
        self.tiempoOptimo = 0
        self.mensajedecifrado = ""
        self.listaInstrucciones = ListaSimple()

    def getNombreMensaje(self):
        return self.nombre
    
    def getNombreSistema(self):
        return self.nombresistema
    
    def getTeimpoObtimo(self):
        return self.tiempoOptimo
    
    def setTiemnpoOptimo(self,tiempo):
        self.tiempoOptimo = tiempo

    def getMensajedecifrado(self):
        return self.mensajedecifrado
    
    def setMensajedecifrado(self,mensaje):
        self.mensajedecifrado = mensaje

