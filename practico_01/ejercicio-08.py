# Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

x1 = ['Arbol', 'Casa', 'Mesa', 'Auto', 'Perro']
x2 = ['Gato', 'Loro', 'Perro', 'Ave']

def superposicion(lista1, lista2):
    for i in range(0, len(lista1)):         # for i in lista1 NO FUNCIONA
        for j in range (0, len(lista2)):
            if (lista1[i] == lista2[j]):
                return True
    return False


assert(superposicion(x1, x2) == True)

