
lista=[]

def borrarPantalla():
    import os
    os.system("clear")

def esperarTecla():
    input("Oprima cualquier tecla para continuar")    

def menu_principal():
    print("\n\t\t\t📝.:::Sitema de gestion de calificaciones :::.📝 \n\t\t\t\t 1️⃣ Agregar \n\t\t\t\t 2️⃣ Mosrar \n\t\t\t\t 3️⃣ Calcular Promeios \n\t\t\t\t 4️⃣ Buscar \n\t\t\t\t 5️⃣ SALIR  ")
    opcion=input("\n\t\t\t👉Elige una opcion (1-4):")
    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    print("Agregar calificaciones")
    nombre=input("Nombre del alumno:") .upper() .strip()
    calificaciones=[]
    for i in range (1,4):
        continua=True
        while continua==True:
            try:
                calificaciones.append=(float(input(f"Calificacion #{i}:")))
                cal=(float(input(f"Calificacion #{i}:")))
                if cal>=0 and cal<=10:
                    calificaciones.append(cal)
                    continua=False

                else:
                    print("Ingresa un valor comprendido entre el 0 y el 10")
            except ValueError:
                print("Ingresa un valor numerico")
    lista.append ([nombre]+calificaciones)

    print("Accion realizada con exito")                          

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("Mostrar las calificaciones")
    if len (lista)>0:
        print (f"{'Nombre':<15}{'Calif.1':<10}{'Calif.2':<10}{'Calif.3':<10}")
        print("-"*50)
        for fila in lista:
            print(f"{fila[0]:<15} {fila[1]:<10}  {fila[2]:<10} {fila[2]:<10}")
        print("-"*50)
        cuantos=len(lista)
        print(f"Son {cuantos} alumnos")
    else:
        print("No hay calificaciones")        

def calcular_promedios(lista):
    borrarPantalla()
    print("Promedios de los alumnos ")
    if len (lista)>0:
        print (f"{'Nombre':<15}{'Promedio':<10}")
        print("-"*50)
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            #promedio=(fila[1]+fila[2]+fila[3])/3
            promedio=sum(fila[1:])/3
            print (f"{nombre:<15}{promedio:<10}")
            promedio_grupal+=promedio
        print("-"*50)
        promedio_grupal=promedio_grupal/len(lista)
        print(f"EL promedio grupal es {promedio_grupal:.2f}")
    else:
        print("No hay calificaciones en el sistema")        
