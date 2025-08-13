import conexionBD
import hashlib
from prendas import prendas
import funciones

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def registrar_admin(nombre, email, password, rol):
    funciones.borrarPantalla()
    conexion = conexionBD.obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT * FROM roles WHERE email = %s", (email,))
            if cursor.fetchone():
                print("⚠️ Ya existe un administrador registrado con ese correo.")
                return False
            
            query = "INSERT INTO roles (nombre, email, password, rol) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nombre, email, hash_password(password), rol))
            conexion.commit()
            print("✅ Registro exitoso ✅")
            return True
        except Exception as err:
            print(f"❌ Error al registrar: {err} ❌")
            return False
    else:
        print("❌ Error al conectar con la base de datos ❌")
        return False
    
def login_admin(email, password):
    funciones.borrarPantalla()
    conexion = conexionBD.obtener_conexion()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        try:
            query = "SELECT * FROM roles WHERE email = %s AND password = %s"
            cursor.execute(query, (email, hash_password(password)))
            usuario = cursor.fetchone()
            return usuario
        except Exception as err:
            print(f"❌ Error en login: {err} ❌")
            return None
    else:
        print("❌ Error al conectar con la base de datos ❌")
    return None 
