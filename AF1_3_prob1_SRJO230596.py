"""
1.-Crea un sistema para gestionar el inventario de 
productos de una tienda. Cada producto se representará 
como un objeto, y todos los productos se almacenarán 
en una lista. Cada objeto tendrá como atributos su nombre, 
precio y categoría. El sistema debe permitir agregar productos, 
consultarlos todos y consultar un producto en particular por su nombre.
"""
class Tienda:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    
    def getNombre(self):
        return self.nombre

    def MostrarInformacion(self):
        print(f"Nombre: {self.nombre} || Precio: {self.precio} || Categoria: {self.categoria}")

Productos = []
while input("Agregar producto [s]si [n]no:") == "s":
    Productos.append(Tienda(input("Inserta el nombre: "), float(input("Inserta el precio: ")), input("Inserta la categoria: ")))

while True: 
    opc = input("[1]Mostrar todos los productos\n[2]Buscar por nombre\n[3]Salir\n[Elige una opcion]$: ")
    if opc == '1':
        for prd in Productos:
            prd.MostrarInformacion()
    if opc == '2':
        nombre = input("Ingresa el nombre: ")
        for prd in Productos:
            if prd.getNombre() == nombre:
                prd.MostrarInformacion()
    if opc == '3': break
