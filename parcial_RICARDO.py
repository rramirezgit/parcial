import csv
import os.path

def cargar_empleado(campos):
    pregunta = "si"
    lista_Empleados = []
    while pregunta == "si":
        empleado = {}
        for campo in campos:
            ok = True
            while ok:
                print(f"Ingrese {campo} del empleado: ")
                dato = input("")
                if campo == 'Legajo' or campo == 'Total Vacaciones':
                    # validacion de numero para legajo y vacaciones
                    try:
                        dato = int(dato)
                        ok = False
                    except ValueError:
                        ok = True
                        print(f'El campo {campo} debe ser un numero')
                else:
                    ok = False

                empleado[campo] = dato     
        lista_Empleados.append(empleado)

        pregunta = input("Desea seguir agregando empleados? Si/No ")
    return lista_Empleados    


def modificar(archivo, campos):
    lista_Empleados = cargar_empleado(campos)
    try:
        with open(archivo, 'a', newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=campos)
            file_guarda.writerows(lista_Empleados)
            print(f"se guardo correctamente {archivo}")
            return
    except IOError:
        print("Ocurrio un error con el archivo")


def crear_sobreescribir(archivo, campos):
    lista_Empleados = cargar_empleado(campos)
    try:
        with open(archivo, 'w', newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=campos)

            file_guarda.writeheader()

            file_guarda.writerows(lista_Empleados)
            print(f"se guardo correctamente {archivo}")
            return
    except IOError:
        print("Ocurrio un error con el archivo")


def ingresar_archivo(archivo,campos):  
    archivo_existe = os.path.isfile(archivo)
    
    if archivo_existe:
        ok = True
        while ok:
            print(f"El archivo ya existe, ¿desea Modificarlo o Sobreescribirlo? M/S: ")
            accion = input("").upper()
            if accion == "M":
                modificar(archivo, campos)
                ok = False
            if accion == "S":
                crear_sobreescribir(archivo, campos)
                ok = False            
            else:
                print('ingrese una opcion valida')
    else:
        crear_sobreescribir(archivo, campos)
        return


def cargar_archivos(archivo,dias):
    empeados = open(archivo)
    dias = open(dias)
    archivo_empleados = csv.reader(empeados)
    archivo_dias = csv.reader(dias) 
    next(archivo_empleados)
    next(archivo_dias)
    empleados = next(archivo_empleados, None)
    dias_tomados = next(archivo_dias, None)

    validar = True
    while validar:
        valor = input(f"Ingrese el numero de legajo: ")
        try:
            valor = int(valor)
            validar = False
        except ValueError:
            validar = True
            print(f'El legajo debe ser un numero')

    contador_dias = 0
    while dias_tomados:
        if int(dias_tomados[0]) == valor:
            contador_dias += 1
        dias_tomados = next(archivo_dias, None)
    
    while empleados:
        if int(empleados[0]) == valor:
            total_dias_tomados = int(empleados[3])
            dias_restantes = total_dias_tomados - contador_dias
            print(f'Legajo {valor}: {empleados[1]} {empleados[2]}, le restan {dias_restantes} dias de vacaciones') 
        empleados = next(archivo_empleados, None)



def menu():
    CAMPOS = ['Legajo', 'Apellido', 'Nombre', 'Total Vacaciones']
    ARCHIVO_DIAS = "dias.csv"
    archivo_datos = ""

    while True:

        print("Elija una opcion: \n 1.Guardar datos \n 2.Cargar datos \n 3.Salir")
        op = input("")

        if op == "1":
            print("Ingrese nombre del archivo")
            archivo_datos = input("")
            ingresar_archivo(archivo_datos,CAMPOS)
        elif op == "2":          
            cargar_archivos(archivo_datos,ARCHIVO_DIAS)
        elif op == "3":
            exit()
        else:
            print("Elija una opcion valida")

menu()