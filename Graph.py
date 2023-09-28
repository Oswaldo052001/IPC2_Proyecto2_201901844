import graphviz


class Graph():
    def __init__(self,sistemaenvaida,nombre):
        self.nombre = nombre
        self.sistemaenvaida = sistemaenvaida
        self.dot = graphviz.Digraph('structs', filename=str(self.nombre)+'.gv', node_attr={'shape': 'rectangle', 'fontname':'Helvetica','style':'filled'}) 
        

    def crearGraficaOriginal(self):
        
        self.dot.node('cabeza', label= self.sistemaenvaida.getNombre(),fillcolor='#fa5f49',shape="circle")
        self.dot.node('alturas',label="Alturas",fillcolor='#95b8f6',shape="invhouse")

        self.dot.edge('cabeza','alturas',dir="none")
        self.InsertarAlturas()
        
        self.add()
        self.generar()
    
    def InsertarAlturas(self):
        altura = int(self.sistemaenvaida.getalturaMax())
        anterior = ""
        for i in range (1, altura+1):
            self.dot.node(str(i),label=str(i),fillcolor='#f9d99a') 
            if i == 1:
                self.dot.edge('alturas',str(i),dir="both", color="#fa5f49:#95b8f6")
            else: 
                self.dot.edge(str(anterior),str(i),dir="both", color="#fa5f49:#95b8f6")
            anterior = str(i)

        
    def add(self):
        dron = self.sistemaenvaida.listaDrones.getInicio()   # Variable que almacena la lista de Tiempos
        contador = 1
        while dron:
            nombredron = dron.getDato().getNombreDron()
            self.dot.node(nombredron,label=nombredron,fillcolor='#95b8f6',shape="invhouse")
            self.dot.edge('cabeza',nombredron,dir="none")

            altura = dron.getDato().ListaAlturas.getInicio()
            anterior = ""

            while altura:
                nombrealtura="A"+str(contador)+str(altura.getDato().getAltura())
                self.dot.node(nombrealtura, label=str(altura.getDato().getValor()),fillcolor='#f9d99a')
                if anterior == "":
                    self.dot.edge(nombredron,nombrealtura,dir="both", color="#fa5f49:#95b8f6")
                
                else:   
                    self.dot.edge(anterior, nombrealtura,dir="both", color="#fa5f49:#95b8f6")

                anterior = nombrealtura
                altura = altura.getSiguiente()
            contador += 1
            dron = dron.getSiguiente()


    
    def generar(self):
       self.dot.render(outfile='img/'+str(self.nombre)+'.png').replace('\\', '/')
       'img/'+str(self.nombre)+'.png' 


class GraphProcesarMensaje():
    def __init__(self,sistemaenvaida,mensaje,nombre):
        self.mensaje = mensaje
        self.nombre = nombre
        self.sistemaenvaida = sistemaenvaida
        self.dot = graphviz.Digraph('structs', filename=str(self.nombre)+'.gv', node_attr={'shape': 'rectangle', 'fontname':'Helvetica','style':'filled'}) 
        
        
    def crearGraficaMensaje(self):
        
        self.dot.node('cabeza', label= self.mensaje.getDato().getNombreMensaje(),fillcolor='#fa5f49',shape="circle")
        self.dot.node('mensaje',label="Mensaje",fillcolor='#95b8f6',shape="invhouse")
        self.dot.node('mensajedecifrado', label= self.mensaje.getDato().getMensajedecifrado(),fillcolor='#fa5f49')
        self.dot.node('tiempos',label="Tiempos",fillcolor='#95b8f6',shape="invhouse")


        self.dot.edge('cabeza','mensaje',dir= "none")
        self.dot.edge('mensaje','mensajedecifrado',dir= "none")
        self.dot.edge('cabeza','tiempos',dir="none")
        
        self.InsertarTiempos()
        self.add()
        self.generar()
    
    def InsertarTiempos(self):
        tiempo = int(self.mensaje.getDato().getTeimpoObtimo())
        anterior = ""
        for i in range (1, tiempo+1):
            self.dot.node(str(i),label=str(i),fillcolor='#f9d99a') 
            if i == 1:
                self.dot.edge('tiempos',str(i),dir="both", color="#fa5f49:#95b8f6")
            else: 
                self.dot.edge(str(anterior),str(i),dir="both", color="#fa5f49:#95b8f6")
            anterior = str(i)

    def add(self):
        dron = self.sistemaenvaida.listaDrones.getInicio()   # Variable que almacena la lista de Tiempos
        contador = 1
        while dron:
            nombredron = dron.getDato().getNombreDron()
            self.dot.node(nombredron,label=nombredron,fillcolor='#95b8f6',shape="invhouse")
            self.dot.edge('cabeza',nombredron,dir="none")

            movimientos = dron.getDato().ListaMovimientos.getInicio()
            anterior = ""

            while movimientos:
                nombreTiempo="T"+str(contador)+str(movimientos.getDato().getTiempo())
                self.dot.node(nombreTiempo, label=str(movimientos.getDato().getMovimiento()),fillcolor='#f9d99a')
                if anterior == "":
                    self.dot.edge(nombredron,nombreTiempo,dir="both", color="#fa5f49:#95b8f6")
                
                else:   
                    self.dot.edge(anterior, nombreTiempo,dir="both", color="#fa5f49:#95b8f6")

                anterior = nombreTiempo
                movimientos = movimientos.getSiguiente()
            contador += 1
            dron = dron.getSiguiente()


    def generar(self):
       self.dot.render(outfile='img/'+str(self.nombre)+'.png').replace('\\', '/')
       'img/'+str(self.nombre)+'.png' 