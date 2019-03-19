#Programe un algoritmo recursivo que encuentre la salida de un laberinto.

lab = [[True, False, True, True],
       [False, False, True, False],
       [False, True, True, False],
       [False, True, True, True]]

def salida_laberinto(f, c):
    if (f == 3 and c == 0):                                #encuentra la salida en el punto 3,0.
        print('Salida encontrada en posición',f,',',c)
        return True

    elif (lab[f][c] == False):
        print('Avanza a la posición ',f,',',c)             #avanza una posicion pero no llego a la salida. Debe seguir avanzando.
        lab[f][c] = 2


    elif (lab[f][c] == True):                              #se encuentra con un obstaculo. Debe cambiar de direccion para poder avanzar.
        print('Obstaculo en posición ',f,',',c)
        return False

    elif (lab[f][c] == 2):                                 #ya paso por esa posicion. Debe cambiar de direccion para poder avanzar.
        print('Ya pasó por la posición ',f,',',c)
        return False


    salida = (salida_laberinto(f+1, c) or salida_laberinto(f, c+1) or salida_laberinto(f-1, c) or salida_laberinto(f, c-1))
    if salida:
        return True                                                 #se mueve en direccion norte, sur, este, oeste.

    return False

#main
a = 0
b = 1                                                               #entrada al laberinto. posicion inicial en 0,1.
salida_laberinto(a, b)
