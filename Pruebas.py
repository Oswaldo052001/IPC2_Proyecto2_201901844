from Lista_Simple import ListaSimple
from Lista_DobleEnlazada import Lista_doble

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

#Valores2.imprimir()
print("------------------------------------")

valores3 = Lista_doble()
valores3.AgregarInicio(5)
valores3.AgregarInicio(8)
valores3.AgregarInicio(3)
valores3.AgregarInicio(1)
valores3.AgregarInicio(2)

valores3.imprimir_Adelante_atras()
valores3.imprimir_Atras_adelante()
