# Determinar la suma de todos los números de 1 a N. N es un número que se ingresa por consola.

n = int(input("Ingresar un número: "))

def suma(nro):
    total = 0
    for i in range(1, n+1):     #arranco en 1 porque el 0 no suma
        total += i
    return total

print('La sumatoria de 1 a', n, 'es: ', suma(n))

#assert(suma(n) == 10)

