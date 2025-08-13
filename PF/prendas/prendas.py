import conexionBD
import funciones


def crear(id_proveedor, marca, tipo, talla, precio, color):
    funciones.borrarPantalla()
    conexion = conexionBD.obtener_conexion()
    if conexion is not None:
        cursor = conexion.cursor()
        sql = "INSERT INTO prendas (marca, tipo, talla, precio, color, id_proveedor) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (marca, tipo, talla, precio, color, id_proveedor)
        try:
            cursor.execute(sql, val)
            conexion.commit()
            print("\n\t\t  ✅ :::¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! ::: ✅ ")
            return True
        except Exception as e:
            print(f"\n\t❌ Error al insertar prenda: {e} ❌ ")
            return False
    else:
        print("\n\t ❌ Error al conectar con la base de datos ❌ ")
        return False

def mostrar(id_proveedor):
    funciones.borrarPantalla()
    conexion = conexionBD.obtener_conexion()
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM prendas WHERE id_proveedor = %s", (id_proveedor,))
            prendas = cursor.fetchall()
            if prendas:
                print("\n\t--- Tus Prendas Registradas ---")
                print(f"{'ID':<4} {'Marca 🏷️':<10} {'Tipo 👕':<10} {'Talla 📏':<10} {'Precio 💲':<10} {'Color 🎨':<10}")
                print("-"*70)
                for prenda in prendas:
                    print(f"{prenda[0]:<4} {prenda[1]:<10} {prenda[2]:<10} {prenda[3]:<10} {prenda[4]:<10}{prenda[5]:<10}")
            else:
                print("\n\t 📛 No tienes prendas registradas 📛")
        except Exception as e:
            print(f"\n\t ❌ Error al mostrar prendas: {e} ❌ ")
    else:
        print("\n\t ❌ Error al conectar con la base de datos ❌ ")

def buscar(id_proveedor):
    funciones.borrarPantalla()
    conexion = conexionBD.obtener_conexion()
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            tipo = input("\n\t 🔍 Ingrese el tipo de la prenda a buscar: ")
            cursor.execute("SELECT * FROM prendas WHERE tipo = %s AND id_proveedor = %s", (tipo, id_proveedor))
            prenda = cursor.fetchone()
            if prenda:
                print(f"{'ID':<4} {'Marca 🏷️':<10} {'Tipo 👕':<10} {'Talla 📏 ':<10} {'Precio 💲':<10} {'Color 🎨':<10}")
                print("-"*70)
                print(f"{prenda[0]:<4} {prenda[1]:<10} {prenda[2]:<10} {prenda[3]:<10} {prenda[4]:<10}{prenda[5]:<10}")
            else:
                print("\n\t 📛 Prenda no encontrada o no te pertenece. 📛")
        except Exception as e:
            print(f"\n\t ❌ Error al buscar prenda: {e} ❌")
    else:
        print("\n\t ❌ Error al conectar con la base de datos ❌")

def modificar(id_proveedor):
    funciones.borrarPantalla()
    mostrar(id_proveedor)
    conexion = conexionBD.obtener_conexion()
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            id_prenda = input("\n\t 🔄 Ingrese el ID de la prenda a modificar: ")
            cursor.execute( "SELECT tipo FROM prendas WHERE id_prenda = %s AND id_proveedor = %s",(id_prenda, id_proveedor))
            prenda = cursor.fetchone()

            if prenda:
                nombre_prenda = prenda[0]
                confirmacion = input(f"\n\t ⚠️ ¿Estás seguro que deseas modificar '{nombre_prenda}'? (Si/No): ").lower().strip()

                if confirmacion == "si":
                    marca = input("\tNueva marca 🏷️ : ").upper().strip()
                    tipo = input("\tNuevo tipo 👕 : ").upper().strip()
                    talla = input("\tNueva talla 📏 : ").upper().strip()
                    precio = input("\tNuevo precio 💲 : ").upper().strip()
                    color = input("\tNuevo color 🎨 : ").upper().strip()

                    sql = """UPDATE prendas SET marca = %s, tipo = %s, talla = %s, precio = %s, color = %s WHERE id_prenda = %s AND id_proveedor = %s"""
                    val = (marca, tipo, talla, precio, color, id_prenda, id_proveedor)
                    cursor.execute(sql, val)
                    conexion.commit()
                    print("\n\t ✅ Prenda modificada con éxito ✅")
                else:
                    print("\n\t ❌ Operación cancelada. ❌")
            else:
                print("\n\t 📛 No se encontró la prenda o no te pertenece 📛")
        except Exception as e:
            print(f"\n\t ❌ Error al modificar prenda: {e} ❌")
    else:
        print("\n\t ❌ Error al conectar con la base de datos ❌")

def borrar(id_proveedor):
    funciones.borrarPantalla()
    mostrar(id_proveedor)
    conexion = conexionBD.obtener_conexion()
    if conexion is not None:
        cursor = conexion.cursor()
        try:
            id_prenda = input("\n\t 📛Ingrese el ID de la prenda a eliminar: ")
            cursor.execute("SELECT tipo FROM prendas WHERE id_prenda = %s AND id_proveedor = %s",(id_prenda, id_proveedor))
            prenda = cursor.fetchone()

            if prenda:
                nombre_prenda = prenda[0]
                confirmacion = input(f"\n\t ⚠️ ¿Estás seguro que deseas eliminar '{nombre_prenda}'? (Si/No): ").lower().strip()

                if confirmacion == "si":
                    cursor.execute("DELETE FROM prendas WHERE id_prenda = %s AND id_proveedor = %s",(id_prenda, id_proveedor))
                    conexion.commit()
                    print("\n\t ✅ Prenda eliminada exitosamente. ✅")
                else:
                    print("\n\t ❌ Operación cancelada. ❌")
            else:
                print("\n\t 📛 No se encontró la prenda o no te pertenece 📛")

        except Exception as e:
            print(f"\n\t ❌ Error al eliminar prenda: {e} ❌")
    else:
        print("\n\t ❌ Error al conectar con la base de datos ❌")

def mostrar_prendas():
    funciones.borrarPantalla()
    conexion = conexionBD.obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT id_prenda, marca, tipo, talla, precio , color, id_proveedor FROM prendas")
            prendas = cursor.fetchall()
            print("\n📦 Inventario de prendas:")
            print(f"{'ID':<4} {'Marca 🏷️':<10} {'Tipo 👕':<10} {'Talla 📏':<10} {'Precio 💲':<10} {'Color 🎨':<10} {'Proveedor'}")
            print("-"*70)
            for fila in prendas:
                print(f"{fila[0]:<4} {fila[1]:<10} {fila[2]:<10} {fila[3]:<10} {fila[4]:<10} {fila[5]:<10} {fila[6]}")
        except Exception as err:
            print(f"❌ Error al obtener prendas: {err} ❌")
    else:
        print("❌ Error al conectar con la base de datos ❌")


