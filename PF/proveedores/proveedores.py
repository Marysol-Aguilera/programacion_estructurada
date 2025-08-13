import conexionBD
import hashlib
import funciones 

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def registrar_proveedor(nombre, telefono, email, password):
    funciones.borrarPantalla()
    try:
        conexion = conexionBD.obtener_conexion()
        if conexion is None:
            print("❌ Error al conectar con la base de datos ❌")
            return False

        cursor = conexion.cursor()
        password_hash = hash_password(password)

        cursor.execute("SELECT * FROM proveedores WHERE email = %s", (email,))
        if cursor.fetchone():
            print("⚠️ El proveedor ya está registrado con ese correo.")
            return False

        sql = "INSERT INTO proveedores (nombre, telefono, email, password) VALUES (%s, %s, %s, %s)"
        valores = (nombre, telefono, email, password_hash)
        cursor.execute(sql, valores)
        conexion.commit()
        return True
    
    except Exception as e:
        print("❌ Error en registrar_proveedor: ❌ ", e )
        return False
    
def login_proveedor(email, password):
    funciones.borrarPantalla()
    try:
        conexion = conexionBD.obtener_conexion()
        if conexion is None:
            print("❌ Error al conectar con la base de datos ❌")
            return None

        cursor = conexion.cursor()
        sql = "SELECT id_proveedor, nombre, password FROM proveedores WHERE email = %s"
        cursor.execute(sql, (email,))
        resultado = cursor.fetchone()

        if resultado:
            id_proveedor, nombre, password_hash = resultado
            if hash_password(password) == password_hash:
                return (id_proveedor, nombre)
        return None
    except Exception as e:
        print("❌ Error en login_proveedor: ❌", e)
        return None

def mostrar_proveedores():
    funciones.borrarPantalla()
    conexion = conexionBD.obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT id_proveedor, nombre, telefono, email FROM proveedores")
            proveedores = cursor.fetchall()
            print("\n📋 Lista de proveedores:")
            print(f"{'ID':<4} {'Nombre 👤':<20} {'Teléfono 📞':<12} {'Email 📧'}")
            print("-"*55)
            for p in proveedores:
                print(f"{p[0]:<4} {p[1]:<20} {p[2]:<12} {p[3]}")
        except Exception as err:
            print(f"❌ Error al obtener proveedores: {err} ❌")
    else:
        print("❌ Error al conectar con la base de datos ❌")