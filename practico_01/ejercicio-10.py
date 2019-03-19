# Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga.

def mas_larga(lista):
    mayor = 0
    for i in range(0, len(lista)):
        if len(lista[i]) > mayor:
            mayor = len(lista[i])
            palabra = lista[i]
    return palabra

palabras = ['Azul', 'Verde', 'Blanco', 'Amarillo']

assert(mas_larga(palabras) == 'Amarillo')
