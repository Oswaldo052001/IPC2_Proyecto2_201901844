import tkinter as tk
import webbrowser
from Lista_Simple import ListaSimple
from Cola import Cola
from tkinter import filedialog, messagebox, ttk
from Xml import xml
from Graph import Graph, GraphProcesarMensaje
from ProcesarMensaje import procesar
from Archivosalida import Archivo

class Interfaz():

    def __init__(self) -> None:
        self.ventanaPrincipal = tk.Tk()
        self.componentes()


    #------------------------------------------- COMPONENTES DE LA VENTANA  PRINCIPAL----------------------------------------------
    def componentes(self):

        #DISEÑO DE LA VENTANA PRINCIPAL
        self.ventanaPrincipal.state(newstate = "normal")
        tamx = 700
        tamy = 400
        x_ventana = self.ventanaPrincipal.winfo_screenwidth() // 2 - tamx // 2
        y_ventana = self.ventanaPrincipal.winfo_screenheight() // 2 - tamy // 2
        posicion = str(tamx) + "x" + str(tamy) + "+" + str(x_ventana) + "+" + str(y_ventana) #creación de la ventana
        self.ventanaPrincipal.geometry(posicion) #insertar posición
        self.ventanaPrincipal.title("Proyecto 2") #insertar titulo
        self.ventanaPrincipal.config(bg="#3E5F8A") #insertar fondo
        self.ventanaPrincipal.resizable(0,0)
        barra_menus = tk.Menu()
        
    
        self.CrearPestañaArchivo(barra_menus)
        self.CrearGestionDrones(barra_menus)
        self.CrearPestañaSistema(barra_menus)
        self.CrearPestañaMensaje(barra_menus)

        self.ventanaPrincipal.config(menu=barra_menus)
        
        #-------------------------------------- IMAGEN --------------------------------------------------------
        self.insertarImg("#3E5F8A",120,15,"Logo",self.ventanaPrincipal)
        self.insertarImg2("#3E5F8A",400,150,"Escudo",self.ventanaPrincipal)
        
        #---------------------------------------ETIQUETAS------------------------------------------------------
        self.crearetiqueta(620, 10, "29-06-22","Bahnschrift SemiLight Condensed",12,"black","#3E5F8A",self.ventanaPrincipal)  
        self.crearetiqueta(620, 33, "25-06-19","Bahnschrift SemiLight Condensed",12,"black","#3E5F8A",self.ventanaPrincipal) 
        self.crearetiqueta(40,130,"BIENVENIDO","Bahnschrift SemiLight Condensed",25,"#c7f7f7","#3E5F8A",self.ventanaPrincipal)
        self.crearetiqueta(40,180,"Ministerio de Defensa de Guatemala:","Aptos Black",15,"#efa229","#3E5F8A",self.ventanaPrincipal)
        self.crearetiqueta(40,210,"Algoritmo de interceptación y decifración \n de mensajes a travez de drones con luzLed","Bahnschrift SemiLight Condensed",14,"White","#3E5F8A",self.ventanaPrincipal)
            

        #--------------------------------------BOTONES---------------------------------------------------------
        self.insertarboton(40,280,"Documentación","#8d4925",2,12,"Documentacion",self.ventanaPrincipal)
        self.insertarboton(200,280,"Información Personal","#8d4925",2,16,"Informacion",self.ventanaPrincipal)
        
        self.ventanaPrincipal.mainloop()

    
    def crearVentana(self,ventana,x,y,titulo,fondo):
        tamx = x
        tamy = y
        x_ventana = ventana.winfo_screenwidth() // 2 - tamx // 2
        y_ventana = ventana.winfo_screenheight() // 2 - tamy // 2
        posicion = str(tamx) + "x" + str(tamy) + "+" + str(x_ventana) + "+" + str(y_ventana) #creación de la ventana
        ventana.geometry(posicion) #insertar posición
        ventana.title(titulo) #insertar titulo
        ventana.config(bg=fondo) #insertar fondo
        ventana.resizable(0,0)

       #FUNCIÓN PARA CREAR ETIQUETAS
    def crearetiqueta(self,tamx,tamy,texto,fuente,tamaño, color,fondo,ventana):

        self.etiqueta = tk.Label(ventana,text=texto) #Creación del Label
        self.etiqueta.config(bg=fondo) #insertar color de fondo
        self.etiqueta.config(font=(fuente, tamaño)) #insertar tipo y tamaño de fuente
        self.etiqueta.config(fg=color) #insertar color del texto
        self.etiqueta.place(x = tamx, y = tamy) # insertar posicion
    
        #FUNCION PARA CREAR UN CUADRO DE TEXTO
    def crear_cuadrodeTexto(self,tamx,tamy,fuente,tamaño,alto,largo,color,Caja):

        Caja.config(font=(fuente, tamaño),width=largo,height=alto,wrap="none",bg=color) #insertar tipo y tamaño de fuente
        Caja.place(x = tamx, y = tamy) # insertar posicion

            #FUNCION PARA CREAR UN CUADRO DE TEXTO
    def cajadetexto(self,tamx,tamy,fuente,tamaño,alto,largo,color,Caja):

        Caja.config(font=(fuente, tamaño),bg=color, justify = tk.CENTER) #insertar tipo y tamaño de fuente
        Caja.place(width=largo,height=alto)
        Caja.place(x = tamx, y = tamy) # insertar posicion
    

      #FUNCION PARA INSERTAR UN IMAGEN
    def insertarImg(self,fondo,posx,posy,nombre,ventana):
        self.imagenL = tk.PhotoImage(file = "Img_interfaz/"+nombre+".png")   #Seleccionar imagen
        self.imagen_sub = self.imagenL.subsample(5)  # Minimizar la imagen
        self.lblimagen = tk.Label(ventana, image= self.imagen_sub) #Agregarla al label
        self.lblimagen.config(bg = fondo) # insertando color de fondo al label
        self.lblimagen.place(x = posx, y = posy) # Insertando su ubicación

    def insertarImg2(self,fondo,posx,posy,nombre,ventana):
        self.imagenL2 = tk.PhotoImage(file = "Img_interfaz/"+nombre+".png") #Seleccionar imagen
        self.lblimagen2 = tk.Label(ventana, image= self.imagenL2) #Insertando al label
        self.lblimagen2.config(bg = fondo) #insertando color de fondo al label
        self.lblimagen2.place(x = posx, y = posy) #Insertando su ubicación

    def insertarImg3(self,fondo,posx,posy,nombre,ventana):
        self.imagenL3 = tk.PhotoImage(file = "Img_interfaz/"+nombre+".png") #Seleccionar imagen
        self.imagen_sub3 = self.imagenL3.subsample(3)  # Minimizar la imagen
        self.lblimagen3 = tk.Label(ventana, image= self.imagen_sub3) #Insertando al label
        self.lblimagen3.config(bg = fondo) #insertando color de fondo al label
        self.lblimagen3.place(x = posx, y = posy) #Insertando su ubicación

    def insertarImg4(self,fondo,posx,posy,nombre,ventana):
        self.imagenL4 = tk.PhotoImage(file = "Img_interfaz/"+nombre+".png") #Seleccionar imagen
        self.imagen_sub4 = self.imagenL4.subsample(4)  # Minimizar la imagen
        self.lblimagen4 = tk.Label(ventana, image= self.imagen_sub4) #Insertando al label
        self.lblimagen4.config(bg = fondo) #insertando color de fondo al label
        self.lblimagen4.place(x = posx, y = posy) #Insertando su ubicación


    #FUNCIÓN PARA CREAR BOTONES
    def insertarboton(self,tamx,tamy,titulo,color,ancho,largo,tipo,ventana):

        self.btn = tk.Button(ventana,text = titulo, height= ancho, width= largo, bg = color, fg='white',
        font=("Roboto Cn",12), relief="raised", borderwidth=4, cursor="hand2") #Creación del boton
        
        if tipo == "Documentacion":
            self.btn["command"] = self.abrirDocumentacion

        if tipo == "Informacion":
            self.btn["command"] = self.VentanaInformacion

        if tipo =="CrearDron":
            self.btn["command"] = self.guardarDron

        if tipo == "GraficarSistema":
            self.btn["command"] = self.crearGrafica

        if tipo == "Decodificar":
            self.btn["command"] = self.seleccionar

        if tipo == "graficarmensaje":
            self.btn["command"] = self.graficarOperaciones


        
        self.btn.place(x=tamx, y=tamy) #insertar posicion
        

    #----------------------------------------------------CREANDO MENUS------------------------------------------------------
    def CrearPestañaArchivo(self,menubase):

        menusarchivos = tk.Menu(menubase, tearoff=False, font = ("Avenir Next LT Pro Demi",11))

        menusarchivos.add_command(
            label="Inicializar Sistema",
            command=self.inicializar,
            compound=tk.LEFT
        )

        menusarchivos.add_command(
            label="Cargar",
            command=self.leerArchivo,
            compound=tk.LEFT
        )
        # Insertando el comando de acceso rápido
        #self.ventanaPrincipal.bind_all("<Control-n>", self.nuevo)
        
        menusarchivos.add_command(
            label="Generar",
            command=self.crearArchivoSalid,
            compound=tk.LEFT
        )
        # Insertando el comando de acceso rápido
        #self.ventanaPrincipal.bind_all("<Control-a>", self.Abrir_archivo)
                       
        menusarchivos.add_separator()
        menusarchivos.add_command(
            label="Salir", 
            command= self.Salir,
            accelerator="Esc")
        
        # Insertando el comando de acceso rápido
        self.ventanaPrincipal.bind_all("<Escape>", self.Salir )

        # Insertarla en la ventana principal.
        menubase.add_cascade(menu=menusarchivos, label="Archivo")


#--------------------------------------------------------------------------------------------------------------------------

    def CrearGestionDrones(self,menubase):
       
        menuDrones = tk.Menu(menubase, tearoff=False, font = ("Avenir Next LT Pro Demi",11))

        menuDrones.add_command(
            label="Inventario",
            command=self.VenanaMostrarInventario,
            compound=tk.LEFT
        )

        menuDrones.add_command(
            label="Agregar",
            command=self.VentanaNuevoDron,
            compound=tk.LEFT
        )
        
        # Insertarla en la ventana principal.
        menubase.add_cascade(menu=menuDrones, label="Drones")
 
#-------------------------------------------------------------------------------------------------------------------------

    def CrearPestañaSistema(self,menubase):
       
        menuSistema = tk.Menu(menubase, tearoff=False, font = ("Avenir Next LT Pro Demi",11))

        menuSistema.add_command(
            label="Ver Gráfica",
            command=self.VentanamostrarSistema,
            compound=tk.LEFT
        )
        
        # Insertarla en la ventana principal.
        menubase.add_cascade(menu=menuSistema, label="Sistema")

#--------------------------------------------------------------------------------------------------------------------------

    def CrearPestañaMensaje(self,menubase):
       
        menuMensaje = tk.Menu(menubase, tearoff=False, font = ("Avenir Next LT Pro Demi",11))

        menuMensaje.add_command(
            label="Mostrar mensajes",
            command=self.Ventanamostrarmensajes,
            compound=tk.LEFT
        )

        menuMensaje.add_command(
            label="Procesar mensaje",
            command=self.ventanaProcesarmensajes,
            compound=tk.LEFT
        )

    
        # Insertarla en la ventana principal.
        menubase.add_cascade(menu=menuMensaje, label="Mensaje")


#------------------------------------------------------ VENTANAS EMERGENTES  -------------------------------------------------------------
    
    def VentanaInformacion(self):
            ventanaInformacion = tk.Toplevel()   #Inicialiazando la ventana emergente
            self.crearVentana(ventanaInformacion,450,200,"Informacion","#2a8c4a")  #Creando la ventana
            self.crearetiqueta(20, 20, "INFORMACION DEL PROGRAMADOR: ","Bahnschrift SemiLight Condensed",20,"#f2be22","#2a8c4a",ventanaInformacion)  #Creando etiqueta
            self.crearetiqueta(40, 60, "OSWALDO ANTONIO CHOC CUTERES ","Bahnschrift SemiLight Condensed",15,"white","#2a8c4a",ventanaInformacion)  #Creando etiqueta
            self.crearetiqueta(40, 90, "201901844","Bahnschrift SemiLight Condensed",15,"white","#2a8c4a",ventanaInformacion)  #Creando etiqueta
            self.crearetiqueta(40, 120, "4TO SEMESTRE ","Bahnschrift SemiLight Condensed",15,"white","#2a8c4a",ventanaInformacion)  #Creando etiqueta
            self.crearetiqueta(40, 150, "INTRODUCCION A LA PROGRAMACION Y COMPUTACION 2 ","Bahnschrift SemiLight Condensed",15,"white","#2a8c4a",ventanaInformacion)  #Creando etiqueta


           

    def VenanaMostrarInventario(self):                   #Esta ventana muestra el inventario de drones que hay en el archivp
        dron = xml.Inventario_drones.getInicio()
        if dron:                                         #Siempre y cuando exista almenos un dron se abrirá la ventana
            ventanaInventario = tk.Toplevel()            #Inicialiazando la ventana emergente
            cajatexto = tk.Text(ventanaInventario)       #Caja de texto donde se mostrara los drones
            self.crearVentana(ventanaInventario,300,200,"Inventario","#64c27b")       #Creando la ventana
            self.crearetiqueta(15, 20, "Los drones ingresados son los siguientes:","Bahnschrift SemiLight Condensed",14,"white","#64c27b",ventanaInventario)  #Creando la etiqueta
            self.crear_cuadrodeTexto(20,50,"Arial",12,7,28,"white",cajatexto)       #Creando cuadro de texto

            contador = 1                                    
            while dron:                 #Este while va a mostrar todos los drones que hayan en el inventario
                mensaje = str(contador)+") "+dron.getDato()+"\n"    
                cajatexto.insert(tk.INSERT,mensaje)         #Insertando el dron
                dron = dron.getSiguiente()
                contador += 1
            
            cajatexto.configure(state='disabled')           #Es configuración permite que no se pueda editar el texto
        else:
            messagebox.showinfo(message="TODAVIA NO SE HA INGRESADO NINGUN DRON", title="VUELVA A INTENTAR")  # Si hubo problema mostrará este mensaje


    def VentanaNuevoDron(self):
            ventanaDron = tk.Toplevel()   #Inicialiazando la ventana emergente
            self.nombreDron = tk.Text(ventanaDron)   #Caja de texto donde se mostrara los drones
            self.crearVentana(ventanaDron,550,200,"Crear Dron","#BDECB6")  #Creando la ventana
            self.crearetiqueta(20, 20, "Ingrese el nombre del dron: ","Bahnschrift SemiLight Condensed",20,"#ea2ce4","#BDECB6",ventanaDron)  #Creando etiqueta

            #COMPONENTES VENTANA
            self.crear_cuadrodeTexto(20,70,"Arial",20,1,20,"white",self.nombreDron)  #Creando la caja de texto
            self.insertarImg3("#BDECB6",350,10,"dron",ventanaDron)    #Insertando imagen
            self.insertarboton(110,120,"Crear","#efa229",1,12,"CrearDron",ventanaDron)  #Insertando boton para crear dron



    def VentanamostrarSistema(self):
        sistema = xml.listSistemas.getInicio()        
        if sistema:                                     #Siempre y cuando exista algun sistema ingresado en el archivo se mostrará la ventana
            ventanaSistema = tk.Toplevel()              #Inicialiazando la ventana emergente
            cajatexto = tk.Text(ventanaSistema)         #Caja de texto donde se mostrara los sistemas
            self.nombreSistema = tk.Text(ventanaSistema)         #Caja de texto donde el usuario podrá ingresar el nombre del sistema que desea graficar
            self.crearVentana(ventanaSistema,500,300,"Graficar","#ED6A5A")          #Creando la ventana
            self.crearetiqueta(20, 20, "SISTEMAS INGRESADOS","Gill Sans Ultra Bold Condensed",20,"#FFFD82","#ED6A5A",ventanaSistema)  #Creando etiqueta
            self.crearetiqueta(298, 70, "Ingrese el nombre del sistema \nque desea graficar","Bahnschrift SemiLight Condensed",14,"#F4F1BB","#ED6A5A",ventanaSistema)  #Creando etiqueta
            self.crear_cuadrodeTexto(20,70,"Bahnschrift SemiCondensed",12,11,33,"white",cajatexto)  #Creando cuadro de texto
            self.crear_cuadrodeTexto(312,150,"Arial",15,1,15,"#9bc1bc",self.nombreSistema) #Creando cuadro de texto
            self.insertarboton(350,200,"Graficar","#1B998B",1,8,"GraficarSistema",ventanaSistema)  #Creando boton
            

            contador = 1
            while sistema:   #Este while va a mostrar todos los sistemas que hay
                mensaje = "   "+str(contador)+") "+sistema.getDato().getNombre()+"\n"
                cajatexto.insert(tk.INSERT,mensaje)  #Inserando sistema
                sistema = sistema.getSiguiente()
                contador += 1
            cajatexto.configure(state='disabled')   #Esta configuración permite que no sea editable el cuadro de texto
        else:
            messagebox.showinfo(message="TODAVIA NO SE HA INGRESADO NINGUN SISTEMA", title="VUELVA A INTENTAR")  # Si hubo problema mostrará este mensaje

    
    def Ventanamostrarmensajes(self):
        mensajes = xml.mensajesordenados.getInicio()      
        if mensajes:                            #Siempre y cuando existan mensajes ingresados se mostrara la ventana
            ventanamensajes = tk.Toplevel()     #Inicialiazando la ventana emergente
            cajatexto = tk.Text(ventanamensajes) #Caja de texto donde se mostrara los mensajes
            self.crearVentana(ventanamensajes,500,600,"Mensajes","#2CA18C")  #Creando ventana
            self.crearetiqueta(42, 20, "MENSAJES INGRESADOS","Gill Sans Ultra Bold Condensed",30,"#FFFD82","#2CA18C",ventanamensajes)  #Creando etiqueta
            self.crear_cuadrodeTexto(23,80,"Bahnschrift SemiCondensed",12,26,56,"#EEE2D1",cajatexto)   #Creando cuadro de texto

            ms = xml.mensajesordenados.getInicio()
            while ms:     #Este while va a recorrer los mesajes ingresados de forma ordenada
                lista = xml.Ilist_mensajes.getInicio()
                while lista:    #Este while va a recorrer la lista de mensajes de forma desordenada y los va a ir mostrando ya ordenados
                    nombre = lista.getDato().getNombreMensaje()
                    if ms.getDato() == nombre:      #Si el mensaje de la lista desordenada es igual al mensaje de la lista ordenada se mostrará
                        titulo = "\n\t• Mensaje: "+nombre+"\n"
                        cajatexto.insert(tk.INSERT,titulo)     #Insertando mensaje

                        instruccion = lista.getDato().listaInstrucciones.getInicio()
                        contador = 1
                        while instruccion:   #Este while va a recorrer las instrucciones de ese mensaje
                            dron = instruccion.getDato().getNombreDron()
                            posicion = instruccion.getDato().getPosicion()

                            salida = "\n\t\t"+str(contador)+")"+" Instruccion: "+str(dron)+"= altura: "+str(posicion)+"\n"
                            cajatexto.insert(tk.INSERT,salida)   #Insertando instruccion
                            contador += 1
                            instruccion = instruccion.getSiguiente()
                    lista = lista.getSiguiente()
                ms = ms.getSiguiente()
            cajatexto.configure(state='disabled')
        else:
            messagebox.showinfo(message="TODAVIA NO SE HA INGRESADO NINGUN SISTEMA", title="VUELVA A INTENTAR")  # Si hubo problema mostrará este mensaje
    


    def ventanaProcesarmensajes(self):
        self.mensajeprocesado = False
        mensajes = xml.mensajesordenados.getInicio()      
        if mensajes:                            #Siempre y cuando existan mensajes ingresados se mostrara la ventana
            ventanamensajes = tk.Toplevel()     #Inicialiazando la ventana emergente
            self.cajaSistema = tk.Entry(ventanamensajes) #Caja de texto donde se mostrara los mensajes
            self.cajaTiempo = tk.Entry(ventanamensajes) #Caja de texto donde se mostrara los mensajes
            self.cajaMensaje = tk.Entry(ventanamensajes) #Caja de texto donde se mostrara los mensajes

            self.crearVentana(ventanamensajes,600,400,"PROCESAR MENSAJES","#31b189")  #Creando ventana
            self.crearetiqueta(30, 20, "DECODIFICAR MENSAJE","Gill Sans Ultra Bold Condensed",25,"#ffc672","#31b189",ventanamensajes)  #Creando etiqueta
            self.crearetiqueta(30, 60, "Seleccione el nombre del mensaje que desea decodificar","Bahnschrift SemiLight Condensed",14,"white","#31b189",ventanamensajes)  #Creando etiqueta
            self.crearetiqueta(30, 200, "Sistema:","Bahnschrift SemiLight Condensed",14,"white","#31b189",ventanamensajes)  #Creando etiqueta
            self.crearetiqueta(220, 200, "Tiempo:","Bahnschrift SemiLight Condensed",14,"white","#31b189",ventanamensajes)  #Creando etiqueta
            self.crearetiqueta(410, 200, "Mensaje:","Bahnschrift SemiLight Condensed",14,"white","#31b189",ventanamensajes)  #Creando etiqueta
            self.insertarImg4("#31b189",400,1,"procesando",ventanamensajes)    #Insertando imagen
            self.insertarboton(140,150,"Decodificar","#7ace67",1,12,"Decodificar",ventanamensajes)  #Creando boton
            self.insertarboton(240,320,"graficar","#ed639e",1,12,"graficarmensaje",ventanamensajes)  #Creando boton

            self.cajadetexto(30,250,"Bahnschrift SemiCondensed",12,40,160,"#EEE2D1",self.cajaSistema)   #Creando cuadro de texto
            self.cajadetexto(220,250,"Bahnschrift SemiCondensed",12,40,160,"#EEE2D1",self.cajaTiempo)   #Creando cuadro de texto
            self.cajadetexto(410,250,"Bahnschrift SemiCondensed",12,40,160,"#EEE2D1",self.cajaMensaje)   #Creando cuadro de texto

            self.cajaSistema.config(state=tk.DISABLED)
            self.cajaTiempo.config(state=tk.DISABLED)
            self.cajaMensaje.config(state=tk.DISABLED)

            self.textoboxmensajes = ttk.Combobox(ventanamensajes,state="readonly")
            self.textoboxmensajes.config(font=("Arial", 15),width=25,height=10) #insertar tipo y tamaño de fuente
            self.textoboxmensajes.place(x=55, y=100)
            ms = xml.mensajesordenados.getInicio()
            Lista = ""
            while ms:
                Lista += ms.getDato()
                ms = ms.getSiguiente()
                if ms != None:
                    Lista += ","

            self.textoboxmensajes["values"] = (Lista.split(sep=','))

        else:
            messagebox.showinfo(message="TODAVIA NO SE HA INGRESADO NINGUN SISTEMA", title="VUELVA A INTENTAR")  # Si hubo problema mostrará este mensaje
    

        

#---------------------------------------------------------METODOS PARA LOS BOTONES------------------------------------------------------- 

    def Salir(self):
        self.ventanaPrincipal.destroy()


    def inicializar(self):
        xml.Inventario_drones = None
        xml.listSistemas = None
        xml.Ilist_mensajes = None
        xml.mensajesordenados = None


        xml.Inventario_drones = Cola()
        xml.listSistemas = ListaSimple()
        xml.Ilist_mensajes = ListaSimple()
        xml.mensajesordenados = Cola()

    
    def abrirDocumentacion(self):
        path = 'Documentación\Documentación Proyecto.pdf'
        webbrowser.open_new(path)

     


    def leerArchivo(self):
        filename = filedialog.askopenfilename(title="buscar archivo",filetypes=(("archivos xml",'*.xml'),("todos los archivos",'*')))   #Obteniendo la dirección donde se encuentra el archivo
        try:
            xml(filename)  #Ingresando a la clase xml y almacenando la imformación del xml
            messagebox.showinfo(message="SE CARGO CORRECTAMENTE", title="Msg")  # Si no hubo problema mostrará este mensaje 

        except:
            messagebox.showinfo(message="A OCURRIDO UN ERROR AL CARGAR EL ARCHIVO \n VUELVA A INTENTARLO", title="ERROR")  # Si hubo problema mostrará este mensaje


    def guardarDron(self):
        name = self.nombreDron.get(1.0,"end-1c")

        if name != "":
            unico = True
            dron = xml.Inventario_drones.getInicio()
            while dron:
                if dron.getDato() == name:
                    unico = False
                    messagebox.showinfo(message="ESE NOMBRE YA EXISTE", title="ERROR")  # Si hubo problema mostrará este mensaje
                dron = dron.getSiguiente()
        
            if unico:
                xml.Inventario_drones.enconlar(name)
                messagebox.showinfo(message="SE AGREGÓ CORRECTAMENTE", title="EXITO")  # Si hubo problema mostrará este mensaje
        else:
            messagebox.showinfo(message="NO HAN INGRESADO NINGUN NOMBRE", title="ERROR")  # Si hubo problema mostrará este mensaje

    
    
    def crearGrafica(self):
        name = self.nombreSistema.get(1.0,"end-1c")
        sistema = xml.listSistemas.getInicio()
        encontro = False

        try:
            while sistema:
                if sistema.getDato().getNombre().lower() == name.lower():
                    encontro = True
                    grafica = Graph(sistema.getDato(),"Sistema_"+name)
                    grafica.crearGraficaOriginal()
                    messagebox.showinfo(message="SE GRAFICÓ CORRECTAMENTE", title="REALIZADO")  # Si hubo problema mostrará este mensaje
                sistema = sistema.getSiguiente()
        except:
            messagebox.showinfo(message="OCURRIO UN ERROR AL GRAFICAR REVISE EL ARCHIVO", title="ERROR")  # Si hubo problema mostrará este mensaje
        
        if encontro == False:
            messagebox.showinfo(message="EL NOMBRE INGRESADO NO EXISTE", title="VUELVA A INTENTAR")  # Si hubo problema mostrará este mensaje    
    

    def seleccionar(self):
        
        nombremensaje = self.textoboxmensajes.get()
        if nombremensaje != "":

            self.cajaSistema.config(state=tk.NORMAL)
            self.cajaTiempo.config(state=tk.NORMAL)
            self.cajaMensaje.config(state=tk.NORMAL)

            self.cajaSistema.delete(0, tk.END)
            self.cajaTiempo.delete(0, tk.END)
            self.cajaMensaje.delete(0, tk.END)

            mensa = xml.Ilist_mensajes.getInicio()
            sistema = xml.listSistemas.getInicio()
            listainstrucciones = None
            listadrones = None
            self.sistemaMensaje = None
            self.datosMensaje = None
            nombresistema = ""
            
            while mensa:
                if mensa.getDato().getNombreMensaje() == nombremensaje:
                    self.datosMensaje = mensa
                    listainstrucciones = mensa.getDato().listaInstrucciones
                    nombresistema = mensa.getDato().getNombreSistema()
                mensa = mensa.getSiguiente()

        
            while sistema:
                if sistema.getDato().getNombre() == nombresistema:
                    listadrones = sistema.getDato().listaDrones
                    self.sistemaMensaje = sistema.getDato()
                sistema = sistema.getSiguiente()

            try:
                procesar(listainstrucciones, listadrones, self.datosMensaje)
                archi = Archivo(self.sistemaMensaje,self.datosMensaje)
                archi.AgregarMensaje()

                sistema = self.datosMensaje.getDato().getNombreSistema()
                tiempo = self.datosMensaje.getDato().getTeimpoObtimo()
                mensajedecifrado = self.datosMensaje.getDato().getMensajedecifrado()
                
                self.cajaSistema.config(state=tk.NORMAL)
                self.cajaTiempo.config(state=tk.NORMAL)
                self.cajaMensaje.config(state=tk.NORMAL)

                self.cajaSistema.insert(0,sistema)
                self.cajaTiempo.insert(0,str(tiempo))
                self.cajaMensaje.insert(0,mensajedecifrado)

                self.cajaSistema.config(state=tk.DISABLED)
                self.cajaTiempo.config(state=tk.DISABLED)
                self.cajaMensaje.config(state=tk.DISABLED)

                self.mensajeprocesado = True
            except:
                messagebox.showinfo(message="A OCURRIDO UN ERROR AL PROCESAR EL ARCHIVO \n VUELVA A INTENTARLO", title="ERROR")  # Si hubo problema mostrará este mensaje
            

    def graficarOperaciones(self):
        if self.mensajeprocesado:
            nombre = self.datosMensaje.getDato().getNombreMensaje()+"_Decifrado"
            grafica = GraphProcesarMensaje(self.sistemaMensaje, self.datosMensaje,nombre)
            grafica.crearGraficaMensaje()
            messagebox.showinfo(message="SE GRAFICÓ CORRECTAMENTE", title="REALIZADO")  # Si hubo problema mostrará este mensaje
        
        else:
            messagebox.showinfo(message="No sea ha procesado ningun mensaje", title="VUELVA A INTENTAR")  # Si hubo problema mostrará este mensaje   
    

    def crearArchivoSalid(self):
        
        archi = Archivo()
        archi.crearArchivo()
        messagebox.showinfo(message="SE CREÓ EL ARCHIVO CORRECTAMENTE", title="REALIZADO")  # Si hubo problema mostrará este mensaje

app = Interfaz()