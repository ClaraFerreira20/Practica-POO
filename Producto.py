class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre  # encapsulación
        self._precio = precio
        self._cantidad = cantidad

    def mostrar_info(self):
        return f"Nombre: {self._nombre}, Precio: ${self._precio:.2f}, Stock: {self._cantidad}"
