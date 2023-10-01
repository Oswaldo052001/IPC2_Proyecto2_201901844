import xml.etree.cElementTree as ET


class Archivo():

    root = ET.Element("respuesta")
    listaMensajes = ET.SubElement(root, "listaMensajes")

    def __init__(self,sistemaenvaida = None, mensaje = None):
        self.mensaje = mensaje
        self.sistemaenvaida = sistemaenvaida
        


    def AgregarMensaje(self):

        nombremensaje = self.mensaje.getDato().getNombreMensaje()
        sistemarecibido = self.mensaje.getDato().getNombreSistema()
        tiemporecibido = self.mensaje.getDato().getTeimpoObtimo()
        mensajerecibido = self.mensaje.getDato().getMensajedecifrado()

        mensaje = ET.SubElement(self.listaMensajes, "mensaje", nombre = nombremensaje)
        
        sistema = ET.SubElement(mensaje, "sistemaDrones")
        sistema.text = sistemarecibido

        tiempo = ET.SubElement(mensaje, "tiempoOptimo")
        tiempo.text = str(tiemporecibido)

        decifrado = ET.SubElement(mensaje, "mensajeRecibido")
        decifrado.text = str(mensajerecibido)


        instrucciones = ET.SubElement(mensaje, "instrucciones")
        self.agregarInstrucciones(instrucciones,int(tiemporecibido))


    def agregarInstrucciones(self,cabeza,tiempo):  # Esta funcion recibira un tabla de grupos y la convertirá a xml

        for i in range(1,tiempo+1):
            tiempoinstruccion = ET.SubElement(cabeza, "tiempo", valor = str(i))
            acciones = ET.SubElement(tiempoinstruccion, "acciones")
            dron = self.sistemaenvaida.listaDrones.getInicio()   # Variable que almacena la lista de Tiempos
            
            while dron:
                nombredron = ET.SubElement(acciones, "dron",nombre=dron.getDato().getNombreDron())
                movimientos = dron.getDato().ListaMovimientos.getInicio()
                while movimientos:
                    if i == movimientos.getDato().getTiempo():
                        nombredron.text = movimientos.getDato().getMovimiento()
                    movimientos = movimientos.getSiguiente()
                dron = dron.getSiguiente()


    def crearArchivo(self):
        arbol = ET.ElementTree(self.root)
        ET.indent(arbol, space="\t", level=0)  # Esta linea de codigo ordena la estructura del archivo xml
        arbol.write("mensajesrecibidos.xml", encoding='utf-8', xml_declaration=True)



