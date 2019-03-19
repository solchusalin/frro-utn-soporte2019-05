# Programe una función que determine si un número entero suministrado como argumento es primo.


def es_primo(n):
    if n < 2:
        return False
    elif n == 2:
        return True         #el 2 es el primer numero primo
    else:
        for i in range(2, n-1):
            if n % i == 0:      #busco un nro distinto de 1 y n, cuyo resto de la division me de 0.
                return False
        return True

assert(es_primo(4) == False)
assert(es_primo(13) == True)
