import xml.etree.ElementTree as ET
from Lista_Simple import ListaSimple
from Cola import Cola

class xml():

    def __init__(self,ruta):
        self.Inventario_drones = Cola()
        self.listSistema_drones = ListaSimple()
        self.Ilist_mensajes = ListaSimple()
        self.archivo = ET.parse(ruta).getroot()
        self.Leerinventario()
        #self.LeerMensajes()
        #self.LeerSistemaDrones()
    

    def Leerinventario(self):

        for inventario in self.archivo.findall('listaDrones'):    # este for va a recorer todo el listado de drones que esten en el doc
            for nombreDron in inventario.findall('dron'):
                print(nombreDron.text)
                self.Inventario_drones.enconlar(nombreDron.text)
                
    
    def LeerSistemaDrones(self):
        for ListSistemaDrones in self.archivo.findall('listaSistemasDrones'):    # este for va a recorer todo el listado de Sistema que esten en el doc
            for sistemaDrones in ListSistemaDrones.findall('sistemaDrones'):
                nombre = sistemaDrones.get("nombre")
                alturamax = sistemaDrones.find('alturaMaxima').text
                cantidadDrons = sistemaDrones.find('cantidadDrones').text
                
                print("Nombre:",nombre)
                print("Altura maxima:",alturamax)
                print("Cantidad de drones:",cantidadDrons)

                contenido = sistemaDrones.find('contenido')
                alturas = contenido.find('alturas')
                
                for altura in alturas.findall('altura'):
                    Altura = altura.get('valor')
                    letra = altura.text
                    print(Altura,letra)


    def LeerMensajes(self):
        for Listmensajes in self.archivo.findall('listaMensajes'):    # este for va a recorer todo el listado de mensajes que esten en el doc
            for mensaje in Listmensajes.findall('Mensaje'):
                nombre = mensaje.get("nombre")
                nombreSistema = mensaje.find('sistemaDrones').text
                Instrucciones = mensaje.find('instrucciones')
                                
                print ("Nombre:",nombre)
                print("Sistema de Drones a usar:",nombreSistema)

                for instruccion in Instrucciones.findall('instruccion'):
                    dron = instruccion.get("dron")
                    posicion = instruccion.text
                    print (dron,posicion)
        

    

objeto = xml("archivo1.xml")
#objeto.getSenal()
