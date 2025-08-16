opciones = 0
a = False
while a == False:
    print("\n-----Menu-----\n1. Registrar producto\n2. Listar productos\n3. Buscar productos\n4. Actualizar producto\n5. Eliminar producto\n6. Salir")
    opciones = int(input("Elija una opcion: "))
    match opciones:
        case 1:
            pass
        case 2:
            opciones1 = 0
            b = False
            while b == False:
                print("\n----Listar Productos----\n1. Por nombre\n2. Por precio\n3. Por stock\n4. Regresar")
                opciones1 = int(input("Elija una opcion: "))
                match opciones1:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        b = True
                    case _:
                        print("Opcion invalida")
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            print("Gracias por usar el sistema")
            a = True
        case _:
            print("Opcion invalida")