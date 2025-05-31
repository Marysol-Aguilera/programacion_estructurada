import os

os.system("clear")
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
num=[14,60,45,92,57,36]
print(num)


lista=""
for i in num:
    lista+=f"{i}"
print(f"{lista}]")  


lista=""
for i in range (0,len(num)):
    lista+=f"{num[1]}"
print(f"{lista}]")  

lista=""
i=0
while i<len(num ):
    lista+=f"{num[i]}"
    i+=1
print(f"{lista}]")  


#Ejemplo 2 Crear un lista de palabras y posteriormente buscar la coicidencia de una palabras
os.system("clear")

palabras=["hola","2023", "true","UTD"]
print(palabras)
palabra_buscar=input ("Dame la palabra a buscar ")

#1
if palabra_buscar in palabras:
    print ("Si se encontro la palabra en la lista")
else:
     print ("No se encontro la palabra en la lista")  

#2
for i in palabras:
    if i==palabra_buscar:
        print ("Si se encontro la palabra en la lista")
    else:
        print ("No se encontro la palabra en la lista") 

encontro=False
cuantas=0
posiciones=[]
for i in palabras:
    if i==palabra_buscar:
      encontro=True
      cuantas+=1
      posiciones.append(palabras.index[i])
if i==palabra_buscar:
    print ("Si se encontro la palabra en la lista")
else:
    print ("No se encontro la palabra en la lista")     

#3
encontro=False
cuantas=0
posiciones=[]
for i in range(0,len(palabras)):
    if palabras[i]==palabra_buscar:
      encontro=True
      cuantas+=1
      posiciones.append 
if encontro:
    print ("Si se encontro la palabra en la lista")
else:
    print ("No se encontro la palabra en la lista")


#Ejemplo 3 añadir elementos a una lista 
frutas=["Manzana","Fresa","Pera","Moras"]
frutas.insert(1,"Platano")
print(frutas)

numeros=[]
opc="si"
while opc=="si":
    numeros.append(float(input("Dame un numero entero o decimal:")))
    opc=input("Deseas agrear otro numero a al lista?(Si/No)").lower
    print(numeros)

#Ejemplo 4 Crear una lista multidimencinal que permita almacenar el nombre y telefono de una agenda 

agenda=[
    
]

