from Lista_Simple import ListaSimple

class MensajeS():

    def __init__(self,nombre,nombresistema):
        self.nombre = nombre
        self.nombresistema = nombresistema
        self.listaInstrucciones = ListaSimple()

    def getNombreMensaje(self):
        return self.nombre
    
    def getNombreSistema(self):
        return self.nombresistema

