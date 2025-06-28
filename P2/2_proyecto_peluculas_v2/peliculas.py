
#Dict u objeto que permita almacenar los siguientea atributos (nombre, categoria, clasificacion, genero, idioma) de peliculas 


#pelicula={
#    "nombre":"",
 #  "clasificacion":"",
#  "genero":"",
#   "idioma":""
#}

pelicula={}

def borrarPantalla():
    import os
    os.system("clear")

def espereTecla():
    input("Oprima cualquier tecla para continuar")

def crearPeliculas():
    borrarPantalla()
    print( "agregar peliculas")
    pelicula.update({"nombre ": input ("ingresa el nombre "). upper().strip()})
    #pelicula["nombre"]=input("ingresa el nombre:") .upper().strip()
    pelicula.update({"categoria ": input ("ingresa la categoria "). upper().strip()})
    pelicula.update({"clasificacion ": input ("ingresa la clasificacion "). upper().strip()})
    pelicula.update({"genero ": input ("ingresa el genero  "). upper().strip()})
    pelicula.update({"idioma ": input ("ingresa el idioma "). upper().strip()})
    print("\n\t :::!LA OEPRACION SE REALIZO CON EXITO!")

def mostrarPeliculas():
    borrarPantalla()
    print("Mostrar peluculas")
    if len (pelicula)>0:
        for i in pelicula:
            print (f"{i}:{pelicula[i]}")
    else:
        print("\n\t .:: No hay peliculas en este momento ") 

def borrarPeliculas():
    borrarPantalla()
    print(" Borrar o quitar la  peluculas")
    if len (pelicula)>0:
        resp=input("Deseas borrar o quitar la pelicula ?(Si/NO)")
        if resp=="si":
            pelicula.clear
            print("\n\t :::!LA OEPRACION SE REALIZO CON EXITO!")
    else:
        print("\n\t .:: No hay peliculas en el sistema  ") 
       
def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print( "Agregar Caracteristica de pelicula")
    atributo=input("ingresa el nombre de la nueva caracteristica que deseas agregar"). lower(). strip()
    valor_atributo=input("ingresa el nombre de la nueva caracteristica que deseas agregar"). upper(). strip()
    #pelicula.update({atributo : valor_atributo})
    pelicula[atributo].upper() .strip()
    print("\n\t :::!LA OEPRACION SE REALIZO CON EXITO!")



def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print( " Modificar Caracteristica de pelicula")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i} : {pelicula}")
            resp=input (f"deseas modificar el valor de la caractgeristica{i}? (si/no)") . lower() .split()
            if resp=="si":
                valor=input(f"ingrese el nuevo valor de la caracteristica {i}") .upper(). split()
                pelicula[i]=valor 
                print("\n\t :::!LA OEPRACION SE REALIZO CON EXITO!")
                espereTecla()
    else:
        print("")

       
def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print(" Borrar Caracteristica de pelicula")
    print(" Valores actuales: ")
    mostrarPeliculas()
    resp=input("Deseas borrar alguna caracteristica? (Si/No)") .lower() .split()
    if not (resp in pelicula):
        print("\n\t .:: Esta pelicula a borrar no existe en el sistema::.")
    else: 
        for i in range (0,len(pelicula)):
            if resp==pelicula[i]:
                resp=input (" Deseas borrar la pelicula?(Si/No)") .lower()
                if resp=="si":
                    pelicula[i]=input ("\n\t Introduce el numevo nombre de la pelicula") . upper() .strip()
                    encontro+=1
                    print("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO ::.")

        print (f"\n se modifico {encontro} pelicula(s) con este titulo ")  