import agenda

def main():
    agenda_contacto = {}
    while True:
        agenda.borrarPantalla()
        print("\n\t\t\t .::: SISTEMA DE AGENDA :::. \n\n\t 1.- Agregar contacto  \n\t 2.- Mostrar contactos \n\t 3.- Buscar contactos \n\t 4.- Modificar contacto \n\t 5.- Eliminar contacto \n\t 6.- Salir")
        opcion = input("\n\t\t Elige una opción: ").strip()

        match opcion:
            case "1":
                agenda.agregar_contactos(agenda_contacto)
                agenda.esperarTecla()
            case "2":
                agenda.mostrar_contacto(agenda_contacto)
                agenda.esperarTecla()
            case "3":
                agenda.buscar_contacto(agenda_contacto)
                agenda.esperarTecla()
            case "4":
                agenda.modificar_contacto(agenda_contacto)
                agenda.esperarTecla()
            case "5":
                agenda.eliminar_contacto(agenda_contacto)
                agenda.esperarTecla()        
            case "6":
                agenda.borrarPantalla()
                print(" Programa finalizado.")
                break
            case _:
                print("❌  Opción inválida, vuelve a intentarlo")
                agenda.esperarTecla()



if __name__ == "__main__":
    main()