import os

# user = "admin"
# password = "admin"

while True:
    os.system("cls")
    print("\t\tSISTEMA DE GESTION DE HUESPEDES")
    print("1) Registrar Huesped")
    print("2) Consultar Datos Huesped")
    print("3) Salir")
    try:
        opcion = int(input("Ingrese una opcion\n"))
        if opcion == 1:
            os.system("cls")
            print("Registro Huesped")
            numresv = input("Ingrese su número de reserva\n")
            while numresv == "":
                # numresv = input()
                numresv = input("Ingrese número de reserva valido\n")

            nomhuesp= input("Ingrese su nombre, no acepta vacíos")
            while nomhuesp == "":
                nomhuesp= input("Ingrese su nombre, no acepta vacíos")

            direccion = input("Ingrese su dirección\n")
            while direccion == "":
                direccion = input("Ingrese su dirección, no acepta vacíos")

            email = input("Ingrese su correo electronico\n")
            while '@' not in email:
                email = input("Ingrese su correo\n")

            edad = input("Ingrese su edad\n")
            while edad < 18 or edad > 120:
                edad = int(input("Ingrese edad valida\n"))
            
            numacomp = input("Ingrese número de acompañantes\n")
            while numacomp == "":
                numacomp = input("ingresa numero valido")
        if opcion == 2:
            print("Consultar datos Huesped")      
    except:
        print("Opcion no existe")
    # print("Ha salido del sistema")