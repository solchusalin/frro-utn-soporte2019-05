#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.

def max(n1, n2):
    if (n1 > n2):
        return n1
    else:
        return n2


assert(max(2,5) == 5)
assert(max(34,8) == 34)
assert (max(4,4) == 4)
