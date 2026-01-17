"""
3.-Crear un sistema para gestionar un grupo de estudiantes, 
permitiendo registrar sus datos y calificaciones en diferentes 
materias.
"""
class Materia:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def mostrarMateria(self):
        print(f"\t\t\tNombre:{self.nombre}\n\t\t\t Calificacion:{self.calificacion}")

class Estudiante:
    def __init__(self, nombre, matricula, grado, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.grado = grado
        self.carrera = carrera
        self.materias = []
    
    def agregarMateria(self,materia):
        self.materias.append(materia)

    def mostrarEstudiante(self):
        print(f"[Estudiante]\n\tNombre: {self.nombre}\n\tMatricula:{self.matricula}\n\tGrado:{self.grado}\n\tCarrera:{self.carrera}")

estudiantes = []
while input("Agregar estudiante [s]si [n]no: ") == 's':
    estudiante = Estudiante(input("Ingresa el nombre: "), input("Ingresa la matricula: "), input("Ingresa el grado: "), input("Ingresa la carrera: "))
    
    while input("Agregar calificacion [s]si [n]no: ") == 's':
        estudiante.agregarMateria(Materia(input("Nombre de la materia: "), input("Calificacion: ")))
    estudiantes.append(estudiante)

for estudiante in estudiantes:
    estudiante.mostrarEstudiante()
    if estudiante.materias:
        print("\t\t[Materias]")
        for materia in estudiante.materias:
            materia.mostrarMateria()