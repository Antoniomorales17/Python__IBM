from inventario import Producto, Inventario

if __name__ == "__main__":
    inventario = Inventario()

    # Crear productos
    p1 = Producto("PlayStation 5", "Electrónica", 500, 10)
    p2 = Producto("Nintendo Swift", "Electrónica", 350, 25)
    p3 = Producto("Xbox SeriesX", "Electrónica", 550, 15)

    # Agregar productos al inventario
    inventario.agregar_producto(p1)
    inventario.agregar_producto(p2)
    inventario.agregar_producto(p3)

    # Mostrar inventario
    print("\nInventario inicial:")
    inventario.mostrar_inventario()

    # Actualizar cantidad y precio de un producto
    inventario.actualizar_producto("Nintendo Swift", nuevo_precio=700, nueva_cantidad=8)

    # Buscar un producto
    print("\nBuscar producto 'PlayStation 5':")
    inventario.buscar_producto("PlayStation 5")

    # Eliminar un producto
    inventario.eliminar_producto("PlayStation 5")


    # Mostrar inventario actualizado
    print("\nInventario después de eliminar 'PlayStation 5':")
    inventario.mostrar_inventario()
