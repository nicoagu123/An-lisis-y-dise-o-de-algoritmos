
"""
Ejercicio 2.1 — Búsqueda Lineal O(n)
Implementación de búsqueda lineal con análisis de casos y complejidad
"""


def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def main():
    # leer tamaño
    n = int(input("Ingrese el tamaño de la lista (n): "))
    # leer la lista (se asume que se ingresan n números, separados por espacios)
    while True:
        linea = input("Ingrese los n elementos de la lista, separados por espacio: ")
        partes = linea.strip().split()
        if len(partes) == n:
            lista = [int(x) for x in partes]
            break
        else:
            print(f"Debe ingresar exactamente {n} números. Intentá nuevamente.")

    # leer valor a buscar
    objetivo = int(input("Ingrese el valor a buscar: "))

    # buscar
    indice = busqueda_lineal(lista, objetivo)

    # mostrar resultado
    if indice != -1:
        print(f"Encontrado en la posición: {indice}")
        if indice == 0:
            print("Mejor caso: está en la primera posición.")
        elif indice == n - 1:
            print("Caso cerca al peor: está en la última posición.")
        else:
            print("Caso promedio: está en una posición intermedia.")
    else:
        print("No encontrado en la lista. Es el peor caso.")

if __name__ == "__main__":
    main()
