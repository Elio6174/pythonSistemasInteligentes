"""
2.-Crear un sistema que permita a los usuarios crear, 
listar y actualizar tareas. Cada tarea tendrá subtareas, 
y estas se almacenarán en listas dentro de los objetos Tarea"""

class Subtarea:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def mostrarSubtarea(self):
        print(f"\t\t\tNombre de la subtarea: {self.nombre} Descripcion: {self.descripcion}")

class Tarea:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.subtareas = []

    def agregarTarea(self, tarea):
        self.subtareas.append(tarea)

    def mostrarTarea(self):
        print(f"[Tarea]\n\tNombre de la tarea: {self.nombre} Descripcion: {self.descripcion}")

tareas = []
while input("Agregar tarea [s]si [n]no: ") == 's':
    tarea = Tarea(input("Ingresa el nombre de la tarea: "), input("Ingresa la descripcion de la tarea: "))
    
    while input("Agregar subtarea [s]si [n]no: ") == 's':
        tarea.agregarTarea(Subtarea(input("Nombre de la subtarea: "), input("Descripcion de la subtarea: ")))
    tareas.append(tarea)

for tarea in tareas:
    tarea.mostrarTarea()
    if tarea.subtareas:
        print("\t\t[Subtareas]")
        for sub in tarea.subtareas:
            sub.mostrarSubtarea()