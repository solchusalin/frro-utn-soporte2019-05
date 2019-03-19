#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx”

def generar_n_caracteres(n, c):
    cad = ""
    for i in range(0, n):
        cad += c
    return cad

assert(generar_n_caracteres(4, '#') == '####')
assert(generar_n_caracteres(7, 'a') == 'aaaaaaa')

