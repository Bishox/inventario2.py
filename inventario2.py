import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga el inventario desde el archivo.
        """
        if not os.path.exists(self.archivo):
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
            with open(self.archivo, 'w') as f:
                pass  # Crea un archivo vacío si no existe
        
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        id_producto, nombre, cantidad, precio = datos
                        self.productos[id_producto] = Producto(id_producto, nombre, int(cantidad), float(precio))
            print("Inventario cargado exitosamente.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al cargar el archivo de inventario: {e}")
        except ValueError as e:
            print(f"Error de formato en el archivo de inventario: {e}")

    def guardar_inventario(self):
        """
        Guarda el inventario en el archivo.
        """
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos.values():
                    f.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("Inventario guardado exitosamente.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al guardar el archivo de inventario: {e}")

    def añadir_producto(self, producto):
        """
        Añade un producto al inventario.
        """
        if producto.id in self.productos:
            print(f"Error: Ya existe un producto con el ID {producto.id}.")
        else:
            self.productos[producto.id] = producto
            self.guardar_inventario()
            print(f"Producto añadido: {producto}")

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario.
        """
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print(f"Producto con ID {id} eliminado.")
        else:
            print(f"Error: No se encontró el producto con el ID {id}.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad y/o precio de un producto en el inventario.
        """
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            self.guardar_inventario()
            print(f"Producto actualizado: {producto}")
        else:
            print(f"Error: No se encontró el producto con el ID {id}.")

    def buscar_producto_por_nombre(self, nombre):
        """
        Busca productos por nombre.
        """
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_productos(self):
        """
        Muestra todos los productos en el inventario.
        """
        if not self.productos:
            print("No hay productos en el inventario.")
        for producto in self.productos.values():
            print(producto)

def imprimir_arte_ascii_inventario():
    arte_ascii = '''
     _________
     /         /|
    /_________/ |
   | _______  | |
   ||       || | |
   ||       || | |
   ||_______|| | |
   |_________|/  
   | INVENTARIO |
   |___________|               
    '''
    print(arte_ascii)

def obtener_numero_positivo(prompt):
    while True:
        try:
            valor = int(input(prompt))
            if valor < 0:
                raise ValueError("El valor debe ser un número positivo.")
            return valor
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un número válido.")

def obtener_numero_flotante(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

def menu():
    inventario = Inventario()
    
    while True:
        imprimir_arte_ascii_inventario()
        print("\nMenú de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = obtener_numero_positivo("Ingrese cantidad del producto: ")
            precio = obtener_numero_flotante("Ingrese precio del producto: ")
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad_input = input("Ingrese nueva cantidad del producto (deje en blanco para no cambiar): ")
            precio_input = input("Ingrese nuevo precio del producto (deje en blanco para no cambiar): ")
            cantidad = int(cantidad_input) if cantidad_input else None
            precio = float(precio_input) if precio_input else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 6.")

if __name__ == "__main__":
    # Crear el archivo vacío si no existe
    archivo = 'inventario.txt'
    if not os.path.exists(archivo):
        try:
            with open(archivo, 'w') as f:
                pass  # Solo se necesita abrir el archivo en modo escritura para crearlo
            print(f"Archivo '{archivo}' creado exitosamente en el directorio actual.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al crear el archivo '{archivo}': {e}")
        except Exception as e:
            print(f"Error inesperado al crear el archivo '{archivo}': {e}")

    # Ejecutar el menú
    menu()
