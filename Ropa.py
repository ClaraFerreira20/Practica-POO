from Producto import Producto

class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, categoria):
        super().__init__(nombre, precio, cantidad)
        self._categoria = categoria

    def mostrar_info(self):
        base_info = super().mostrar_info()
        return f"{base_info}, Categoría: {self._categoria}"