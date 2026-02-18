def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio  # Objetivo encontrado
        elif lista[medio] < objetivo:
            bajo = medio + 1  # Buscar en la mitad derecha
        else:
            alto = medio - 1  # Buscar en la mitad izquierda
    return -1  # Objetivo no encontrado

# Ejemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13]
objetivo=int(input("Ingrese el número a buscar: "))
resultado = busqueda_binaria(lista_ordenada, objetivo)
print(f"posición: {resultado}") # Salida: 3

