
"""
Ejercicio 1.2 — Búsqueda Binaria O(log n)
Implementación de búsqueda binaria con análisis de complejidad
"""

import math


def busqueda_binaria(lista, objetivo, contar_comparaciones=False):
    """
    Realiza búsqueda binaria en una lista ordenada.
    
    Parámetros:
        lista (list): Lista ordenada de integers
        objetivo (int): Valor a buscar
        contar_comparaciones (bool): Si True, retorna (índice, num_comparaciones)
    
    Retorna:
        int o tuple: Índice si encuentra (0-based), -1 si no encuentra
                     Si contar_comparaciones=True, retorna (índice, comparaciones)
    
    Complejidad de Tiempo: O(log n)
    - En cada iteración, dividimos el espacio de búsqueda a la mitad
    - Máximo de iteraciones = log₂(n)
    - En una lista de 1,000 elementos: máximo ~10 iteraciones
    - En una lista de 1,000,000 elementos: máximo ~20 iteraciones
    
    Complejidad de Espacio: O(1)
    - Solo usamos variables de control (izq, der, mid, contador)
    - No usamos estructuras adicionales que crezcan con n
    """
    izq = 0
    der = len(lista) - 1
    comparaciones = 0
    
    while izq <= der:
        # +1 comparación por la condición del while
        comparaciones += 1
        
        mid = (izq + der) // 2
        
        # Comparación central
        if lista[mid] == objetivo:
            if contar_comparaciones:
                return (mid, comparaciones)
            return mid
        
        # +1 otra comparación
        comparaciones += 1
        if lista[mid] < objetivo:
            izq = mid + 1
        else:
            der = mid - 1
    
    if contar_comparaciones:
        return (-1, comparaciones)
    return -1


def busqueda_lineal_para_comparar(lista, objetivo):
    """
    Búsqueda lineal O(n) para comparar con binaria.
    Se usa solo para validar resultados.
    """
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1


# ============================================================================
# PRUEBAS Y ANÁLISIS
# ============================================================================

def prueba_mejor_caso(tamanio):
    """
    Mejor caso: elemento está en el centro (se encuentra de inmediato)
    """
    lista = list(range(tamanio))
    objetivo = tamanio // 2  # Elemento en el centro
    
    indice, comparaciones = busqueda_binaria(lista, objetivo, contar_comparaciones=True)
    
    return {
        'tamanio': tamanio,
        'objetivo': objetivo,
        'encontrado': indice >= 0,
        'comparaciones': comparaciones,
        'log2(n)': math.log2(tamanio)
    }


def prueba_peor_caso(tamanio):
    """
    Peor caso: elemento no existe en la lista.
    Requiere explorar hasta los límites del árbol de búsqueda.
    """
    lista = list(range(tamanio))
    objetivo = -1  # Número que no existe en la lista
    
    indice, comparaciones = busqueda_binaria(lista, objetivo, contar_comparaciones=True)
    
    return {
        'tamanio': tamanio,
        'objetivo': objetivo,
        'encontrado': indice >= 0,
        'comparaciones': comparaciones,
        'log2(n)': math.log2(tamanio)
    }


def prueba_elemento_extremo(tamanio):
    """
    Caso intermedio: búsqueda del último elemento (extremo derecho)
    """
    lista = list(range(tamanio))
    objetivo = tamanio - 1  # Último elemento
    
    indice, comparaciones = busqueda_binaria(lista, objetivo, contar_comparaciones=True)
    
    return {
        'tamanio': tamanio,
        'objetivo': objetivo,
        'encontrado': indice >= 0,
        'comparaciones': comparaciones,
        'log2(n)': math.log2(tamanio)
    }


def prueba_elemento_primer(tamanio):
    """
    Caso intermedio: búsqueda del primer elemento (extremo izquierdo)
    """
    lista = list(range(tamanio))
    objetivo = 0  # Primer elemento
    
    indice, comparaciones = busqueda_binaria(lista, objetivo, contar_comparaciones=True)
    
    return {
        'tamanio': tamanio,
        'objetivo': objetivo,
        'encontrado': indice >= 0,
        'comparaciones': comparaciones,
        'log2(n)': math.log2(tamanio)
    }


if __name__ == "__main__":
    print("=" * 80)
    print("EJERCICIO 1.2 — BÚSQUEDA BINARIA O(log n)")
    print("=" * 80)
    
    tamanios = [100, 1_000, 10_000, 100_000]
    
    # ========================================================================
    # MEJOR CASO: Elemento en el centro
    # ========================================================================
    print("\n" + "=" * 80)
    print("MEJOR CASO: Elemento en el centro")
    print("=" * 80)
    print(f"{'Tamaño n':>10} | {'Objetivo':>10} | {'Comparaciones':>15} | {'log₂(n)':>10} | {'C/log(n)':>10}")
    print("-" * 80)
    
    resultados_mejor = []
    for tamanio in tamanios:
        resultado = prueba_mejor_caso(tamanio)
        resultados_mejor.append(resultado)
        ratio = resultado['comparaciones'] / resultado['log2(n)']
        print(f"{resultado['tamanio']:>10} | {resultado['objetivo']:>10} | "
              f"{resultado['comparaciones']:>15} | {resultado['log2(n)']:>10.2f} | {ratio:>10.2f}")
    
    # ========================================================================
    # PEOR CASO: Elemento no existe
    # ========================================================================
    print("\n" + "=" * 80)
    print("PEOR CASO: Elemento no existe en la lista")
    print("=" * 80)
    print(f"{'Tamaño n':>10} | {'Objetivo':>10} | {'Comparaciones':>15} | {'log₂(n)':>10} | {'C/log(n)':>10}")
    print("-" * 80)
    
    resultados_peor = []
    for tamanio in tamanios:
        resultado = prueba_peor_caso(tamanio)
        resultados_peor.append(resultado)
        ratio = resultado['comparaciones'] / resultado['log2(n)']
        print(f"{resultado['tamanio']:>10} | {resultado['objetivo']:>10} | "
              f"{resultado['comparaciones']:>15} | {resultado['log2(n)']:>10.2f} | {ratio:>10.2f}")
    
    # ========================================================================
    # CASO: Primer elemento
    # ========================================================================
    print("\n" + "=" * 80)
    print("CASO INTERMEDIO: Búsqueda del primer elemento")
    print("=" * 80)
    print(f"{'Tamaño n':>10} | {'Objetivo':>10} | {'Comparaciones':>15} | {'log₂(n)':>10} | {'C/log(n)':>10}")
    print("-" * 80)
    
    for tamanio in tamanios:
        resultado = prueba_elemento_primer(tamanio)
        ratio = resultado['comparaciones'] / resultado['log2(n)']
        print(f"{resultado['tamanio']:>10} | {resultado['objetivo']:>10} | "
              f"{resultado['comparaciones']:>15} | {resultado['log2(n)']:>10.2f} | {ratio:>10.2f}")
    
    # ========================================================================
    # CASO: Último elemento
    # ========================================================================
    print("\n" + "=" * 80)
    print("CASO INTERMEDIO: Búsqueda del último elemento")
    print("=" * 80)
    print(f"{'Tamaño n':>10} | {'Objetivo':>10} | {'Comparaciones':>15} | {'log₂(n)':>10} | {'C/log(n)':>10}")
    print("-" * 80)
    
    for tamanio in tamanios:
        resultado = prueba_elemento_extremo(tamanio)
        ratio = resultado['comparaciones'] / resultado['log2(n)']
        print(f"{resultado['tamanio']:>10} | {resultado['objetivo']:>10} | "
              f"{resultado['comparaciones']:>15} | {resultado['log2(n)']:>10.2f} | {ratio:>10.2f}")
    
    # ========================================================================
    # ANÁLISIS COMPARATIVO
    # ========================================================================
    print("\n" + "=" * 80)
    print("ANÁLISIS COMPARATIVO: Crecimiento Logarítmico")
    print("=" * 80)
    
    print("\n▼ MEJOR CASO (Elemento en el centro):")
    print("  Comparaciones Esperadas: O(1) a O(log n)")
    comparaciones_mejor = [r['comparaciones'] for r in resultados_mejor]
    print(f"  Secuencia: {comparaciones_mejor}")
    
    print("\n▼ PEOR CASO (Elemento no existe):")
    print("  Comparaciones Esperadas: O(log n)")
    comparaciones_peor = [r['comparaciones'] for r in resultados_peor]
    print(f"  Secuencia: {comparaciones_peor}")
    
    # Verificar que sigue patrón logarítmico
    print("\n▼ VERIFICACIÓN DEL CRECIMIENTO LOGARÍTMICO:")
    print("  La razón Comparaciones/log₂(n) debe ser aproximadamente constante")
    
    print("\n  Mejor Caso:")
    for r in resultados_mejor:
        ratio = r['comparaciones'] / r['log2(n)']
        print(f"    n={r['tamanio']:>6} → {ratio:>6.2f}x log₂(n)")
    
    print("\n  Peor Caso:")
    for r in resultados_peor:
        ratio = r['comparaciones'] / r['log2(n)']
        print(f"    n={r['tamanio']:>6} → {ratio:>6.2f}x log₂(n)")
    
    # ========================================================================
    # COMPARACIÓN BÚSQUEDA BINARIA vs LINEAL
    # ========================================================================
    print("\n" + "=" * 80)
    print("COMPARACIÓN: Búsqueda Binaria O(log n) vs Búsqueda Lineal O(n)")
    print("=" * 80)
    
    print(f"\n{'Tamaño':>10} | {'Binaria (C)':>15} | {'Lineal (C)':>15} | {'Mejora':>10}")
    print("-" * 80)
    
    for tamanio in tamanios:
        # Peor caso binaria
        lista = list(range(tamanio))
        _, comparaciones_bin = busqueda_binaria(lista, -1, contar_comparaciones=True)
        
        # Peor caso lineal (no encontrado)
        comparaciones_lin = tamanio
        
        mejora = comparaciones_lin / comparaciones_bin
        print(f"{tamanio:>10} | {comparaciones_bin:>15} | {comparaciones_lin:>15} | "
              f"{mejora:>9.1f}x")
    
    # ========================================================================
    # RESUMEN TEÓRICO
    # ========================================================================
    print("\n" + "=" * 80)
    print("RESUMEN DE COMPLEJIDAD")
    print("=" * 80)
    
    resumen = """
    ┌────────────────────────────────────────────────────────────────┐
    │ CARACTERÍSTICAS DE LA BÚSQUEDA BINARIA                          │
    ├────────────────────────────────────────────────────────────────┤
    │                                                                 │
    │ TIEMPO:                                                        │
    │ • Mejor Caso:    O(1)      - Elemento en la mitad             │
    │ • Caso Promedio: O(log n)  - Típicamente                      │
    │ • Peor Caso:     O(log n)  - Elemento no existe               │
    │                                                                 │
    │ ESPACIO:                                                       │
    │ • O(1)           - Solo variables de control (sin recursión)  │
    │                    (Nota: recursiva sería O(log n) por stack) │
    │                                                                 │
    │ PRERREQUISITO:                                                 │
    │ • La lista DEBE estar ORDENADA                                 │
    │                                                                 │
    │ VENTAJAS:                                                      │
    │ • Mucho más rápida que búsqueda lineal para listas grandes    │
    │ • Con n=1,000,000: binaria ≈ 20 comp vs lineal ≈ 1,000,000  │
    │                                                                 │
    │ DEMOSTRACIÓN:                                                  │
    │ • log₂(100)      ≈ 6.6  comparaciones máximo                 │
    │ • log₂(1,000)    ≈ 10.0 comparaciones máximo                 │
    │ • log₂(10,000)   ≈ 13.3 comparaciones máximo                 │
    │ • log₂(100,000)  ≈ 16.6 comparaciones máximo                 │
    │                                                                 │
    │ El número de comparaciones CRECE LOGARÍTMICAMENTE,            │
    │ mientras que en búsqueda lineal crece LINEALMENTE.            │
    │                                                                 │
    └────────────────────────────────────────────────────────────────┘
    """
    print(resumen)

