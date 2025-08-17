class Buscar():
    def __init__(self, registro):
        self.registro = registro

    def buscar_codigo(self, codigo):
        if codigo in self.registro.diccionario_productos:
            return self.registro.diccionario_productos[codigo].info_productos()
        else:
            return "No"

    def buscar_nombre(self, nombre):
        for producto in self.registro.diccionario_productos.values():
            if producto.nombre.lower() == nombre.lower():
                return producto.info_productos()
        return "No se encontraron productos con ese nombre"
#2