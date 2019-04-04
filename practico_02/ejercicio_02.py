# Implementar la clase Circulo que contiene un radio, y sus metodos area y perimetro.

from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return float(pi*(self.radio**2))

    def perimetro(self):
        return float(2*pi*self.radio)

#r = float(input('Ingrese el radio de un circulo: '))
#c = Circulo (r)
#print('El area del circulo es: ', c.area())
#print('El perimetro del circulo es: ', c.perimetro())


c = Circulo(5)
assert(c.area()== 78.53981633974483)
assert(c.perimetro()== 31.41592653589793)

