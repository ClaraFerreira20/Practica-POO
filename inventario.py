class Inventario:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def mostrar_productos(self):
        print("Productos disponibles:")
        for producto in self._productos:
            print(producto.mostrar_info())

    def procesar_compra(self, nombre_producto):
        for producto in self._productos:
            if producto._nombre.lower() == nombre_producto.lower():
                if producto._cantidad > 0:
                    producto._cantidad -= 1  # Reducir stock
                    print(f"Compraste: {producto.mostrar_info()}")
                    return
                else:
                    print("Producto fuera de stock.")
                    return
        print("Producto no encontrado.")