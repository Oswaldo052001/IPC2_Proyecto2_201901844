from Lista_Simple import ListaSimple

class Cola(ListaSimple):

    def enconlar(self, dato):
        ListaSimple.ordenarAlfabeticamente(self, dato)

    def encolarDesorden(self, dato):
        ListaSimple.agregarFinal(self, dato)
        
    def desencolar(self):
        ListaSimple.eliminarInicio(self)
