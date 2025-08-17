from Registrar_Listar import registro_productos
from Buscar_Actualizar import Buscar
registrar = registro_productos()
busqueda = Buscar(registrar)

def menu():
    print("\n-----Menú-----\n1. Registrar producto\n2. Listar productos\n3. Buscar productos\n4. Actualizar producto\n5. Eliminar producto\n6. Salir")
def menuListarProductos():
    print("\n-----Listar Productos-----\n1. Por nombre\n2. Por precio\n3. Por stock\n4. Regresar")
def menuBusqueda():
    print("\n-----Buscar Productos-----\n1. Por código\n2. Por nombre\n3. Por categoria\n4. Regresar")
def menuActulizarProductos():
    print("\n-----Actualizar Productos-----\n1. Actualizar precio\n2. Actualizar stock\n3. Actualizar precio y stock\n4. Regresar")

def busquedaProductos():
    while True:
        try:
            menuBusqueda()
            opciones = int(input("Elija una opción: "))
            match opciones:
                case 1:
                    while True:
                        try:
                            codigo = int(input("Ingrese código: "))
                            print(busqueda.buscar_codigo(codigo))
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

def actualizarProductos():
    while True:
        try:
            menuActulizarProductos()
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

def eliminarProductos():
    pass

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