#implementar la clase Rectangulo que contiene una base y una altura, y el metodo area.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


#a = float(input('Ingrese la altura de un rectangulo: '))
#b = float(input('ingrese la base de un rectangulo: '))
#r = Rectangulo(b, a)
#print('El area del rectangulo es: ',r.area())

r = Rectangulo (3,5)
assert (r.area()==15)
