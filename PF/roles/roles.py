import conexionBD
import hashlib
from prendas import prendas

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def registrar_admin(nombre, email, password, rol):
    prendas.borrarPantalla()
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
    prendas.borrarPantalla()
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

#notas = []

#def agregar_nota():
    inventario.borrarPantalla()
    nota = input("📝 Escribe tu nota: ").strip()
    if nota:
        notas.append(nota)
        print("✅ Nota guardada ✅")
    else:
        print("❌ No se escribió ninguna nota ❌")

#def ver_notas():
    inventario.borrarPantalla()
    print("\n📓 Notas internas:")
    if notas:
        for i, nota in enumerate(notas, 1):
            print(f"{i}. {nota}")
    else:
        print("❌ No hay notas guardadas ❌")