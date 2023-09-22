import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from Xml import xml
from Graph import Graph

class Interfaz():

    def __init__(self) -> None:
        self.ventanaPrincipal = tk.Tk()
        self.abrirarchivo =  False
        self.nombreDron = None
        self.nombreSistema = None
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
        self.ventanaPrincipal.config(bg="#009929") #insertar fondo
        self.ventanaPrincipal.resizable(0,0)
        barra_menus = tk.Menu()
        
    
        self.CrearPestañaArchivo(barra_menus)
        self.CrearGestionDrones(barra_menus)
        self.CrearPestañaSistema(barra_menus)
        self.CrearPestañaMensaje(barra_menus)

        self.ventanaPrincipal.config(menu=barra_menus)
        
        #-------------------------------------- IMAGEN --------------------------------------------------------
        self.insertarImg("#009929",120,15,"Logo",self.ventanaPrincipal)
        self.insertarImg2("#009929",400,150,"Escudo",self.ventanaPrincipal)
        
        #---------------------------------------ETIQUETAS------------------------------------------------------
        self.crearetiqueta(620, 10, "29-06-22","Bahnschrift SemiLight Condensed",12,"black","#009929",self.ventanaPrincipal)  
        self.crearetiqueta(620, 33, "25-06-19","Bahnschrift SemiLight Condensed",12,"black","#009929",self.ventanaPrincipal) 
        self.crearetiqueta(40,130,"BIENVENIDO","Bahnschrift SemiLight Condensed",25,"#053B28","#009929",self.ventanaPrincipal)
        self.crearetiqueta(40,180,"Ministerio de Defensa de Guatemala:","Aptos Black",15,"#efa229","#009929",self.ventanaPrincipal)
        self.crearetiqueta(40,210,"Algoritmo de interceptación y decifración \n de mensajes a travez de drones con luzLed","Bahnschrift SemiLight Condensed",14,"White","#009929",self.ventanaPrincipal)
            

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


    #FUNCIÓN PARA CREAR BOTONES
    def insertarboton(self,tamx,tamy,titulo,color,ancho,largo,tipo,ventana):

        self.btn = tk.Button(ventana,text = titulo, height= ancho, width= largo, bg = color, fg='white',
        font=("Roboto Cn",12), relief="raised", borderwidth=4, cursor="hand2") #Creación del boton
        
        if tipo == "Documentacion":
            self.btn["command"] = print("hola")

        if tipo =="CrearDron":
            self.btn["command"] = self.guardarDron

        if tipo == "GraficarSistema":
            self.btn["command"] = self.crearGrafica
        
        self.btn.place(x=tamx, y=tamy) #insertar posicion
        

    #----------------------------------------------------CREANDO MENUS------------------------------------------------------
    def CrearPestañaArchivo(self,menubase):

        menusarchivos = tk.Menu(menubase, tearoff=False, font = ("Avenir Next LT Pro Demi",11))

        menusarchivos.add_command(
            label="Cargar",
            command=self.leerArchivo,
            compound=tk.LEFT
        )
        # Insertando el comando de acceso rápido
        #self.ventanaPrincipal.bind_all("<Control-n>", self.nuevo)
        
        menusarchivos.add_command(
            label="Generar",
            #command=self.Abrir_archivo,
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
            command=self.MostrarInventario,
            compound=tk.LEFT
        )

        menuDrones.add_command(
            label="Agregar",
            command=self.NuevoDron,
            compound=tk.LEFT
        )
        
        # Insertarla en la ventana principal.
        menubase.add_cascade(menu=menuDrones, label="Drones")
 
#-------------------------------------------------------------------------------------------------------------------------

    def CrearPestañaSistema(self,menubase):
       
        menuSistema = tk.Menu(menubase, tearoff=False, font = ("Avenir Next LT Pro Demi",11))

        menuSistema.add_command(
            label="Ver Gráfica",
            command=self.mostrarSistema,
            compound=tk.LEFT
        )
        
        # Insertarla en la ventana principal.
        menubase.add_cascade(menu=menuSistema, label="Sistema")

#--------------------------------------------------------------------------------------------------------------------------

    def CrearPestañaMensaje(self,menubase):
       
        menuMensaje = tk.Menu(menubase, tearoff=False, font = ("Avenir Next LT Pro Demi",11))

        menuMensaje.add_command(
            label="Mostrar mensajes",
            #command=self.errores,
            compound=tk.LEFT
        )

        menuMensaje.add_command(
            label="Mostrar instrucciones",
            #command=self.errores,
            compound=tk.LEFT
        )

    
        # Insertarla en la ventana principal.
        menubase.add_cascade(menu=menuMensaje, label="Mensaje")


#-------------------------------------------------------- FUNCIONES -----------------------------------------------------
    def Salir(self):
        self.ventanaPrincipal.destroy()


    def leerArchivo(self):
        filename = filedialog.askopenfilename(title="buscar archivo",filetypes=(("archivos xml",'*.xml'),("todos los archivos",'*')))   #Obteniendo la dirección donde se encuentra el archivo
        try:
            xml(filename)  #Ingresando a la clase xml y almacenando la imformación del xml
            messagebox.showinfo(message="SE CARGO CORRECTAMENTE", title="Msg")  # Si no hubo problema mostrará este mensaje 
            self.abrirarchivo = True  
        except:
            messagebox.showinfo(message="A OCURRIDO UN ERROR AL CARGAR EL ARCHIVO \n VUELVA A INTENTARLO", title="ERROR")  # Si hubo problema mostrará este mensaje


    def MostrarInventario(self):
        dron = xml.Inventario_drones.getInicio()
        if dron:
            ventanaInventario = tk.Toplevel()
            cajatexto = tk.Text(ventanaInventario)
            self.crearVentana(ventanaInventario,300,200,"Inventario","#2D572C")
            self.crearetiqueta(20, 20, "Los drones ingresados son los siguientes:","Bahnschrift SemiLight Condensed",12,"white","#2D572C",ventanaInventario)  
            self.crear_cuadrodeTexto(20,50,"Arial",12,7,28,"white",cajatexto)

            contador = 1
            while dron:
                mensaje = str(contador)+") "+dron.getDato()+"\n"
                cajatexto.insert(tk.INSERT,mensaje)
                dron = dron.getSiguiente()
                contador += 1
            
            cajatexto.configure(state='disabled')
        else:
            messagebox.showinfo(message="TODAVIA NO SE HA INGRESADO NINGUN DRON", title="VUELVA A INTENTAR")  # Si hubo problema mostrará este mensaje


    def NuevoDron(self):
            ventanaDron = tk.Toplevel()
            cajatexto = tk.Text(ventanaDron)
            self.crearVentana(ventanaDron,600,200,"Crear Dron","#BDECB6")
            self.crearetiqueta(20, 20, "Ingrese el nombre del dron: ","Bahnschrift SemiLight Condensed",20,"#ea2ce4","#BDECB6",ventanaDron)  

            #COMPONENTES VENTANA
            self.crear_cuadrodeTexto(20,70,"Arial",20,1,20,"white",cajatexto)
            self.nombreDron = cajatexto
            self.insertarImg3("#BDECB6",400,10,"dron",ventanaDron)
            self.insertarboton(110,120,"Crear","#efa229",1,12,"CrearDron",ventanaDron)
            
            
    def guardarDron(self):
        name = self.nombreDron.get(1.0,"end-1c")
        unico = True
        dron = xml.Inventario_drones.getInicio()
        while dron:
            if dron.getDato() == name:
                unico = False
                messagebox.showinfo(message="ESE NOMBRE YA EXISTE", title="ERROR")  # Si hubo problema mostrará este mensaje
                self.NuevoDron()
            dron = dron.getSiguiente()
    
        if unico:
            xml.Inventario_drones.enconlar(name)
            messagebox.showinfo(message="SE AGREGÓ CORRECTAMENTE", title="EXITO")  # Si hubo problema mostrará este mensaje
            self.NuevoDron()

    
    def mostrarSistema(self):
        sistema = xml.listSistemas.getInicio()
        if sistema:
            ventanaSistema = tk.Toplevel()
            cajatexto = tk.Text(ventanaSistema)
            nameSiste = tk.Text(ventanaSistema)
            self.crearVentana(ventanaSistema,500,300,"Graficar","#ED6A5A")
            self.crearetiqueta(20, 20, "SISTEMAS INGRESADOS","Gill Sans Ultra Bold Condensed",20,"#FFFD82","#ED6A5A",ventanaSistema)  
            self.crearetiqueta(298, 70, "Ingrese el nombre del sistema \nque desea graficar","Bahnschrift SemiLight Condensed",14,"#F4F1BB","#ED6A5A",ventanaSistema)  
            self.crear_cuadrodeTexto(20,70,"Bahnschrift SemiCondensed",12,11,33,"white",cajatexto)
            self.crear_cuadrodeTexto(312,150,"Arial",15,1,15,"#9bc1bc",nameSiste)
            self.insertarboton(350,200,"Graficar","#1B998B",1,8,"GraficarSistema",ventanaSistema)
            self.nombreSistema = nameSiste

            contador = 1
            while sistema:
                mensaje = "   "+str(contador)+") "+sistema.getDato().getNombre()+"\n"
                cajatexto.insert(tk.INSERT,mensaje)
                sistema = sistema.getSiguiente()
                contador += 1
            cajatexto.configure(state='disabled')
        else:
            messagebox.showinfo(message="TODAVIA NO SE HA INGRESADO NINGUN SISTEMA", title="VUELVA A INTENTAR")  # Si hubo problema mostrará este mensaje


    def crearGrafica(self):
        name = self.nombreSistema.get(1.0,"end-1c")
        sistema = xml.listSistemas.getInicio()
        encontro = False

        while sistema:
            if sistema.getDato().getNombre().lower() == name.lower():
                encontro = True
                grafica = Graph(sistema.getDato(),"Sistema_"+name)
                grafica.crearGraficaOriginal()
                messagebox.showinfo(message="SE GRAFICÓ CORRECTAMENTE", title="REALIZADO")  # Si hubo problema mostrará este mensaje
            sistema = sistema.getSiguiente()
        
        if encontro == False:
            messagebox.showinfo(message="EL NOMBRE INGRESADO NO EXISTE", title="VUELVA A INTENTAR")  # Si hubo problema mostrará este mensaje



    
 
app = Interfaz()