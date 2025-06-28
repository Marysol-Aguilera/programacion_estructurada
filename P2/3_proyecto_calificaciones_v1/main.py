#proyecto 3

import calificaciones



def main():
    datos =[]

    opcion=True
    while opcion==True:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()
        
        match opcion:
            case"1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla 
            case"2":
                calificaciones.mostrar_calificaciones (datos)
                calificaciones.esperarTecla
            case"3":
                calificaciones.mostrar_calificaciones (datos)
                calificaciones.esperarTecla
            case"4":
                opcion=False
                calificaciones.borrarPantalla()
                print("Terminaste la ejecucion del sistema")
            case _:
                opcion=True
                print(" ❌Opcion invalida, vuelva a intentarlo❌")
                calificaciones.esperarTecla 
                

if __name__=="__main__": #Modo consola
   main()

