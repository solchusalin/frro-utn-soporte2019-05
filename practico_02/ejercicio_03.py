
import random
class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = self.generar_dni()

    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    # llamarlo desde __init__
    def generar_dni(self):
        return random.randrange(100000000)

    def print_data(self):
        print('Nombre:', self.nombre,"\n",'Edad:', self.edad,"\n",'Sexo:', self.sexo,"\n",'Peso:', self.peso,"\n",'Altura:',self.altura,"\n",'DNI:', self.dni)


per = Persona ('Sol',22,'F','60','1.70')
per.print_data()
assert(per.es_mayor_edad() == True)
