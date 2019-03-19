# Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.


def max_de_tres(a, b, c):
    if (a > b) and (a > c):
        return a
    elif (b > c) and (b > a):
        return b
    else:
        return c


assert(max_de_tres(10,20,30) == 30)
assert(max_de_tres(20,30,10) == 30)
assert(max_de_tres(30,10,20) == 30)
