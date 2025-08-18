class productos():
    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Stock: {self.stock}"

class registro_productos():
    def __init__(self):
        self.diccionario_productos = {}

    def registrar_productos(self):
        codigo = int(input("Ingrese el codigo: "))
        if codigo in self.diccionario_productos:
            print("El codigo ya esta en uso, intente de nuevo")
            return
        nombre = input("Ingrese el nombre: ").lower()
        categoria = input("Ingrese la categoria: ").lower()
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock: "))

        self.diccionario_productos[codigo] = productos(nombre, categoria, precio, stock)
        print("Se ha registrado con exito!")

    def info(self):
        if len(self.diccionario_productos) > 0:
            print("Productos Agregados")
            for producto in self.diccionario_productos.values():
                print(producto.info_productos())
        else:
            print("No hay productos registrados")
registro = registro_productos()

class quick_sorts():
    def quick_sort_nombre(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.nombre < pivote.nombre]
        iguales = [x for x in lista if x.nombre == pivote.nombre]
        mayores = [x for x in lista[1:] if x.nombre > pivote.nombre]
        return self.quick_sort_nombre(menores) + iguales + self.quick_sort_nombre(mayores)

    def quick_sort_precio(self, lista):
        if len(lista) <= 1:
            return  lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.precio < pivote.precio]
        iguales = [x for x in lista if x.precio == pivote.precio]
        mayores = [x for x in lista[1:] if x.precio > pivote.precio]
        return self.quick_sort_precio(menores) + iguales + self.quick_sort_precio(mayores)

    def quick_sort_stock(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.stock < pivote.stock]
        iguales = [x for x in lista if x.stock == pivote.stock]
        mayores = [x for x in lista[1:] if x.stock > pivote.stock]
        return self.quick_sort_stock(menores) + iguales + self.quick_sort_stock(mayores)