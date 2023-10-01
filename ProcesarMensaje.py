
from Movimientos import Movimientos


class procesar():

    def __init__(self, listainstrucciones, listadrones, mensaje):
        self.mensaje = mensaje
        self.listainstrucciones = listainstrucciones
        self.listadrones = listadrones
        self.eliminarMovimientosAnteriores()
        self.asignar()
        self.calcular()
        #self.pruebas()

    def eliminarMovimientosAnteriores(self):
        dron = self.listadrones.getInicio()
        while dron:
            movimiento = dron.getDato().ListaMovimientos
            total = movimiento.size
            
            if total != 0:
                for i in range (1, total+1):
                    movimiento.eliminarInicio()
            dron = dron.getSiguiente()
        

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


    def calcular(self):
        instruccion = self.listainstrucciones.getInicio()
        mensaje =  ""
        tiempo = 1

        while instruccion:
            DronInstruccion = instruccion.getDato().getNombreDron()
            posicion = instruccion.getDato().getPosicion()
            emitioluz = False
            #print(DronInstruccion,posicion)

            while emitioluz != True:
                dron = self.listadrones.getInicio()
                while dron:    
                    nombredron = dron.getDato().getNombreDron()
                    ubicaciondron = dron.getDato().ListaAlturas.getPosicion()

                    if ubicaciondron == None and tiempo == 1:  # Estamos validando que si se encuentra en la posición 0 que suba a la posicion 1
                        dron.getDato().ListaAlturas.setPosicion(dron.getDato().ListaAlturas.getInicio())
                        objmovimiento = Movimientos(tiempo,"Subir")
                        dron.getDato().ListaMovimientos.agregarFinal(objmovimiento)
                    else:
                        alt = ubicaciondron.getDato().getAltura()
                        if nombredron == DronInstruccion and int(alt) == int(posicion):
                            #print("Encontro",nombredron,str(alt),"en tiempo:",tiempo)
                            objmovimiento = Movimientos(tiempo,"Emitir luz")
                            dron.getDato().ListaMovimientos.agregarFinal(objmovimiento)
                            dron.getDato().ListaInstrucciones.desencolar()
                            mensaje += ubicaciondron.getDato().getValor()
                            emitioluz = True
                        else:
                            self.Movimientos(dron,ubicaciondron,tiempo)
                    dron = dron.getSiguiente()
                tiempo += 1
            instruccion = instruccion.getSiguiente()
            
        self.mensaje.getDato().setTiemnpoOptimo(tiempo-1)
        self.mensaje.getDato().setMensajedecifrado(mensaje)

        dron = self.listadrones.getInicio()
        while dron:
            dron.getDato().ListaAlturas.setPosicion(None)
            dron = dron.getSiguiente()
            

    
    def Movimientos(self,dron,ubicacion,tiempo):

        alt = ubicacion.getDato().getAltura()
        instruccion = dron.getDato().ListaInstrucciones.getInicio()
        if instruccion != None:
            posicion = instruccion.getDato()

            if int(alt) < int(posicion):
                objmovimiento = Movimientos(tiempo,"Subir")
                dron.getDato().ListaMovimientos.agregarFinal(objmovimiento)
                dron.getDato().ListaAlturas.setPosicion(ubicacion.getSiguiente())

            elif int(alt) > int(posicion):
                objmovimiento = Movimientos(tiempo,"Bajar")
                dron.getDato().ListaMovimientos.agregarFinal(objmovimiento)
                dron.getDato().ListaAlturas.setPosicion(ubicacion.getAnterior())

            else:
                objmovimiento = Movimientos(tiempo,"Esperar")
                dron.getDato().ListaMovimientos.agregarFinal(objmovimiento)
        else:
            objmovimiento = Movimientos(tiempo,"Esperar")
            dron.getDato().ListaMovimientos.agregarFinal(objmovimiento)
 


    def pruebas(self):
        print("tiempo total de ejecucion =",str(self.mensaje.getDato().getTeimpoObtimo()))
        print("mensaje obetnido =",self.mensaje.getDato().getMensajedecifrado())

        dron = self.listadrones.getInicio()        
        while dron:
            print("-----------------------------------------------")
            print("\n"+dron.getDato().getNombreDron())
            movimiento = dron.getDato().ListaMovimientos.getInicio()
            while movimiento:
                print(movimiento.getDato().getMovimiento())
                movimiento = movimiento.getSiguiente()
            dron = dron.getSiguiente()
        
        


