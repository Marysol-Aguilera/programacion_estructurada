'''
Crear un proyecto que permita gestionar (administrar ) peliculas Colocar un menu de opciones 
agregar, borrar, modificar, buscar,  limpiar una lista de peliculas 

notas:
1 utilizar funciones y mandar llamar desde otro archivo (modulo)
2 utilizar listas para almacenar los nombres de peliculas 

'''

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t.::: GESTION DE PELICULAS:::. \n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.-buacar \n\t 6.- limpiar   ")
    opcion=input("Elige una opcion ")

    match opcion:
        case"1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
        case"2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case"3":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case"4":
            peliculas.mostarPeliculas()
            peliculas.esperarTecla()
        case"5":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case"6":
            peliculas.limpiarPeliculas()
            peliculas.esperarTecla()
        case"7":
           opcion=False
           print("\n\t Terminaste la ejecución del sistema. Gracias")
        case _ :
            opcion=False
            print("\n\t Opción invalida vuelva a intentar") 

