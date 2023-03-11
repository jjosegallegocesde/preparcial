option = 1

empanadas = []

while option != 1:
    print("******Empanadas*********")
    print("Opcion 1 = Ingresar una empanada")
    print("Opcion 2 = Mostrar todas las empanadas Registradas")
    print("Opcion 3 = Buscar empanada por ID")
    print("Opcion 4 = Editar una empanada")
    print("Opcion 5 = Eliminar una empanada")
    print("Presiona 0 Para salir")
    option = int(input("Escoga opcion: "))
    if(option == 1):
        empanada = {}
        empanada['id'] = int(input("Digite el id de la empanada: "))
        empanada['nombre'] = input("Digite nombre de la empanda: ")
        empanada['precio'] = float(input("Digite el precio de la empanada: "))
        empanada['popularidad'] = int(input("Digite la popularidad de la empanada: "))
        empanada['fechavencimiento'] = input("Digite la popularidad de la empanada: ")
        empanadas.append(empanada)
        print("Empanada registrada...")


    elif(option == 2):
        for empanada in empanadas:
            print(empanada)
    elif(option == 3):
        empandadaBuscar=int(input('ingrese el id de empanada a buscar: '))
        for empanada in empanadas:
            if(empanada['id']!=empandadaBuscar):
                print('sin empanada')
            else:
                 print(f'empanada encontrada {empanada}')
    elif(option == 4):
        empandadaBuscar=int(input('ingrese el id de empanada a buscar: '))
        for empanada in empanadas:
            if(empanada['id']!=empandadaBuscar):
                print('sin empanada')
            else:
                print(f"precio actual de la empanada es: {empanada['precio']}")
                print(empanada["precio"])
                precioNuevo=float(input("Digita el nuevo precio: "))
                empanada["precio"]=precioNuevo


    elif(option == 5):
        pass
    elif(option == 0):
        pass
    else:
        print("Opción ivalida")
    




    
