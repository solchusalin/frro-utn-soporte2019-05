import random
import datetime

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


    def avance(self):
        porcentaje = float("%.2f" % ((self.cantidad_aprobadas * 100) / self.cantidad_materias))
        return porcentaje


    def edad_ingreso(self):
        edad_ingreso = self.edad - (datetime.datetime.now().year - self.anio)
        return edad_ingreso


estudiante = Estudiante("Agustin", 27, 'M',80, 1.82, "Ingenieria Mecanica",2012, 38, 30)
assert(estudiante.avance() == 78.95 and estudiante.edad_ingreso() == 20)
