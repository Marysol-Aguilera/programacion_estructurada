'''
list(Array)
son colleciones o conjunto de datos/valores bajo
un mismo nombre, para acceder a los valoresse 
hace un indice numerico 

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modifiacable permita 
miembros duplicados
'''

import os
os.system("clear")

#Funciones mas comunes en las listas 
paises=["Mexico","España","Brasil","Canada"]

numeros=[23,45,0,24]

varios=["hola",3.1416,33,True]

#imprimir el contenido de una lista 
print(paises)
print(numeros)
print(varios)

#Recorrer la lista 
#1er forma 
for i in paises: #valores 
    print (i)

 #2do formas 
for i in range(0,len(paises)):  #posiciones  
    print(paises[i])

lista=""
for i in range(0,len(paises)):
    lista+=f"[{paises [i]}]"
    print(lista) 

#ordenar elementos de una lista
paises.sort()
print(paises)
numeros.sort
print(numeros)

#dar la vuelta a una lista 
paises.reverse()
print(paises)

varios.reverse()
print (varios)


#Agregar,insertar, añadir un elemento a una lista 
#1er forma 
paises.append ("Honduras")
print(paises)

#2da forma
paises.insert(1,"Honduras")
print(paises)

paises.sort()
print(paises)


#Eliminar, borrar, suprimir un elemento de una lista 
#1er forma 

paises.pop(4)
print(paises)

#2da forma 
paises.remove ("Honduras")
print(paises)

#buscar un elemento dentro de la lista 

resp="Brasil"in paises   #forma 1
print("Brasil" in paises )#forma 2

#contar el numero de veces que aparece un elemento dentro de una lista
print(numeros)

numeros.append ()
cuantos=numeros.count (23)
print(cuantos)

#Conocer la posicion o inice en el que se encuentra un elemento
paises.reverse()
print(paises)

posicion=paises.index("Canada")
print(f"El valor de canada lo encontro en la posicion {posicion}")

#unir el contenido de una lista dentro de otra 
print(numeros)
numeros2=[100.200]
print(numeros2)


#Crear a partir de las listas de numeros 1 y 2 un resultante y mostrar el contenido ordenado descendentemente 

numeros.extend (numeros2)
print(numeros)

numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)



