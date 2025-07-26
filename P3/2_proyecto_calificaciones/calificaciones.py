
lista=[]

import mysql.connector
from mysql.connector import Error
 
def borrarPantalla():
    import os
    os.system("clear")

def esperarTecla():
    input("🕒... Oprima cualquier tecla para continuar...🕒")       
 

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"❌ Error de conexión: {e}")
        return None
 
def agregarCalificaciones():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n\t .:: Agregar Calificaciones ::.\n")
        alumno = {}  
        alumno["nombre"] = input("Ingresa el nombre del alumno: ").upper().strip()
        for i in range(1, 4):
            while True:
                try:
                    cal = float(input(f"Ingrese la calificación #{i}: "))
                    if 0 <= cal <= 10:
                        alumno[f"calificacion{i}"] = cal
                        break
                    else:
                        print("⚠️ La calificación debe estar entre 0 y 10")
                except ValueError:
                    print("❌ Ingresa un valor numérico válido")
 
        cursor = conexionBD.cursor()
        sql = "INSERT INTO calificaciones (nombre, calificacion1, calificacion2, calificacion3) VALUES (%s, %s, %s, %s)"
        val = (alumno["nombre"], alumno["calificacion1"], alumno["calificacion2"], alumno["calificacion3"])
        cursor.execute(sql, val)
        conexionBD.commit()
        print("\n✅ ¡Calificación registrada con éxito!")
    else:
        print("❌ No fue posible conectar a la base de datos")
 
def mostrarCalificaciones():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        sql = "SELECT nombre, calificacion1, calificacion2, calificacion3 FROM calificaciones"
        cursor.execute(sql)
        lista = cursor.fetchall()
       
        print("📋 Mostrar TODAS las calificaciones")
        if len(lista) > 0:
            print(f"{'Nombre':<15}  {'Calificación 1':<15}  {'Calificación 2':<15}  {'Calificación 3':<15}")
            print("-" * 60)
            for fila in lista:
                print(f"{fila[0]:<15}  {fila[1]:<15}  {fila[2]:<15}  {fila[3]:<15}")
            print("-" * 60)
            print(f"👥 Total de alumnos: {len(lista)}")
        else:
            print("⚠️ No hay calificaciones registradas")
    else:
        print("❌ No se pudo conectar a la base de datos")
 
def calcularCalificaciones():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        sql = "SELECT nombre, calificacion1, calificacion2, calificacion3 FROM calificaciones"
        cursor.execute(sql)
        lista = cursor.fetchall()
       
        print("📊 Promedios de los alumnos")
        if len(lista) > 0:
            print(f"{'Nombre':<15}  {'Promedio':<15}")
            print("-" * 40)
            promedio_grupal = 0
            for fila in lista:
                nombre = fila[0]
                promedio = sum(fila[1:]) / 3
                print(f"{nombre:<15}  {promedio:.2f}")
                promedio_grupal += promedio
            promedio_grupal = promedio_grupal / len(lista)
            print("-" * 40)
            print(f"📈 Promedio del grupo: {promedio_grupal:.2f}")
        else:
            print("⚠️ No hay calificaciones registradas")
    else:
        print("❌ No se pudo conectar a la base de datos")