

class procesar():

    def __init__(self, listainstrucciones, listadrones):
        self.listainstrucciones = listainstrucciones
        self.listadrones = listadrones
        self.asignar()
        self.calcular()
        self.pruebas()

    
    def asignar(self):
        instruccion = self.listainstrucciones.getInicio()
        while instruccion:
            DronInstruccion = instruccion.getDato().getNombreDron()
            posicion = instruccion.getDato().getPosicion()
            dron = self.listadrones.getInicio()
            while dron:
                if dron.getDato().getNombreDron() == DronInstruccion:
                    dron.getDato().ListaInstrucciones.encolarDesorden(posicion)
                dron = dron.getSiguiente()
            instruccion = instruccion.getSiguiente()

            
        '''dron = lisdron.getInicio()
        while dron:
            nombre = dron.getDato().getNombreDron()
            lista = dron.getDato().ListaInstrucciones.getInicio()
            print(nombre)
            while lista:
                print(lista.getDato())
                lista = lista.getSiguiente()
            dron = dron.getSiguiente()'''


    def calcular(self):
        instruccion = self.listainstrucciones.getInicio()
        mensaje =  ""
        tiempo = 1

        while instruccion:
            DronInstruccion = instruccion.getDato().getNombreDron()
            posicion = instruccion.getDato().getPosicion()
            emitioluz = False
            terminorecorridodron = False
            #print(DronInstruccion,posicion)

            while emitioluz != True:
                
                dron = self.listadrones.getInicio()
     
                while dron:
                    
                    nombredron = dron.getDato().getNombreDron()
                    ubicaciondron = dron.getDato().ListaAlturas.getPosicion()


                    if ubicaciondron == None and tiempo == 1:  # Estamos validando que si se encuentra en la posición 0 que suba a la posicion 1
                        dron.getDato().ListaAlturas.setPosicion(dron.getDato().ListaAlturas.getInicio())
                        dron.getDato().ListaMovimientos.encolarDesorden("subir")

                    else:
                        alt = ubicaciondron.getDato().getAltura()
                        if nombredron == DronInstruccion and int(alt) == int(posicion):
                            print("Encontro",nombredron,str(alt),"en tiempo:",tiempo)
                            dron.getDato().ListaMovimientos.encolarDesorden("emerger luz")
                            dron.getDato().ListaInstrucciones.desencolar()
                            mensaje += ubicaciondron.getDato().getValor()
                            emitioluz = True
                        else:
                            self.Movimientos(dron,ubicaciondron)
                    
                    dron = dron.getSiguiente()
                tiempo += 1
            instruccion = instruccion.getSiguiente()
        
        print("tiempo total de ejecucion =",tiempo-1)
        print("mensaje obetnido =",mensaje)

    
    def Movimientos(self,dron,ubicacion):

        alt = ubicacion.getDato().getAltura()
        instruccion = dron.getDato().ListaInstrucciones.getInicio()
        if instruccion != None:
            posicion = instruccion.getDato()

            if int(alt) < int(posicion):
                dron.getDato().ListaMovimientos.encolarDesorden("subir")
                dron.getDato().ListaAlturas.setPosicion(ubicacion.getSiguiente())

            elif int(alt) > int(posicion):
                dron.getDato().ListaMovimientos.encolarDesorden("bajar")
                dron.getDato().ListaAlturas.setPosicion(ubicacion.getAnterior())

            else:
                dron.getDato().ListaMovimientos.encolarDesorden("esperar")
        else:
            dron.getDato().ListaMovimientos.encolarDesorden("esperar")


    def pruebas(self):
        dron = self.listadrones.getInicio()
        while dron:
            print("-----------------------------------------------")
            print("\n"+dron.getDato().getNombreDron())
            movimiento = dron.getDato().ListaMovimientos.getInicio()
            while movimiento:
                print(movimiento.getDato())
                movimiento = movimiento.getSiguiente()
            dron = dron.getSiguiente()
        
        


