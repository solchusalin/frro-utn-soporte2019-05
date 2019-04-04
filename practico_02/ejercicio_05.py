import random

class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = self.generar_dni()

    def generar_dni(self):
        dni = random.randrange(100000000)
        return dni

class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        Persona.__init__(self, nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas


def organizar_estudiantes(estudiantes):
    carreras = []
    alumnos = {}

    for i in estudiantes:
        if (i.carrera not in carreras):
            carreras.append(i.carrera)

    for j in carreras:
        cant_alumnos = 0
        for k in estudiantes:
            if (k.carrera ==  j):
                cant_alumnos += 1
                alumnos[k.carrera] = cant_alumnos

    return alumnos



e1 = Estudiante("Julian", 19, 'H', 65, 1.72, "Ing. en Sistemas de Información", 2018, 38, 8)
e2 = Estudiante("Mauro", 23, 'H', 75, 1.84, "Ingeniería Mecánica", 2014, 40,30 )
e3 = Estudiante("Laura", 25, 'M', 62, 1.62, "Ingeniería Mecánica", 2013, 40, 20)
e4 = Estudiante("Luz", 19, 'M', 67, 1.65, 'Ingeniería Química', 2018, 38, 7)
e5 = Estudiante("Tomas", 23, 'H', 75, 1.73, 'Ingeniería Química', 2014, 40, 31)
e6 = Estudiante("Juan", 28, 'H', 74, 1.80, "Ing. en Sistemas de Información", 2010, 38, 27)

estudiantes = [e1, e2, e3, e4, e5, e6]

dic = organizar_estudiantes(estudiantes)
assert(list(dic.keys()) == ["Ing. en Sistemas de Información", "Ingeniería Mecánica", "Ingeniería Química"] and list(dic.values()) == [2, 2, 2])
