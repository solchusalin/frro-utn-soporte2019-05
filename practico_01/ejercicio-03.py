#Definir una función que calcule la longitud de una lista o una cadena dada.


lista = ['Azul', 'Amarillo', 'Verde', 'Naranja', 'Rojo']
cad = "Colores"


def longitud(s):
    cant = 0
    for i in s:
        cant += 1
    return cant

#print("Longitud de Lista:", longitud(lista), "\n")
#print("Longitud de Cadena:", longitud(cad))

assert (longitud(lista) == 5)
assert (longitud(cad) == 7)






