# Sistema de Gestión de Inventario de Productos

Este es un sistema de gestión de inventario de productos desarrollado en Python utilizando Programación Orientada a Objetos (POO). Permite agregar, actualizar, eliminar y mostrar productos en un inventario.

## Enunciado del Ejercicio

Descripción: Crea una aplicación en Python para la gestión de un inventario de productos, usando programación orientada a objetos (POO). El sistema debe permitir agregar, actualizar, eliminar y mostrar productos en un inventario, cada uno de los cuales es representado como un objeto de la clase Producto.

### Requisitos:

1. **Clases y Objetos:**
   - Implementar una clase `Producto` con los siguientes atributos:
     - `nombre`: El nombre del producto.
     - `categoria`: La categoría a la que pertenece el producto.
     - `precio`: El precio del producto (debe ser mayor que 0).
     - `cantidad`: La cantidad en stock (debe ser mayor o igual que 0).
   - Implementar una clase `Inventario` que maneje una lista de productos y permita las siguientes operaciones:
     1. Agregar un producto: Verificar que el producto no exista previamente en el inventario.
     2. Actualizar un producto: Modificar el precio o la cantidad en stock de un producto ya existente.
     3. Eliminar un producto: Quitar un producto del inventario.
     4. Mostrar inventario: Listar todos los productos disponibles.
     5. Buscar un producto: Permitir buscar un producto por nombre.

2. **Validaciones:**
   - El precio debe ser siempre mayor que 0.
   - La cantidad debe ser mayor o igual que 0.
   - Manejar correctamente las excepciones y validar entradas (evitar que el usuario ingrese datos no válidos).

3. **Funciones y Métodos:**
   - Todos los atributos deben ser privados, utilizando getters y setters para acceder y modificar los valores.
   - Deben implementarse métodos para cada una de las funcionalidades mencionadas (agregar, actualizar, eliminar, etc.).

4. **Organización del Código:**
   - El código debe estar estructurado de manera que sea legible y modular.
   - Cada funcionalidad debe estar en un método de la clase correspondiente.
   - No se deben utilizar variables globales fuera de las clases.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:


### Clases

1. **Producto**
   - Atributos:
     - `nombre`: El nombre del producto.
     - `categoria`: La categoría a la que pertenece el producto.
     - `precio`: El precio del producto (debe ser mayor que 0).
     - `cantidad`: La cantidad en stock (debe ser mayor o igual que 0).
   - Métodos:
     - Getters y Setters para acceder y modificar los atributos.
     - Método `__str__` para representar el producto como una cadena.

2. **Inventario**
   - Atributos:
     - `__productos`: Una lista de objetos de la clase `Producto`.
   - Métodos:
     - `agregar_producto`: Permite agregar un producto al inventario (verifica si ya existe).
     - `actualizar_producto`: Actualiza el precio o la cantidad de un producto existente.
     - `eliminar_producto`: Elimina un producto del inventario.
     - `mostrar_inventario`: Muestra todos los productos disponibles en el inventario.
     - `buscar_producto`: Busca un producto por su nombre y lo muestra.

## Uso

Para ejecutar el sistema, asegúrate de tener Python instalado en tu computadora. Luego, ejecuta el archivo `main.py`:

```bash
python main.py
