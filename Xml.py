import xml.etree.ElementTree as ET
from tkinter import messagebox
from Lista_Simple import ListaSimple
from Sistema import Sistema
from Cola import Cola
from Mensaje import MensajeS
from Instruccion import Instruccion
from Graph import Graph



class xml():
    Inventario_drones = Cola()
    listSistemas = ListaSimple()
    Ilist_mensajes = ListaSimple()
    mensajesordenados = Cola()

    
    def __init__(self,ruta):
        self.archivo = ET.parse(ruta).getroot()
        self.Leerinventario()
        self.LeerSistemaDrones()
        self.LeerMensajes()
        #self.procesarmensaje("msg")
        #self.procesarmensaje("msg2")
        #self.prueba()
        #self.comprobar2()
    

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
                self.sistemarepetido = None
                nombre = sistemaDrones.get("nombre")
                alturamax = sistemaDrones.find('alturaMaxima').text
                cantidadDrons = sistemaDrones.find('cantidadDrones').text

                if int(alturamax) > 100:
                    alturamax = 100
                
                if int(cantidadDrons) > 200:
                    cantidadDrons = 200
                
                #print("Nombre:",nombre)
                #print("Altura maxima:",alturamax)
                #print("Cantidad de drones:",cantidadDrons)
     
                if self.sistemaExistente(nombre):
                    self.verificarSistema(sistemaDrones,self.sistemarepetido)
                    #self.agregarValoresAlturas(sistemaDrones,self.sistemarepetido)
                
                else:
                    tmpSistema = Sistema(nombre,alturamax,cantidadDrons)   # Creando objeto sistema que hay en el xml
                    self.listSistemas.agregarFinal(tmpSistema)  # Agregando sistema a la lista de sistemas
                    ssistema = self.listSistemas.getFin().getDato()
                    self.agregarValoresAlturas(sistemaDrones,ssistema) 
                    

    def verificarSistema(self,SistemaDron, Sistema):

        #dron = Sistema.listaDrones.getInicio()
        for contenido in SistemaDron.findall('contenido'):
            nombreDron = contenido.find('dron').text
            alturas = contenido.find('alturas')
            dron = Sistema.listaDrones.getInicio()
            
            if self.existeDron(nombreDron):

                if self.añadir(nombreDron,alturas):
                    while dron.getDato().getNombreDron() != None:
                        dron = dron.getSiguiente()
                    dron.getDato().setNombreDron(nombreDron)        #Falta validar que exista en el inventario

                    for altura in alturas.findall('altura'):
                        Altura = altura.get('valor')
                        letra = altura.text
                        Alturas = dron.getDato().ListaAlturas.getFin()
                        while Alturas:
                            if int(Altura) == int(Alturas.getDato().getAltura()):
                                Alturas.getDato().setValor(letra)
                            Alturas = Alturas.getAnterior()

            else:
                messagebox.showinfo(message="EL DRON \""+nombreDron+"\" NO EXISTE EN EL INVENTARIO \n  REVISE EL SISTEMA "+Sistema.getNombre(), title="VUELVA A INTENTAR")  # Si hubo problema mostrará este mensaje
            dron = dron.getSiguiente()

        
    def añadir(self,nombre,alturas):
        nuevo = True
        dron = self.sistemarepetido.listaDrones.getInicio()

        while dron:
            if dron.getDato().getNombreDron() == nombre:
                nuevo = False
                for altura in alturas.findall('altura'):
                    Altura = altura.get('valor')
                    letra = altura.text

                    Alturas = dron.getDato().ListaAlturas.getInicio()

                    while Alturas:
                        if int(Altura) == int(Alturas.getDato().getAltura()):
                            if Alturas.getDato().getValor() != letra:
                                Alturas.getDato().setValor(letra)
                        Alturas = Alturas.getSiguiente()         
            dron = dron.getSiguiente()
        return nuevo
    

    def sistemaExistente(self,nombre):
        existe = False       
        sistema = self.listSistemas.getInicio()   #Verificamos de los sistemas ya ingresados si existe o no un sistema con ese nombre
        while sistema:
            if sistema.getDato().getNombre() == nombre:  #Si en todo caso existe
                self.sistemarepetido = sistema.getDato() #Aguardamos el sistema en una variable para luego acceder a ella y a su contenido
                existe = True  
            sistema = sistema.getSiguiente()
        return existe  #Retornamos un verdadero o un falso 

    def LeerMensajes(self):
        for Listmensajes in self.archivo.findall('listaMensajes'):    # este for va a recorer todo el listado de mensajes que esten en el doc
            for mensaje in Listmensajes.findall('Mensaje'):
                self.mensajerepetido = None
                nombre = mensaje.get("nombre")
                nombreSistema = mensaje.find('sistemaDrones').text
                Instrucciones = mensaje.find('instrucciones')

                #print ("Nombre:",nombre)
                #print("Sistema de Drones a usar:",nombreSistema)

                if self.mensajeExistente(nombre):   #Verificamos si ya existe algun mensaje con el mismo nombre

                    instruccionesexistentes = self.mensajerepetido.listaInstrucciones.getInicio() #Accediendo a la lista de instrucciones del mensaje que ya existe
                    #Si existe hay que verificar en la lsita de instrucciones si son las mismas o cambian o hay nuevas

                    for instruccion in Instrucciones.findall('instruccion'): # Accediendo a las instrucciones que hay en el archivo
                        dron = instruccion.get("dron")  #Obteniendo el nombre del dron 
                        posicion = instruccion.text # Obteniendo la posicion 
                        nueva = True   #Si en todo caso es nueva se declara como Verdadero
                        
                        if instruccionesexistentes != None:   #Mientras las instrucciones del mensaje sea diferente de vacio 
                            nameDron = instruccionesexistentes.getDato().getNombreDron()  #Accediendo al nombre del dron de la instruccion
                            posi = instruccionesexistentes.getDato().getPosicion()  #Accediendo a la posicion del dron en la instruccion

                            if nameDron == dron:   #Si el nombre del dron del archivo y el nombre del dron existente son iguales
                                nueva = False      #No es una nueva instruccion
                                if posi != posicion:    #verificamos si es la misma posicion 
                                    instruccionesexistentes.getDato().setPosicion(posicion)  #Si no lo es se le asigna la posicion nueva

                            instruccionesexistentes = instruccionesexistentes.getSiguiente()   #Accedemos a la siguiente instruccion ya existente

                        if nueva == True:  #Si es una instruccion nueva
                            objinstruccion = Instruccion(dron,posicion)   
                            tmpmensaje.listaInstrucciones.agregarFinal(objinstruccion) #Se agrega a la lista

                else:
                    self.mensajesordenados.enconlar(nombre)        
                    tmpmensaje = MensajeS(nombre,nombreSistema)   # Creando objeto sistema que hay en el xml
                    self.Ilist_mensajes.agregarFinal(tmpmensaje)  # Agregando sistema a la lista de sistemas

                    for instruccion in Instrucciones.findall('instruccion'):
                        dron = instruccion.get("dron")  #Obteniendo el nombre del dron 
                        posicion = instruccion.text # Obteniendo la posicion 
                        objinstruccion = Instruccion(dron,posicion)  
                        tmpmensaje.listaInstrucciones.agregarFinal(objinstruccion) #Agregando a la lista de instrucciones
                        

    def mensajeExistente(self,nombre):
        existe = False
        mensaje = self.Ilist_mensajes.getInicio()   #Verificamos de los mensajes ya ingresados si existe o no un mensaje con ese nombre
        while mensaje:
            if mensaje.getDato().getNombreMensaje() == nombre:  #Si en todo caso existe
                self.mensajerepetido = mensaje.getDato() #Aguardamos el sistema en una variable para luego acceder a ella y a su contenido
                existe = True
            mensaje = mensaje.getSiguiente()  
        return existe         #Retornamos un verdadero o un falso
    

    def agregarValoresAlturas(self,SistemaDron,Sistema):

        dron = Sistema.listaDrones.getInicio()
      
        for contenido in SistemaDron.findall('contenido'):
            nombreDron = contenido.find('dron').text
            alturas = contenido.find('alturas')

            if self.existeDron(nombreDron):
                dron.getDato().setNombreDron(nombreDron)        #Falta validar que exista en el inventario

                for altura in alturas.findall('altura'):
                    Altura = altura.get('valor')
                    letra = altura.text

                    Alturas = dron.getDato().ListaAlturas.getFin()
                    while Alturas:
                        if int(Altura) == int(Alturas.getDato().getAltura()):
                            Alturas.getDato().setValor(letra)
                        Alturas = Alturas.getAnterior()
            else:
                messagebox.showinfo(message="EL DRON \""+nombreDron+"\" NO EXISTE EN EL INVENTARIO \n  REVISE EL SISTEMA "+Sistema.getNombre(), title="VUELVA A INTENTAR")  # Si hubo problema mostrará este mensaje
            dron = dron.getSiguiente()

    
    def existeDron(self,nombre):

        existe = False
        droninventario = self.Inventario_drones.getInicio()

        while droninventario:
            if nombre == droninventario.getDato():
                existe = True
            droninventario = droninventario.getSiguiente()
        
        return existe

    
    def comprobar(self):
        ms = self.mensajesordenados.getInicio()
        while ms:
            lista = self.Ilist_mensajes.getInicio()
            while lista:
                nombre = lista.getDato().getNombreMensaje()
                sistema = lista.getDato().getNombreSistema()
                if ms.getDato() == nombre:
                    print(nombre,sistema)
                    instruccion = lista.getDato().listaInstrucciones.getInicio()
                    while instruccion:
                        dron = instruccion.getDato().getNombreDron()
                        posicion = instruccion.getDato().getPosicion()
                        print (dron,posicion)
                        instruccion = instruccion.getSiguiente()
                lista = lista.getSiguiente()
            ms = ms.getSiguiente()


    def comprobar2(self):
        
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
            Sistema = Sistema.getSiguiente()                        #Cambiando de sistema'''


    def VerificarDronRepetido(self,nombre):
        unico = True
        dron = self.Inventario_drones.getInicio()
        while dron:
            if dron.getDato() == nombre:
                unico = False
            dron = dron.getSiguiente()
        return unico


        

#objeto = xml("archivo4.xml")
#objeto = xml("archivo5.xml")

