import mysql.connector

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_ropa"
        )
        return conexion
    
    except mysql.connector.Error as err:
        print(f"❌ Error al conectar a la base de datos: {err}")
        return None


