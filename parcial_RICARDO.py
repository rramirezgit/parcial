import csv
import os.path

def modificar(archivo,campos):
    cargar = "si"
    lista_Empleados = []
    while cargar == "si":
        empleado = {}
        for campo in campos:
            empleado[campo] = input(f"Ingrese {campo} del empleado: ")
        lista_Empleados.append(empleado)
        cargar = input("Desea seguir agregando empleados? Si/No")
    if modificar == "M":

        try:
            with open(archivo, 'a', newline='') as file:
                file_guarda = csv.DictWriter(file, fieldnames=campos)
             
                file_guarda.writerows(lista_Empleados)
                print(f"se guardo correctamente {archivo}")
                return
        except IOError:
            print("Ocurrio un error con el archivo")

def sobreescribir(archivo,campos):
    pass

def guardar_datos(campos):
    print("Ingrese nombre del archivo")
    ARCHIVO_DATOS = input("")

    archivo_existe = os.path.isfile(ARCHIVO_DATOS)
    if archivo_existe:
        print(f"El archivo ya existe, ¿desea Modificarlo o Sobreescribirlo? M/S")
        accion = input("").upper()
        #validacion de accion correcta M/S
        # corte = True
        # while corte:
        #     accion = input("")
        #     es_letra = accion.isalpha()            
        #     if es_letra == True:
        #         accion = accion.upper()                              
        #     else:
        #         print('ingrese una opcion valida')

        if accion == "M":
            modificar(ARCHIVO_DATOS,campos)
        if accion == "S":
            sobreescribir(ARCHIVO_DATOS,campos)
        else:
            print('ingrese una opcion valida')


def cargar_archivos(dias):
    pass
   

def menu():    
    CAMPOS = ['Legajo', 'Apellido', 'Nombre', 'Total Vacaciones']
    ARCHIVO_DIAS = "dias.csv"

    while True:

        print("Elija una opcion: \n 1.Guardar datos \n 2.Cargar datos \n 3.Salir")
        op = input("")
       
        if op == "1":
            guardar_datos(CAMPOS)
        if op == "2":
            cargar_archivos(ARCHIVO_DIAS)
        if op == "3":
            exit()
        else:
            print("Elija una opcion valida")

menu()

