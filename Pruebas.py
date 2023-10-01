from Lista_Simple import ListaSimple
from Lista_DobleEnlazada import Lista_doble
from Cola import Cola

Valores = ListaSimple()

Valores.agregarFinal(5)
Valores.agregarFinal(8)
Valores.agregarFinal(3)
Valores.agregarFinal(1)
Valores.agregarFinal(2)

#Valores.imprimir()

#print("*----------------------------------*")

Valores2 = ListaSimple()
Valores2.agregarInicio(5)
Valores2.agregarInicio(8)
Valores2.agregarInicio(3)
Valores2.agregarInicio(1)
Valores2.agregarInicio(2)



print("***********************************")
valor = Valores2.getInicio()
while valor:
    print(valor.getDato())
    valor = valor.getSiguiente()


total = Valores2.size


for i in range (1, total+1):
    Valores2.eliminarInicio()


valor2 = Valores2.getInicio()
print("Imprimiendo valores de la lista")
while valor2:
    print("entro")
    print(valor2.getDato())
    valor2 = valor2.getSiguiente()

#Valores2.imprimir()
print("------------------------------------")

valores3 = Lista_doble()
valores3.AgregarInicio(5)
valores3.AgregarInicio(8)
valores3.AgregarInicio(3)
valores3.AgregarInicio(1)
valores3.AgregarInicio(2)

#valores3.imprimir_Adelante_atras()
#valores3.imprimir_Atras_adelante()


v = Cola()
v.encolarDesorden(2)
v.encolarDesorden(6)
v.encolarDesorden(10)
v.encolarDesorden(12)

v.imprimir()
#v.desencolar()


totalnuevo = v.size
for i in range (1, totalnuevo+1):
    v.desencolar()


print("imprimiendo los valores de la cola")
v.imprimir()





palabra1 = "Dronx12"
palabra2 = "Drony12"



    
if palabra1 > palabra2:
    print("palabra1 es mayor que palabra2")

elif palabra1 < palabra2:
     print("palabra2 es mayor que palabra1")
else:
    print("Palabra1 es igual que palabra2")


hola = True

pa = "Hola1"
p2 = "hola1"

if pa.lower() == p2.lower():
    print("son iguales")
else:
    print("no son iguales")

for i in range (1, 5): 
    print(i)

if hola:
    print("holaaa")