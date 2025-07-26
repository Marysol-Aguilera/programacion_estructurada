import mysql.connector
from mysql.connector import Error
import os

def borrarPantalla():    
    os.system("clear")

def esperarTecla():
    input("Presione una tecla para continuar...")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_agenda"
        )
        return conexion
    except Error as e:
        print(f"❌ Error de conexión: {e}")
        return None

def agregar_contactos(agenda):
    borrarPantalla()
    print("📥 Agregar Contacto")
    nombre = input("Nombre: ").upper().strip()
    if nombre in agenda:
        print("⚠️ Este contacto ya existe")
    else:
        tel = input("Teléfono: ").strip()
        email = input("E-mail: ").strip().lower()
        agenda[nombre] = [tel, email]

        conexionBD = conectar()
        if conexionBD:
            cursor = conexionBD.cursor()
            sql = "insert into contactos (nombre, telefono, email) values (%s, %s, %s)"
            val = (nombre, tel, email)
            cursor.execute(sql, val)
            conexionBD.commit()
            print("✅ Contacto agregado con éxito")

def mostrar_contacto(agenda):
    borrarPantalla()
    print("📋 Mostrar Contactos")
    if not agenda:
        print("⚠️ No hay contactos registrados")
    else:
        for nombre, datos in agenda.items():
            print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<25}")
        print("-" * 60)

def buscar_contacto(agenda):
    borrarPantalla()
    print("🔎 Buscar Contacto")
    if not agenda:
        print("⚠️ No hay contactos registrados")
    else:
        nombre = input("Ingrese el nombre que desea buscar: ").upper().strip()
        if nombre in agenda:
            print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][1]:<25}")
        else:
            print("❌ El contacto no se encuentra en la agenda")

def modificar_contacto(agenda):
    borrarPantalla()
    print("✏️ Modificar Contacto")
    if not agenda:
        print("⚠️ No hay contactos en la agenda")
    else:
        nombre = input("Ingrese el nombre del contacto a modificar: ").upper().strip()
        if nombre in agenda:
            print(f"Nombre: {nombre}\nTeléfono: {agenda[nombre][0]}\nEmail: {agenda[nombre][1]}")
            resp = input("¿Deseas modificarlo? (SI/NO): ").upper().strip()
            if resp == "SI":
                tel = input("Nuevo teléfono: ").strip()
                email = input("Nuevo email: ").strip().lower()
                agenda[nombre] = [tel, email]

                conexionBD = conectar()
                if conexionBD:
                    cursor = conexionBD.cursor()
                    sql = "update contactos set telefono=%s, email=%s where nombre=%s"
                    val = (tel, email, nombre)
                    cursor.execute(sql, val)
                    conexionBD.commit()
                    print("✅ Contacto modificado con éxito")
        else:
            print("❌ Este contacto no existe")

def eliminar_contacto(agenda):
    borrarPantalla()
    print("🗑️ Eliminar Contacto")
    if not agenda:
        print("⚠️ No hay contactos en la agenda")
    else:
        nombre = input("Ingrese el nombre del contacto a eliminar: ").upper().strip()
        if nombre in agenda:
            resp = input("¿Deseas eliminarlo? (SI/NO): ").upper().strip()
            if resp == "SI":
                agenda.pop(nombre)

                conexionBD = conectar()
                if conexionBD:
                    cursor = conexionBD.cursor()
                    sql = "delete from contactos where nombre = %s"
                    val = (nombre,)
                    cursor.execute(sql, val)
                    conexionBD.commit()
                    print("✅ Contacto eliminado")
        else:
            print("❌ Este contacto no existe")