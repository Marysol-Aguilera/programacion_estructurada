
import agenda 

def main():
    agenda_contactos={}

    opcion=True
    while opcion==True:
        agenda.borrarPantalla()
        opc=agenda.menu_principal()

        match opc:
            case "1":
                agenda.agregar_contacto (agenda_contactos)
                agenda.esperarTecla() 
            case "2":
                agenda.mostrar_contacto (agenda_contactos)
                agenda.esperarTecla()
            case "3": 
                agenda.buscar_contacto (agenda_contactos)
                agenda.esperarTecla()
            case "4":
                agenda.modificar_contacto (agenda_contactos)
                agenda.esperarTecla() 
            case "5":
                agenda.eliminar_contacto (agenda_contactos)
                agenda.esperarTecla()
            case "6": 
                agenda.borrarPantalla()
                print("Terminaste la ejecucion del sistema")
                opcion=False   
            case _ :
                opcion=True
                print(" ⚠️ Opcion invalida, vuelva a intentarlo ⚠️")
                agenda.esperarTecla()



if __name__=="__main__": #Modo consola
   main()    