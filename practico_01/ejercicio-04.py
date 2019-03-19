# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

v = ['a', 'e', 'i', 'o', 'u']
c = input("Ingrese un caracter: ")

def esVocal(car, vocales):
    if car in vocales:
        return True
    else:
        return False

assert(esVocal(c, v) == True)



