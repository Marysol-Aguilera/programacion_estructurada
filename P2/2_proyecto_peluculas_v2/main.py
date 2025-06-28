#Crear un proyecto que permita gestionar (administrar) peliculas. Colocar un menu de opciones para agregar, Borrar, Modificar, Mostrar, Buscar, Limpiar una lista de peliculas 
#Notas 
#1.-Utilizar funciones y mandar llamar desde otro archivo
#2.-Utilizar listas para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma) de peliculas 


import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("GESTION DE PELICULAS 1.Crear 2.Borrar 3.Mostrar  4.Agregar caracteristicas 5.Modificar caracteristica 6.Borrar caracteristica 7.Salir") 
    opcion=input("Elige una opcion:").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.espereTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
        case "4":
            peliculas.agregarCaracteristicaPeliculas()
            peliculas.espereTecla()
        case "5":
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.espereTecla()
        case "6":
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.espereTecla()
        case "7":
            opcion=False
            peliculas.borrarPantalla()
            print("Terminaste la ejecucion del sistema")
        case _:
            opcion=True
            print("Opcion invalida, vuelva a intentarlo")