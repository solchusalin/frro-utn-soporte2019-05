# Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".

def inversa(cad1):
    cad2 = ""
    for i in range(1, len(cad1)+1):   #arranco en 1 porque no existe el -0
        cad2 += cad1[-i]
    return cad2


assert(inversa('Hola como estas') == 'satse omoc aloH')
assert(inversa('123456789') == '987654321')
