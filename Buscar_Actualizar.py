class Buscar():
    def __init__(self, registro):
        self.registro = registro

    def buscar_codigo(self, codigo):
        if codigo in self.registro.diccionario_productos:
            return self.registro.diccionario_productos[codigo]
        else:
            return "No se encontraron productos con ese código"

    def buscar_nombre(self, nombre):
        for producto in self.registro.diccionario_productos.values():
            if producto.nombre.lower() == nombre.lower():
                return producto
        return "No se encontraron productos con ese nombre"

    def buscar_categoria(self, categoria):
        for producto in self.registro.diccionario_productos.values():
            if producto.categoria.lower() == categoria.lower():
                return producto
        return "No se encontraron productos con ese precio"

    def buscar_en_diccionario(self, termino):
        termino = str(termino).lower()
        resultados = {}
        resultados.clear()

        for clave, obj in self.registro.diccionario_productos.items():
            if termino in str(obj):
                resultados[clave] = obj

        return resultados

class Modificar():
    def __init__(self, registro):
        self.registro = registro

    def eliminar_producto(self, codigo):
        for clave, obj in self.registro.diccionario_productos.items():
            if clave == codigo:
                print(f"Se ha eliminado el producto: ID: {clave} {obj}")
                self.registro.diccionario_productos.pop(clave)
                return

    def actualizar_precio(self,codigo, precio):
        for clave, obj in self.registro.diccionario_productos.items():
            if clave == codigo:
                print(f"Se ha actualizado el precio del producto de: ID: {clave} {obj}")
                self.registro.diccionario_productos[clave].precio = precio
                print(f"Al nuevo precio: ID: {clave} {obj}")
                return

