Sistema de Gestión de Inventario
Este proyecto es un sistema simple de gestión de inventario en Python. Permite añadir, eliminar, actualizar y buscar productos en un archivo de texto llamado inventario.txt.

Características
Añadir Producto: Permite añadir un nuevo producto al inventario.
Eliminar Producto: Permite eliminar un producto existente del inventario.
Actualizar Producto: Permite actualizar la cantidad y/o precio de un producto existente.
Buscar Producto por Nombre: Permite buscar productos por su nombre.
Mostrar Todos los Productos: Muestra todos los productos almacenados en el inventario.
Persistencia en Archivo: Los productos se guardan en un archivo inventario.txt en el directorio actual.

Requisitos
Python 3.x
Instalación
Clona el repositorio:

bash
Copiar código
git clone https://github.com/tu_usuario/nombre_del_repositorio.git
Navega al directorio del proyecto:

bash
Copiar código
cd nombre_del_repositorio
Uso
Ejecuta el script:

bash
Copiar código
python nombre_del_archivo.py
Selecciona una opción del menú para gestionar el inventario:

1. Añadir producto: Introduce el ID, nombre, cantidad y precio del nuevo producto.
2. Eliminar producto: Introduce el ID del producto a eliminar.
3. Actualizar producto: Introduce el ID del producto a actualizar, y la nueva cantidad y/o precio.
4. Buscar producto por nombre: Introduce el nombre del producto para buscar.
5. Mostrar todos los productos: Muestra todos los productos actualmente en el inventario.
6. Salir: Sale del sistema.
Ejemplo de Uso
Al ejecutar el script, el programa mostrará un menú con opciones para gestionar el inventario. Los productos se almacenarán en inventario.txt en el mismo directorio del script. Si el archivo no existe, se creará automáticamente al iniciar el programa.

Ejemplo de Salida
plaintext
Copiar código
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

Menú de Gestión de Inventarios
1. Añadir producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto por nombre
5. Mostrar todos los productos
6. Salir
Seleccione una opción (1-6): 
Contribuciones
Las contribuciones son bienvenidas. Si tienes sugerencias para mejorar el proyecto, por favor abre un issue o envía una pull request.

Licencia
Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.
