

"""
Ejercicio 3.2 — Gráficas para búsqueda binaria
Genera dos gráficas:
 1) Tiempo promedio por búsqueda (ms) vs tamaño n
 2) Número de comparaciones (peor caso) vs n (y comparación con log2(n))

Guarda: 'bin_search_time.png' y 'bin_search_comparisons.png' en el Escritorio.

Uso:
    python ejercicio_3_2.py

Opcional: pasar tamaños personalizados en línea de comandos.
"""

import time
import math
import sys
import matplotlib.pyplot as plt
import gc


def busqueda_binaria(lista, objetivo):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        mid = (izq + der) // 2
        if lista[mid] == objetivo:
            return mid
        elif lista[mid] < objetivo:
            izq = mid + 1
        else:
            der = mid - 1
    return -1


def busqueda_binaria_contar(lista, objetivo):
    """Devuelve (indice, comparaciones). Cuenta comparaciones en peor caso."""
    izq = 0
    der = len(lista) - 1
    comparaciones = 0
    while izq <= der:
        mid = (izq + der) // 2
        comparaciones += 1  # comparación lista[mid] == objetivo
        if lista[mid] == objetivo:
            return mid, comparaciones
        comparaciones += 1  # comparación lista[mid] < objetivo
        if lista[mid] < objetivo:
            izq = mid + 1
        else:
            der = mid - 1
    return -1, comparaciones


def medir_tiempo(func, lista, objetivo, repeticiones):
    gc.collect()
    start = time.perf_counter()
    for _ in range(repeticiones):
        func(lista, objetivo)
    end = time.perf_counter()
    total = end - start
    return (total / repeticiones) * 1000.0  # ms


def main(ns=None):
    # Valores por defecto para n
    if ns is None:
        ns = [1000, 2000, 5000, 10000, 20000, 50000, 100000]

    lista_ns = ns

    tiempos = []
    comparaciones = []
    teorico = []

    for n in lista_ns:
        lista = list(range(n))
        objetivo = -1  # No existe -> suele producir peor caso

        # ajustar repeticiones para mantener tiempos razonables
        repeticiones = max(50, int(200000 / n))

        t_prom = medir_tiempo(busqueda_binaria, lista, objetivo, repeticiones)
        tiempos.append(t_prom)

        _, comps = busqueda_binaria_contar(lista, objetivo)
        comparaciones.append(comps)

        teorico.append(math.log2(n) + 1)

        print(f"n={n:7} | rep={repeticiones:4} | tiempo_bin(ms)={t_prom:8.4f} | comps={comps}")

    # GRAFICA 1: Tiempo vs n
    plt.figure(figsize=(8,5))
    plt.plot(lista_ns, tiempos, marker='o', label='Tiempo promedio (ms)')
    plt.title('Búsqueda binaria — Tiempo promedio por búsqueda')
    plt.xlabel('Tamaño de la lista n')
    plt.ylabel('Tiempo (ms)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig('bin_search_time.png')

    # GRAFICA 2: Comparaciones vs n (peor caso)
    plt.figure(figsize=(8,5))
    plt.plot(lista_ns, comparaciones, marker='o', label='Comparaciones (medidas)')
    plt.plot(lista_ns, teorico, marker='x', linestyle='--', label='log2(n) + 1 (teórico)')
    plt.title('Búsqueda binaria — Comparaciones (peor caso)')
    plt.xlabel('Tamaño de la lista n')
    plt.ylabel('Comparaciones')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig('bin_search_comparisons.png')

    print('\nGráficas guardadas: bin_search_time.png, bin_search_comparisons.png')
    try:
        plt.show()
    except Exception:
        pass


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            ns = [int(x) for x in sys.argv[1:]]
        except ValueError:
            print('Argumentos inválidos; se usarán los valores por defecto.')
            ns = None
    else:
        ns = None
    main(ns)
