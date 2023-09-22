import xml.etree.ElementTree as ET
from Lista_Simple import ListaSimple
from Sistema import Sistema
from Inventario import Cola
from Mensaje import MensajeS
from Instruccion import Instruccion
from Graph import Graph

class xml():
    Inventario_drones = Cola()
    listSistemas = ListaSimple()
    Ilist_mensajes = ListaSimple()
    
    def __init__(self,ruta):
        self.archivo = ET.parse(ruta).getroot()
        self.Leerinventario()
        self.LeerSistemaDrones()
        self.LeerMensajes()
        self.prueba()
        #self.comprobar()
    

    def prueba(self):
        sistema = self.listSistemas.getInicio().getDato()
        grafica = Graph(sistema,"prueba")
        grafica.crearGraficaOriginal()


    def Leerinventario(self):
        for inventario in self.archivo.findall('listaDrones'):    # este for va a recorer todo el listado de drones que esten en el doc
            for nombreDron in inventario.findall('dron'):
                if self.VerificarDronRepetido(nombreDron.text):
                    self.Inventario_drones.enconlar(nombreDron.text)
                
    
    def LeerSistemaDrones(self):
        for ListSistemaDrones in self.archivo.findall('listaSistemasDrones'):    # este for va a recorer todo el listado de Sistema que esten en el doc
            for sistemaDrones in ListSistemaDrones.findall('sistemaDrones'):
                nombre = sistemaDrones.get("nombre")
                alturamax = sistemaDrones.find('alturaMaxima').text
                cantidadDrons = sistemaDrones.find('cantidadDrones').text
                
                #print("Nombre:",nombre)
                #print("Altura maxima:",alturamax)
                #print("Cantidad de drones:",cantidadDrons)

                tmpSistema = Sistema(nombre,alturamax,cantidadDrons)   # Creando objeto sistema que hay en el xml
                self.listSistemas.agregarFinal(tmpSistema)  # Agregando sistema a la lista de sistemas
                self.agregarValoresAlturas(sistemaDrones) 
                


    def LeerMensajes(self):
        for Listmensajes in self.archivo.findall('listaMensajes'):    # este for va a recorer todo el listado de mensajes que esten en el doc
            for mensaje in Listmensajes.findall('Mensaje'):
                nombre = mensaje.get("nombre")
                nombreSistema = mensaje.find('sistemaDrones').text
                Instrucciones = mensaje.find('instrucciones')

                #print ("Nombre:",nombre)
                #print("Sistema de Drones a usar:",nombreSistema)
                
                tmpmensaje = MensajeS(nombre,nombreSistema)   # Creando objeto sistema que hay en el xml
                self.Ilist_mensajes.agregarFinal(tmpmensaje)  # Agregando sistema a la lista de sistemas

                for instruccion in Instrucciones.findall('instruccion'):
                    dron = instruccion.get("dron")
                    posicion = instruccion.text
                    objinstruccion = Instruccion(dron,posicion)  
                    tmpmensaje.listaInstrucciones.agregarFinal(objinstruccion)
                    
        

    def agregarValoresAlturas(self,SistemaDron):

        Sistema = self.listSistemas.getFin().getDato()
        dron = Sistema.listaDrones.getInicio()
      
        for contenido in SistemaDron.findall('contenido'):
            nombreDron = contenido.find('dron').text
            alturas = contenido.find('alturas')

            dron.getDato().setNombreDron(nombreDron)        #Falta validar que exista en el inventario

            for altura in alturas.findall('altura'):
                Altura = altura.get('valor')
                letra = altura.text

                Alturas = dron.getDato().ListaAlturas.getFin()
                while Alturas:
                    if int(Altura) == int(Alturas.getDato().getAltura()):
                        Alturas.getDato().setValor(letra)

                    Alturas = Alturas.getAnterior()
            dron = dron.getSiguiente()

    
    def comprobar(self):
        
        Sistema = self.listSistemas.getInicio()
        while Sistema:                                      #Este while recorre todos los Sistemas guardados
            nombreSistema = Sistema.getDato().getNombre()
            print(nombreSistema)
            dron = Sistema.getDato().listaDrones.getInicio()    #Obteniendo el dron inicial de este sistema
            while dron:                                         #Este while recorre todos los drones que hay
                nombredron = dron.getDato().getNombreDron() 
                print(nombredron)
                altura = dron.getDato().ListaAlturas.getInicio()    #Obteniendo la primera altura de este dron
                while altura:                                       #Este while recorre todas las aturas del dron
                    Altu = altura.getDato().getAltura()
                    valor = altura.getDato().getValor()
                    print(Altu,valor)
                    altura = altura.getSiguiente()                  #Cambiando de altura
                dron = dron.getSiguiente()                          #Cambiando de dron
            Sistema = Sistema.getSiguiente()                        #Cambiando de sistema


        
        lista = self.Ilist_mensajes.getInicio()
        while lista:
            nombre = lista.getDato().getNombreMensaje()
            sistema = lista.getDato().getNombreSistema()
            print(nombre,sistema)

            instruccion = lista.getDato().listaInstrucciones.getInicio()
            while instruccion:
                dron = instruccion.getDato().getNombreDron()
                posicion = instruccion.getDato().getPosicion()
                print (dron,posicion)
                instruccion = instruccion.getSiguiente()
            lista = lista.getSiguiente()


    def VerificarDronRepetido(self,nombre):
        unico = True
        dron = self.Inventario_drones.getInicio()
        while dron:
            if dron.getDato() == nombre:
                unico = False
            dron = dron.getSiguiente()
        return unico

    def obtenerIventario(self):
        return self.Inventario_drones

objeto = xml("archivo1.xml")

