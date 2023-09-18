from Lista_Simple import ListaSimple

class Cola(ListaSimple):

    def enconlar(self, dato):
        ListaSimple.agregarEnOrden(self, dato)

    def desencolar(self):
        ListaSimple.eliminarFinal(self)
