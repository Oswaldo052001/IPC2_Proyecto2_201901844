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

            



    def crearGraficaReducida(self):

        
        self.dot.node('cabeza', label= self.sistemaenvaida.getNombre()+"\nreducida")
        self.dot.node('amplitud',label="A= "+self.sistemaenvaida.getAmplitudMaxima())
        self.dot.edge('cabeza','amplitud')

        lstTiempo = self.sistemaenvaida.ListaTiempos   # Variable que almacena la lista de Tiempos
        objtiempo = lstTiempo.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos  
        nombreanterior = ""

        while objtiempo != None:
            nombre = "G="+str(objtiempo.getDato().getTiempo())
            self.dot.node(nombre, str(nombre+"\nt("+objtiempo.getDato().getGrupo()+")"))

            if nombreanterior == "":
                self.dot.edge('cabeza',nombre)
            
            else:   
                self.dot.edge(nombreanterior, nombre)
            nombreanterior = nombre
            objtiempo = objtiempo.getSiguiente()

        self.add()
        self.generar()


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












        '''amplitudes = int(self.sistemaenvaida.getAmplitudMaxima())
        contador = 1

        while contador <= amplitudes:

            nombreAnterior = ""
            objtiempo = lstdrones.getInicio()     # Obteniendo el nodo inicial de la lista de tiempos  

            while objtiempo != None:
                objamplitud = objtiempo.getDato().ListaAmplitudes.getInicio()     # Obteniendo el nodo inicial de la lista de amplitudes

                while objamplitud != None:

                    if objamplitud.getDato().getAmplitud() == contador:
                        nombre = str(objtiempo.getDato().getTiempo())+"_"+str(objamplitud.getDato().getAmplitud())
                        self.dot.node(nombre, str(objamplitud.getDato().getValor()))

                        if nombreAnterior == "":
                            self.dot.edge('cabeza',nombre)
                        
                        else:   
                            self.dot.edge(nombreAnterior, nombre)

                        nombreAnterior = nombre

                    objamplitud = objamplitud.getSiguiente()
                objtiempo = objtiempo.getSiguiente()

            contador += 1'''


    def generar(self):
       self.dot.render(outfile='img/'+str(self.nombre)+'.png').replace('\\', '/')
       'img/'+str(self.nombre)+'.png' 