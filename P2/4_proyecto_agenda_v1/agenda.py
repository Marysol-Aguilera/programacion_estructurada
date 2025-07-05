
def borrarPantalla():
    import os
    os.system("clear")

def esperarTecla():
    input("🕒... Oprima cualquier tecla para continuar...🕒")  

def menu_principal():
    print("\n\t\t\t📝.:::Sitema de gestion de Agenda de contactos :::.📝")
    print("\n\t\t\t\t 1️⃣ Agregar Contacto \n\t\t\t\t 2️⃣ Mosrar todos los contactos \n\t\t\t\t 3️⃣ Buscar contacto por nombre \n\t\t\t\t 4️⃣ Modificar" \
    "\n\t\t\t\t 5️⃣ Eliminar contacto \n\t\t\t\t 6️⃣ Sallir")
    opcion=input("\n\t\t\t👉Elige una opcion (1-6")
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print ("\n\t\t📝 .::Agregar contactos::. 📝")
    nombre=input("\n\t\t👤 Nombre:") .upper() .strip()
    if nombre in agenda:
        print("\n\t\t.::Este contacto ya existe::.")
    else:
        tel=input("\n\t\t📞 Telefono:") .upper() .strip()
        email=input("\n\t\t📧 E-mail:") .strip()
        agenda[nombre]=[tel,email] 
        print("\n\t\t 🎉 .::Accion realizada con exito::. 🎉")   

def mostrar_contacto(agenda ):
    borrarPantalla()
    print ("\n\t\t 📂 .::Mostrar contactos::. 📂 ")
    if not agenda:
        print("\n\t\t .::No hay contactos en la agenda::.")
    else:
        print (f"{'👤 Nombre':<15} {'📞 Telefono':<15} {"📧 E-mail":<10}")
        print (f"-"*60)
        for nombre , datos in agenda.items():
            print (f"{nombre:<15} {datos[0]:<15} {datos[1]:<10}")
        print (f"-"*60)

def buscar_contacto(agenda ):
    borrarPantalla()
    print ("\n\t\t 🔍 .::Buscar contactos::. 🔍")
    if not agenda:
        print("\n\t\t .::No hay contactos en la agenda::.")
    else:
        nombre=input("\n\t\t 👤 Nombre del contacto a buscar") .upper() .strip()
        if nombre in agenda :
            print (f"{'👤 Nombre':<15} {'📞 Telefono':<15} {"📧 E-mail":<10}")
            print (f"-"*60)
            print (f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][1]:<10}")
            print (f"-"*60)
        else:
            print("\n\t\t .::Este contacto no existe::.")    

def modificar_contacto(agenda):
    borrarPantalla()
    print ("\n\t\t  🔄 .:::Modificar contactos::. 🔄")
    if not agenda:
        print("\n\t\t .::No hay contactos en la agenda::.")
    else:
        nombre=input("\n\t\t 👤 Nombre del contacto a modificar") .upper() .strip()
        if nombre in agenda :
            print("\n\t\tValores actuales")
            print (f"\n\t\t 👤 Nombre: {nombre}\n\t\t 📞 Telefono: {agenda[nombre][0]}\n\t\t 📧 E-mail: {agenda[nombre][1]}")
            resp=input("\n\t\tDeseas cambiar un valor?(si/no)") .lower() .split()
            if resp=="si":
                tel=input("\n\t\t 📞 Telefono:") .upper() .strip()
                email=input("\n\t\t 📧 E-mail:") .strip()
                agenda[nombre]=[tel,email]
                print("\n\t\t 🎉 .::Accion realizada con exito::. 🎉")
        else:
            print("\n\t\t .::Este contacto no existe::.")   

def eliminar_contacto(agenda):
    borrarPantalla()
    print ("\n\t\t 📛 .::Eliminar contactos::. 📛")
    if not agenda:
        print("\n\t\t .::No hay contactos en la agenda::.")
    else:
        nombre=input("\n\t\t Nombre del contacto a eliminar") .upper() .strip()
        if nombre in agenda :
            print("\n\t\t .::Valores actuales::.")
            print (f"\n\t\t 👤 Nombre: {nombre}\n\t\t 📞 Telefono: {agenda[nombre][0]}\n\t\t 📧 E-mail: {agenda[nombre][1]}")
            resp=input("\n\t\t Deseas eliminar los valores? (si/no)") .lower() .split()
            if resp=="si":
                agenda.pop(nombre)
                print("\n\t\t 🎉 .::Accion realizada con exito::. 🎉")  
        else:
            print("\n\t\t .::Este contacto no existe::.") 
