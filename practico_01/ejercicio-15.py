#Reescriba el programa que pide al usuario una lista de números e imprime en pantalla el máximo y mínimo de los números introducidos al final, cuando el usuario introduce “fin”.
#Escriba ahora el programa de modo que almacene los números que el usuario introduzca en una lista y usa las funciones max () y min () para calcular los números maximo y mínimo después de que el bucle termine.

def max(lista):
    mayor = -999999999
    for i in range(0, len(lista)):
        if (lista[i] > mayor):
            mayor = lista[i]
    return mayor


def min(lista):
    menor = 999999999
    for i in range(0, len(lista)):
        if (lista[i] < menor):
            menor = lista[i]
    return menor


def main():
    n = input("Ingrese un número (fin para terminar): ")
    lista = []
    while (n != "fin"):
        n = float(n)
        lista.append(n)
        n = input()         #cuando ingrese 'fin' sale del while
    maximo = max(lista)
    minimo = min(lista)

    print("\nEl máximo es: ", maximo, "\n")
    print("El mínimo es: ", minimo, "\n")


main()







