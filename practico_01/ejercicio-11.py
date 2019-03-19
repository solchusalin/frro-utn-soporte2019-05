# Determinar la cantidad de dígitos de un número ingresado.


n = input("Ingrese un numero: ")

def cant_digitos(nro):
    nro = str(nro)
    total  = 0
    for i in range(0, len(nro)):
        if (nro[i] != '.'):         #no cuenta la coma de un numero decimal
            total += 1
    return total


assert(cant_digitos(n) == 5)

