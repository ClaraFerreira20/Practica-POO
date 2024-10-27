from Ropa import Ropa
from inventario import Inventario

def main():
    inventario = Inventario()

    # Creamos algunos productos
    camisa = Ropa("Camisa", 25.99, 10, "Camisas")
    pantalon = Ropa("Pantalón", 39.99, 20, "Pantalones")
    zapatos = Ropa("Zapatos", 49.99, 15, "Calzado")

    # Agregar productos al inventario
    inventario.agregar_producto(camisa)
    inventario.agregar_producto(pantalon)
    inventario.agregar_producto(zapatos)

    while True:
        inventario.mostrar_productos()
        eleccion = input("Ingrese el nombre del producto que desea comprar (o 'salir' para terminar): ").strip()
        
        if eleccion.lower() == 'salir':
            break
        
        inventario.procesar_compra(eleccion)

if __name__ == "__main__":
    main()