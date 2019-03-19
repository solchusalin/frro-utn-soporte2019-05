# Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.


def es_palindromo(cad1):
    cad2 = ""
    for i in range(1, len(cad1)+1):
        cad2 += cad1[-i]
    if (cad1 == cad2):
        return True
    else:
        return False


assert(es_palindromo('neuquen') == True)
assert(es_palindromo('hola') == False)


