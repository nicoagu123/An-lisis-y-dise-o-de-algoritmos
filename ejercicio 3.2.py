

"""
Mide memoria usada al construir una lista de los primeros n cuadrados
vs crear y consumir un generador que produce los mismos valores.

Uso:
    python medir_cuadrados_memoria.py 100000 1000000

Si no se pasan argumentos, usa n=100000 por defecto.
"""
import sys
import tracemalloc
import gc


def bytes_to_mb(b):
    return b / (1024 * 1024)


def medir_lista(n):
    gc.collect()
    tracemalloc.start()
    # Construir la lista
    lista = [i * i for i in range(1, n + 1)]
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    # liberar memoria
    del lista
    gc.collect()
    return current, peak


def medir_generador_consumido(n):
    gc.collect()
    tracemalloc.start()
    gen = (i * i for i in range(1, n + 1))
    # Consumir todo el generador construyendo una lista (como pide el enunciado)
    lista_from_gen = list(gen)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    # liberar memoria
    del lista_from_gen
    gc.collect()
    return current, peak


def medir_generador_iterado(n):
    """
    Variante: medir el caso de iterar sin almacenar (memoria constante esperada).
    No se usa para la tabla principal, pero es útil como referencia.
    """
    gc.collect()
    tracemalloc.start()
    gen = (i * i for i in range(1, n + 1))
    # Iterar pero no guardar
    s = 0
    for v in gen:
        s += v  # operación trivial para forzar la evaluación
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    gc.collect()
    return current, peak


def medir_para_n(n):
    print(f"\n--- Medición para n = {n:,} ---")

    cur_l, peak_l = medir_lista(n)
    print(f"Lista: current = {bytes_to_mb(cur_l):.2f} MB, peak = {bytes_to_mb(peak_l):.2f} MB")

    cur_g, peak_g = medir_generador_consumido(n)
    print(f"Generador (consumido con list()): current = {bytes_to_mb(cur_g):.2f} MB, peak = {bytes_to_mb(peak_g):.2f} MB")

    cur_gi, peak_gi = medir_generador_iterado(n)
    print(f"Generador (iterado sin almacenar): current = {bytes_to_mb(cur_gi):.2f} MB, peak = {bytes_to_mb(peak_gi):.2f} MB")

    print("\nConclusión primaria:")
    print("  - Construir la lista asigna memoria proporcional a n → O(n) en espacio.")
    print("  - Crear el generador es O(1), pero consumirlo con list(gen) también requiere O(n) memoria (porque se crea una lista).")
    print("  - Iterar el generador sin almacenar mantiene el uso de memoria aproximadamente constante → O(1).")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            ns = [int(x) for x in sys.argv[1:]]
        except ValueError:
            print("Argumentos inválidos. Proporcione enteros para n.")
            sys.exit(1)
    else:
        ns = [100000]

    print("Mediciones de memoria (tracemalloc). Ten en cuenta que los valores son memoria Python asignada.")
    for n in ns:
        medir_para_n(n)
    print('\nHecho.')
