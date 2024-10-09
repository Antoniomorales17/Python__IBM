class Inventario:
    def __init__(self):
        self.__productos = []

         # Método para agregar producto
    def agregar_producto(self, producto):
        for prod in self.__productos:
            if prod.get_nombre() == producto.get_nombre():
                print(f"El producto '{producto.get_nombre()}' ya existe en el inventario.")
                return
        self.__productos.append(producto)
        print(f"Producto '{producto.get_nombre()}' agregado correctamente.")

          # Método para actualizar producto
    def actualizar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        for prod in self.__productos:
            if prod.get_nombre() == nombre:
                if nuevo_precio is not None:
                    prod.set_precio(nuevo_precio)
                if nueva_cantidad is not None:
                    prod.set_cantidad(nueva_cantidad)
                print(f"Producto '{nombre}' actualizado correctamente.")
                return
        print(f"El producto '{nombre}' no se encuentra en el inventario.")

        # Método para eliminar producto
    def eliminar_producto(self, nombre):
        for prod in self.__productos:
            if prod.get_nombre() == nombre:
                self.__productos.remove(prod)
                print(f"Producto '{nombre}' eliminado correctamente.")
                return
        print(f"El producto '{nombre}' no se encuentra en el inventario.")

         # Método para mostrar todos los productos
    def mostrar_inventario(self):
        if not self.__productos:
            print("El inventario está vacío.")
        else:
            print("\n{:<15} {:<15} {:<10} {:<10}".format("Nombre", "Categoría", "Precio", "Cantidad"))
            print("-" * 50)  
            for prod in self.__productos:
                print("{:<15} {:<15} ${:<9} {:<10}".format(prod.get_nombre(), prod.get_categoria(), prod.get_precio(), prod.get_cantidad()))

                 # Método para buscar un producto por nombre
    def buscar_producto(self, nombre):
        for prod in self.__productos:
            if prod.get_nombre() == nombre:
                print(prod)
                return
        print(f"El producto '{nombre}' no se encuentra en el inventario.")