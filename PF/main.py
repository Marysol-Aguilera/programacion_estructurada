import getpass
from roles import roles
from proveedores import proveedores
from prendas import prendas
import funciones
from funciones import PDF
import conexionBD
import os 

def menu_proveedor(id_proveedor, nombre):
    while True:
        funciones.borrarPantalla()
        print(f"\n\t\t 🎉 Bienvenido {nombre}, has iniciado sesión ... 🎉")
        print("\n\t 1️⃣- Crear prenda")
        print("\t 2️⃣- Mostrar prendas")
        print("\t 3️⃣- Modificar prenda")
        print("\t 4️⃣- Buscar prenda")
        print("\t 5️⃣- Borrar prenda")
        print("\t 6️⃣- Salir")
        opcion = input("\n\tElige una opción: ").strip()

        if opcion == "1":
            funciones.borrarPantalla()
            print("\n\t 📝 Crear Prenda\n")
            marca = input("Marca 🏷️ : ").upper().strip()
            tipo = input("Tipo 👕 : ").upper().strip()
            talla = input("Talla 📏 : ").upper().strip()
            precio = input("Precio 💲 : ").upper().strip()
            color = input("Color 🎨 : ").upper().strip()
            if prendas.crear(id_proveedor, marca, tipo, talla, precio, color):
                print("\n ✅ Prenda registrada con éxito ✅")
            else:
                print("\n ❌ Error al registrar prenda ❌")
            funciones.esperarTecla()

        elif opcion == "2":
            prendas.mostrar(id_proveedor)
            funciones.esperarTecla()

        elif opcion == "3":
            prendas.modificar(id_proveedor)
            funciones.esperarTecla()

        elif opcion == "4":
            prendas.buscar(id_proveedor)
            funciones.esperarTecla()

        elif opcion == "5":
            prendas.borrar(id_proveedor)
            funciones.esperarTecla()

        elif opcion == "6":
            print("\n 🚪 Cerrando sesión... 🚪")
            funciones.esperarTecla()
            break

        else:
            print("\n ❌ Opción inválida, intenta de nuevo ❌")
            funciones.esperarTecla()


def menu_admin(nombre):
    notas = []
    while True:
        funciones.borrarPantalla()
        print(f"\n\t 🧾 - Menú de Administrador ({nombre}) - 🧾")
        print("\n\t 1️⃣ Ver inventario")
        print("\t 2️⃣ Consultar proveedores")
        print("\t 3️⃣ Crear nota")
        print("\t 4️⃣ Ver notas")
        print("\t 5️⃣ Cerrar sesión")
        opcion = input("\n\t Elige una opción: ").strip()

        if opcion == "1":
            prendas.mostrar_prendas()
            resp = input("\n📄 ¿Deseas descargar el inventario en PDF? (Si/No): ").lower().strip()
            if resp == "si":
                conexion = conexionBD.obtener_conexion()
                if conexion is not None:
                    cursor = conexion.cursor()
                    cursor.execute("SELECT id_prenda, marca, tipo, talla, precio, color FROM prendas")
                    Lista_inventario = cursor.fetchall()
                    conexion.close()

                    pdf = PDF()
                    pdf.add_page()
                    pdf.tabla_inventario(Lista_inventario)
                    pdf.output("inventario.pdf")
                    print("✅ PDF de inventario generado como 'inventario.pdf'")

                    try:
                        os.startfile("inventario.pdf")
                    except AttributeError:
                        print("⚠️ Apertura automática no soportada en este sistema.")
            funciones.esperarTecla()
        elif opcion == "2":
            proveedores.mostrar_proveedores()
            funciones.esperarTecla()
        elif opcion == "3":
            nota = input(" 📝 Escribe tu nota: ").strip()
            if nota:
                notas.append(nota)
                print("✅ Nota guardada ✅")
            else:
                print(" ❌ No se escribió ninguna nota ❌")
            funciones.esperarTecla()
        elif opcion == "4":
            print("\n📓 Notas internas:")
            if notas:
                for i, nota in enumerate(notas, 1):
                    print(f"{i}. {nota}")
            else:
                print(" ❌ No hay notas guardadas ❌")
            funciones.esperarTecla()
        elif opcion == "5":
            print("🚪 Cerrando sesión...🚪")
            funciones.esperarTecla()
            break
        else:
            print("❌ Opción no válida. Intenta otra vez ❌")
            funciones.esperarTecla()


def main():
    while True:
        funciones.borrarPantalla()
        print("\n\t\t 📋 .::: MENÚ PRINCIPAL :::. 📋 \n")
        print("\t 1️⃣- Registrar Proveedor")
        print("\t 2️⃣- Login Proveedor")
        print("\t 3️⃣- Registrar Administrador")
        print("\t 4️⃣- Login Administrador")
        print("\t 5️⃣- Salir")
        opcion = input("\n\tElige una opción: ").strip()

        if opcion == "1":
            funciones.borrarPantalla()
            print("\n\t 📝 Registro de Proveedor\n")
            nombre = input("Nombre 👤 : ").upper() .strip()
            telefono = input("Teléfono 📞 : ").strip()
            email = input("Email 📧 : ").strip()
            password = getpass.getpass("Contraseña 🔒 : ").strip()
            if proveedores.registrar_proveedor(nombre, telefono, email, password):
                print("\n ✅ Proveedor registrado con éxito ✅")
                funciones.esperarTecla()
            else:
                print("\n ❌ Error al registrar proveedor ❌")
                funciones.esperarTecla()
        
        elif opcion == "2":
           funciones.borrarPantalla()
           print("\n\t 🔑 Login de Proveedor\n")
           email = input("Email 📧 : ").strip()
           password = getpass.getpass("Contraseña 🔒 : ").strip()
           proveedor = proveedores.login_proveedor(email, password)
           if proveedor:
              print(f"\n 🎉 Bienvenido {proveedor[1]} 🎉 ")
              funciones.esperarTecla()
              menu_proveedor(proveedor[0], proveedor[1]) 
           else:
               print("\n ❌ Email o contraseña incorrectos ❌ ")
               funciones.esperarTecla()

        elif opcion == "3":
            funciones.borrarPantalla()
            print("\n\t 📝 Registro de Administrador\n")
            nombre = input("Nombre 👤 : ") .upper() .strip()
            email = input("Email 📧 : ").strip()
            password = getpass.getpass("Contraseña 🔒 : ").strip()
            rol = input("Rol (Ej. admin, supervisor): ").upper() .strip()
            if roles.registrar_admin(nombre, email, password, rol):
                print("\n ✅ Administrador registrado con éxito ✅")
            else:
                print("\n ❌ Error al registrar administrador ❌")
            funciones.esperarTecla()

        elif opcion == "4":
            funciones.borrarPantalla()
            print("\n\t 🔑 Login de Administrador\n")
            email = input("Email 📧 : ").strip()
            password = getpass.getpass("Contraseña 🔒 : ").strip()
            admin = roles.login_admin(email, password)
            if admin:
                print(f"\n 🎉 Bienvenido, {admin['nombre']} ({admin['rol']})")
                funciones.esperarTecla()
                menu_admin(admin['nombre'])
            else:
                print("❌ Credenciales incorrectas ❌ ")
                funciones.esperarTecla()

        elif opcion == "5":
            funciones.borrarPantalla()
            print("\n 🚪 Saliendo del sistema. ¡Gracias! 🚪")
            funciones.esperarTecla()
            break

        else:
            print("\n ❌ Opción inválida, intenta de nuevo ❌")
            funciones.esperarTecla()


if __name__ == "__main__":
    main()
