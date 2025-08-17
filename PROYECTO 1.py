from Registrar_Listar import registro_productos
from Buscar_Actualizar import Buscar, Modificar
registrar = registro_productos()
busqueda = Buscar(registrar)
modificar = Modificar(registrar)
def menu():
    print("\n-----Menú-----\n1. Registrar producto\n2. Listar productos\n3. Buscar productos\n4. Actualizar producto\n5. Eliminar producto (por código)\n6. Salir")
def menuListarProductos():
    print("\n-----Listar Productos-----\n1. Por nombre\n2. Por precio\n3. Por stock\n4. Regresar")
def menuBusqueda():
    print("\n-----Buscar Productos-----\n1. Por código\n2. Por nombre\n3. Por categoria\n4. Busqueda por coincidencia\n5. Regresar")
def menuActulizarProductos():
    print("\n-----Actualizar Productos-----\n1. Actualizar precio\n2. Actualizar stock\n3. Actualizar precio y stock\n4. Regresar")

def listarProductos():
    while True:
        try:
            menuListarProductos()
            opciones = int(input("Elija una opción: "))
            match opciones:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    break
                case _:
                    print("Opción inválida, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")

def busquedaProductos():
    while True:
        try:
            menuBusqueda()
            opciones = int(input("Elija una opción: "))
            match opciones:
                case 1:
                    while True:
                        try:
                            codigo = int(input("Ingrese el código a buscar: "))
                            print(busqueda.buscar_codigo(codigo))
                            break
                        except Exception as ex:
                            print(f"Ha ocurrido un error: {ex}")
                case 2:
                    while True:
                        nombre = input("Ingrese el nombre a buscar: ")
                        print(busqueda.buscar_nombre(nombre))
                        break
                case 3:
                    while True:
                        categoria = input("Ingrese el categoria a buscar: ")
                        print(busqueda.buscar_categoria(categoria))
                        break
                case 4:
                    while True:
                        coincidencia = input("Ingrese el coincidencia a buscar: ")
                        if len(coincidencia) > 1:
                            encontrados = busqueda.buscar_en_diccionario(coincidencia)
                            if encontrados:
                                print("\nCoincidencias encontradas:")
                                for k, v in encontrados.items():
                                    print(f"ID {k}: {v}")
                                encontrados.clear()
                            else:
                                print("\nNo se encontraron coincidencias.")
                            break
                        else:
                            print("\nLa palabra para buscar por coincidencia debe tener más de 2 caracteres, reintente.")
                case 5:
                    break
                case _:
                    print("Opción inválida, reintente")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")

def actualizarProductos():
    if registrar.diccionario_productos:
        while True:
            try:
                menuActulizarProductos()
                opciones = int(input("Elija una opción: "))
                match opciones:
                    case 1:
                        while True:
                            try:
                                codigo = int(input("Ingrese el código del producto que le cambiará el precio: "))
                                if codigo in registrar.diccionario_productos:
                                    precio = float(input("Ingrese el precio nuevo que le dará : "))
                                    modificar.actualizar_precio(codigo, precio)
                                    break
                            except Exception as ex:
                                print(f"Ha ocurrido un error: {ex}")
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        break
                    case _:
                        print("Opción inválida, reintente")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
    else:
        print("No hay productos en el inventario.")

def eliminarProductos():
    if registrar.diccionario_productos:
        while True:
            try:
                cod = int(input("Ingrese el código del producto que va a eliminar: "))
                if cod > 0:
                    modificar.eliminar_producto(cod)
                    break
                else:
                    print("El código no es válido, reintente.")
            except Exception as ex:
                print(f"Ha ocurrido un error: {ex}")
    else:
        print("No hay productos en el inventario.")

def main():
    while True:
        try:
            menu()
            opciones = int(input("Elija una opción: "))
            match opciones:
                case 1:
                    registrar.registrar_productos()
                case 2:
                    listarProductos()
                case 3:
                    busquedaProductos()
                case 4:
                    actualizarProductos()
                case 5:
                    eliminarProductos()
                case 6:
                    print("Gracias por usar el sistema. . .")
                    break
                case _:
                    print("Opción inválida. . .")
        except Exception as ex:
            print(f"Ha ocurrido un error: {ex}")
main()