peliculas=[]

def borrarPantalla():
    import os 
    os.system("clear")

def esperarTecla():
    input ("\n\t... Oprima cualquier tecla para continuar")

def agregarPeliculas():
    borrarPantalla()
    print("\n\t .:: Agregar peliculas::.\n")
    peliculas.append(input("ingrese el nombre "). upper() .strip())  
    print("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO ::")

def mostarPeliculas():
    borrarPantalla()
    print("\n\t .:: Mostrar TODAS las peliculas ::.\n")
    if len (peliculas)>0:
        for i in range (0,len (peliculas)):
            print(f"{i+1} :{peliculas [i]}")
    else:
        print("\n\t .:: No hay peliculas en este momento ")    

def limpiarPeliculas():
    borrarPantalla()
    print("\n\t .:: Limpiar o borrar TODAS las peliculas ::.\n")
    resp=input("deseas borrar todas las peliculas del sistema? (si/no)") .lower().strip()
    if resp=="si":
        peliculas.clear()
        print("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO ::")

def buscarPeliculas():
    borrarPantalla()
    print("\n\t .:: Buscar peliculas ::.\n")
    pelicula_buscar=input ("ingrese el nombre de la pelicula a buscar") . upper() .strip()
    if not (pelicula_buscar in peliculas):
        print("\n\t .:: Esta pelicula a buscaar no existe en el sitema::.")
    else:
        encontro=0
        for i in range (0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print (f"\n\t La pelicula {pelicula_buscar}se encontro en el casillero:{i+1}")
                encontro+=1
        print(f"\n Tenemos {encontro} peliculas(s)en ese titulo")
                
def modificarPeliculas():
    borrarPantalla()
    print("\n\t .:: Modificar peliculas ::.\n")
    pelicula_buscar=input ("ingrese el nombre de la pelicula a buscar") .upper() .strip()
    encontro=0
    if not (pelicula_buscar in peliculas):
        print("\n\t .:: Esta pelicula a buscar no existe en el sitema::.")
    else: 
        for i in range (0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                resp=input ("Deseas actualizar la pelicula?(Si/No)") .lower()
                if resp=="si":
                    peliculas[i]=input ("\n\t Introduce el numevo nombre de la pelicula") . upper() .strip()
                    encontro+=1
                    print("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO ::.")

        print (f"\n se modifico {encontro} pelicula(s) con este titulo ")        

def borrarPelicula():
    borrarPantalla()
    print("\n\t .:: Borrar peliculas ::.\n")
    pelicula_buscar=input ("ingrese el nombre de la pelicula que desea borrar: ") .upper() .strip()
    encontro=0
    if not (pelicula_buscar in peliculas):
        print("\n\t .:: Esta pelicula a borrar no existe en el sistema::.")
    else: 
        for i in range (0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                resp=input ("Deseas borrar la pelicula?(Si/No)") .lower()
                if resp=="si":
                    peliculas[i]=input ("\n\t Introduce el numevo nombre de la pelicula") . upper() .strip()
                    encontro+=1
                    print("\n\t\t ::: !LA OPERACION SE REALIZO CON EXITO ::.")

        print (f"\n se modifico {encontro} pelicula(s) con este titulo ")  


    