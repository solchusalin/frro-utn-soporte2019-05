# Escribir una función multip() que multiplique respectivamente todos los números de una lista. Por ejemplo: multip([1,2,3,4]) debería devolver 24.

lista = [1, 2, 5, 6.3, -2]

def multip(nros):
    total = 1
    for i in nros:
        total *= i
    return total


assert(multip(lista) == -126)
