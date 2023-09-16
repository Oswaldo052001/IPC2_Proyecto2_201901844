import tkinter as tk


class Interfaz():

    def __init__(self) -> None:
        self.ventanaPrincipal = tk.Tk()
        self.abrirarchivo =  False
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
        self.CrearPestañaAnalisis(barra_menus)
        self.CrearPestañaTokens(barra_menus)
        self.CrearPestañaErrores(barra_menus)

        self.ventanaPrincipal.config(menu=barra_menus)
        
        #-------------------------------------- IMAGEN --------------------------------------------------------
        self.insertarImg("#009929",120,15,"Logo")
        self.insertarImg2("#009929",400,150,"Escudo")
        
        #---------------------------------------ETIQUETAS------------------------------------------------------
        self.crearetiqueta(620, 10, "29-06-22","Bahnschrift SemiLight Condensed",12,"black","#009929",self.ventanaPrincipal)  
        self.crearetiqueta(620, 33, "25-06-19","Bahnschrift SemiLight Condensed",12,"black","#009929",self.ventanaPrincipal) 
        self.crearetiqueta(40,130,"BIENVENIDO","Bahnschrift SemiLight Condensed",25,"#053B28","#009929",self.ventanaPrincipal)
        self.crearetiqueta(40,180,"Ministerio de Defensa de Guatemala:","Aptos Black",15,"#efa229","#009929",self.ventanaPrincipal)
        self.crearetiqueta(40,210,"Algoritmo de interceptación y decifración \n de mensajes a travez de drones con luzLed","Bahnschrift SemiLight Condensed",14,"White","#009929",self.ventanaPrincipal)
            

        #--------------------------------------BOTONES---------------------------------------------------------
        self.insertarboton(40,280,"Documentación","#8d4925",2,12,1,self.ventanaPrincipal)
        self.insertarboton(200,280,"Información Personal","#8d4925",2,16,1,self.ventanaPrincipal)
        
        self.ventanaPrincipal.mainloop()

    
       #FUNCIÓN PARA CREAR ETIQUETAS
    def crearetiqueta(self,tamx,tamy,texto,fuente,tamaño, color,fondo,ventana):

        self.etiqueta = tk.Label(ventana,text=texto) #Creación del Label
        self.etiqueta.config(bg=fondo) #insertar color de fondo
        self.etiqueta.config(font=(fuente, tamaño)) #insertar tipo y tamaño de fuente
        self.etiqueta.config(fg=color) #insertar color del texto
        self.etiqueta.place(x = tamx, y = tamy) # insertar posicion
    

      #FUNCION PARA INSERTAR UN IMAGEN
    def insertarImg(self,fondo,posx,posy,nombre):
        self.imagenL = tk.PhotoImage(file = "Img_interfaz/"+nombre+".png")   #Seleccionar imagen
        self.imagen_sub= self.imagenL.subsample(5)  # Minimizar la imagen
        self.lblimagen = tk.Label(self.ventanaPrincipal, image= self.imagen_sub) #Agregarla al label
        self.lblimagen.config(bg = fondo) # insertando color de fondo al label
        self.lblimagen.place(x = posx, y = posy) # Insertando su ubicación

          #FUNCION PARA INSERTAR UN IMAGEN
    def insertarImg2(self,fondo,posx,posy,nombre):
        self.imagenL2 = tk.PhotoImage(file = "Img_interfaz/"+nombre+".png") #Seleccionar imagen
        self.lblimagen2 = tk.Label(self.ventanaPrincipal, image= self.imagenL2) #Insertando al label
        self.lblimagen2.config(bg = fondo) #insertando color de fondo al label
        self.lblimagen2.place(x = posx, y = posy) #Insertando su ubicación


    #FUNCIÓN PARA CREAR BOTONES
    def insertarboton(self,tamx,tamy,titulo,color,ancho,largo,tipo,ventana):

        self.btn = tk.Button(ventana,text = titulo, height= ancho, width= largo, bg = color, fg='white',
        font=("Roboto Cn",12), relief="raised", borderwidth=4, cursor="hand2") #Creación del boton
        
        if tipo == 1:
            self.btn["command"] = print("hola")

        
        self.btn.place(x=tamx, y=tamy) #insertar posicion
        

    #----------------------------------------------------CREANDO MENUS------------------------------------------------------
    def CrearPestañaArchivo(self,menubase):

        menusarchivos = tk.Menu(menubase, tearoff=False, font = ("Avenir Next LT Pro Demi",11))

        menusarchivos.add_command(
            label="Nuevo",
            accelerator="Ctrl+N",
            #command=self.nuevo,
            compound=tk.LEFT
        )
        # Insertando el comando de acceso rápido
        #self.ventanaPrincipal.bind_all("<Control-n>", self.nuevo)
        
        menusarchivos.add_command(
            label="Abrir",
            accelerator="Ctrl+A",
            #command=self.Abrir_archivo,
            compound=tk.LEFT
        )
        # Insertando el comando de acceso rápido
        #self.ventanaPrincipal.bind_all("<Control-a>", self.Abrir_archivo)
                       
        menusarchivos.add_command(
            label="Guardar",
            accelerator="Ctrl+G",
            #command=self.guardar,
            compound=tk.LEFT
        )
        # Insertando el comando de acceso rápido
        #self.ventanaPrincipal.bind_all("<Control-g>", self.guardar)

        menusarchivos.add_command(
            label="GuardarComo",
            accelerator="Ctrl+S",
            #command=self.Guardarcomo,
            compound=tk.LEFT
        )

        # Insertando el comando de acceso rápido
        #self.ventanaPrincipal.bind_all("<Control-s>", self.Guardarcomo)

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

    def CrearPestañaAnalisis(self,menubase):
       
        menuAnalisis = tk.Menu(menubase, tearoff=False, font = ("Avenir Next LT Pro Demi",11))

        menuAnalisis.add_command(
            label="Generar Sentencia",
            accelerator="Ctrl+Q",
            #command=self.analisis,
            compound=tk.LEFT
        )

        # Insertando el comando de acceso rápido
        #self.ventanaPrincipal.bind_all("<Control-q>", self.analisis)
        
        # Insertarla en la ventana principal.
        menubase.add_cascade(menu=menuAnalisis, label="Analisis")
 
#-------------------------------------------------------------------------------------------------------------------------

    def CrearPestañaTokens(self,menubase):
       
        menuTokens = tk.Menu(menubase, tearoff=False, font = ("Avenir Next LT Pro Demi",11))

        menuTokens.add_command(
            label="Ver Tokens",
            accelerator="Ctrl+T",
            #command=self.Tokens,
            compound=tk.LEFT
        )
        # Insertando el comando de acceso rápido
        #self.ventanaPrincipal.bind_all("<Control-t>", self.Tokens)
        
        # Insertarla en la ventana principal.
        menubase.add_cascade(menu=menuTokens, label="Tokens")

#--------------------------------------------------------------------------------------------------------------------------

    def CrearPestañaErrores(self,menubase):
       
        menuErrores = tk.Menu(menubase, tearoff=False, font = ("Avenir Next LT Pro Demi",11))

        menuErrores.add_command(
            label="Mostrar Errores",
            accelerator="Ctrl+E",
            #command=self.errores,
            compound=tk.LEFT
        )
        # Insertando el comando de acceso rápido
       #self.ventanaPrincipal.bind_all("<Control-e>", self.errores)
        
        # Insertarla en la ventana principal.
        menubase.add_cascade(menu=menuErrores, label="Errores")


#------------------------------------ FUNCIONES -----------------------------------------------------
    def Salir(self,event = None):
        self.ventanaPrincipal.destroy()
 
app = Interfaz()