

"""
Ejercicio 3.1 — Comparar búsqueda lineal vs binaria
Mide tiempos promediados usando time.perf_counter()
"""

import time


def busqueda_lineal(lista, objetivo):
    for i, v in enumerate(lista):
        if v == objetivo:
            return i
    return -1


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


def medir(func, lista, objetivo, repeticiones):
    start = time.perf_counter()
    for _ in range(repeticiones):
        func(lista, objetivo)
    end = time.perf_counter()
    total = end - start
    promedio = total / repeticiones
    return promedio * 1000.0  # ms por ejecución


def main():
    tamanios = [1_000, 10_000, 100_000]
    escenarios = [
        ("al_final", lambda n: n - 1),
        ("no_existe", lambda n: n)
    ]

    print("Comparativa búsqueda lineal vs binaria (tiempo promedio por búsqueda en ms)")
    print("-" * 80)

    for escenario_nombre, objetivo_fn in escenarios:
        print(f"Escenario: {escenario_nombre}")
        print(f"{'n':>10} | {'Lineal (ms)':>15} | {'Binaria (ms)':>15} | {'Repeticiones':>12}")
        print('-' * 80)

        for n in tamanios:
            lista = list(range(n))
            objetivo = objetivo_fn(n)

            # ajustar repeticiones para que el tiempo total sea razonable
            repeticiones = max(10, int(1_000_000 / n))

            t_lineal = medir(busqueda_lineal, lista, objetivo, repeticiones)
            t_binaria = medir(busqueda_binaria, lista, objetivo, repeticiones)

            print(f"{n:10} | {t_lineal:15.6f} | {t_binaria:15.6f} | {repeticiones:12}")

        print('\n')

    # Conclusión breve
    print("Conclusión: Búsqueda binaria es mucho más eficiente para listas ordenadas")
    print("porque su complejidad es O(log n) frente a O(n) de la lineal.")


if __name__ == '__main__':
    main()
