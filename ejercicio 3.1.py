

"""
Ejercicio 3.1 — Comparar búsqueda lineal vs binaria
Mide tiempos promediados usando time.perf_counter()
"""

import time

# Tamaños de lista que vamos a probar
tamaños = [1000, 10000, 100000]

# Número de repeticiones para cada tamaño (para que el tiempo total sea manejable)
repeticiones = {
    1000: 10000,   # 10.000 repeticiones para listas pequeñas
    10000: 1000,   # 1.000 repeticiones para listas medianas
    100000: 100    # 100 repeticiones para listas grandes
}

def busqueda_lineal(lista, objetivo):
    """Busca objetivo en lista ordenada recorriendo elemento por elemento."""
    for elemento in lista:
        if elemento == objetivo:
            return True
        # Como la lista está ordenada, si encontramos un elemento mayor que el objetivo,
        # podemos detenernos porque el objetivo no estará más adelante.
        if elemento > objetivo:
            return False
    return False  # No se encontró

def busqueda_binaria(lista, objetivo):
    """Busca objetivo en lista ordenada dividiendo el espacio de búsqueda a la mitad."""
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return False

# Guardaremos los resultados aquí
resultados = []

for n in tamaños:
    # Creamos una lista ordenada de 0 a n-1
    lista = list(range(n))
    # Elegimos un objetivo que NO está en la lista (n es mayor que todos)
    objetivo = n

    print(f"Probando con lista de {n} elementos...")

    # --- Medición de búsqueda lineal ---
    inicio = time.perf_counter()               # Tiempo inicial
    for _ in range(repeticiones[n]):           # Repetimos muchas veces
        busqueda_lineal(lista, objetivo)
    fin = time.perf_counter()                   # Tiempo final
    tiempo_lineal = (fin - inicio) / repeticiones[n]   # Tiempo promedio por búsqueda

    # --- Medición de búsqueda binaria ---
    inicio = time.perf_counter()
    for _ in range(repeticiones[n]):
        busqueda_binaria(lista, objetivo)
    fin = time.perf_counter()
    tiempo_binaria = (fin - inicio) / repeticiones[n]

    # Guardamos
    resultados.append((n, tiempo_lineal, tiempo_binaria))

# Mostramos la tabla comparativa
print("\n" + "="*60)
print("Tamaño   Tiempo Lineal (seg)   Tiempo Binario (seg)   Mejora (veces)")
print("="*60)
for n, tlin, tbin in resultados:
    mejora = tlin / tbin
    print(f"{n:<8} {tlin:.3e}           {tbin:.3e}           {mejora:.2f}")
print("="*60)
