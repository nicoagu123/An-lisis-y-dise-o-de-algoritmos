
"""
Ejercicio 2.1 — Búsqueda Lineal O(n)
Implementación de búsqueda lineal con análisis de casos y complejidad
"""

import math


def busqueda_lineal(lista, objetivo, contar_comparaciones=False):
    """
    Realiza búsqueda lineal (secuencial) en una lista.
    
    Parámetros:
        lista (list): Lista de enteros (puede estar desordenada)
        objetivo (int): Valor a buscar
        contar_comparaciones (bool): Si True, retorna (índice, num_comparaciones)
    
    Retorna:
        int o tuple: Índice si encuentra (0-based), -1 si no encuentra
                     Si contar_comparaciones=True, retorna (índice, comparaciones)
    
    Complejidad de Tiempo:
    • Mejor Caso:    O(1)  - Se encuentra en la primera posición
    • Caso Promedio: O(n)  - Se encuentra aproximadamente a mitad
    • Peor Caso:     O(n)  - Elemento no existe o está al final
    
    Complejidad de Espacio: O(1)
    - Solo se usa la variable 'comparaciones' y 'i', sin estructuras adicionales
    """
    comparaciones = 0
    
    for i in range(len(lista)):
        # Cada iteración es 1 comparación
        comparaciones += 1
        
        if lista[i] == objetivo:
            if contar_comparaciones:
                return (i, comparaciones)
            return i
    
    # Si llegamos aquí, no se encontró el elemento
    if contar_comparaciones:
        return (-1, comparaciones)
    return -1


# ============================================================================
# PRUEBAS DE CASOS
# ============================================================================

def prueba_mejor_caso(tamanio):
    """
    MEJOR CASO: Elemento en la primera posición
    
    Análisis:
    - Se encuentra inmediatamente en la primera iteración
    - Número de comparaciones: 1
    - Complejidad: O(1) - Tiempo constante
    
    Nota: Aunque O(1) es el mejor caso, la búsqueda lineal es O(n)
    en el análisis de complejidad promedio y peor caso.
    """
    lista = list(range(tamanio))
    objetivo = 0  # Primer elemento
    
    indice, comparaciones = busqueda_lineal(lista, objetivo, contar_comparaciones=True)
    
    return {
        'caso': 'MEJOR',
        'descripcion': 'Elemento en primera posición',
        'tamanio': tamanio,
        'objetivo': objetivo,
        'indice_encontrado': indice,
        'comparaciones': comparaciones,
        'complejidad': 'O(1)'
    }


def prueba_caso_promedio(tamanio):
    """
    CASO PROMEDIO: Elemento aproximadamente a la mitad
    
    Análisis:
    - Se encuentra después de recorrer aproximadamente n/2 elementos
    - Número de comparaciones: ~n/2
    - Complejidad: O(n) - Tiempo lineal
    
    Nota: El factor constante 1/2 se ignora en notación O,
    quedando O(n).
    """
    lista = list(range(tamanio))
    objetivo = tamanio // 2  # Elemento aproximadamente en la mitad
    
    indice, comparaciones = busqueda_lineal(lista, objetivo, contar_comparaciones=True)
    
    return {
        'caso': 'PROMEDIO',
        'descripcion': 'Elemento a mitad de la lista',
        'tamanio': tamanio,
        'objetivo': objetivo,
        'indice_encontrado': indice,
        'comparaciones': comparaciones,
        'complejidad': 'O(n)'
    }


def prueba_peor_caso(tamanio):
    """
    PEOR CASO: Elemento no existe (o está al final)
    
    Análisis:
    - Se recorre la lista COMPLETA sin encontrarlo
    - Número de comparaciones: n
    - Complejidad: O(n) - Tiempo lineal
    
    Este es el peor caso porque:
    1. Se hacen el máximo de comparaciones posibles
    2. No hay forma de optimizarlo sin información adicional
    """
    lista = list(range(tamanio))
    objetivo = -1  # Valor que NO existe en la lista
    
    indice, comparaciones = busqueda_lineal(lista, objetivo, contar_comparaciones=True)
    
    return {
        'caso': 'PEOR',
        'descripcion': 'Elemento NO existe (o está al final)',
        'tamanio': tamanio,
        'objetivo': objetivo,
        'indice_encontrado': indice,
        'comparaciones': comparaciones,
        'complejidad': 'O(n)'
    }


def prueba_peor_caso_al_final(tamanio):
    """
    PEOR CASO ALTERNATIVO: Elemento está en la última posición
    
    Análisis:
    - Se recorre toda la lista hasta encontrarlo al final
    - Número de comparaciones: n
    - Complejidad: O(n) - Tiempo lineal
    """
    lista = list(range(tamanio))
    objetivo = tamanio - 1  # Último elemento
    
    indice, comparaciones = busqueda_lineal(lista, objetivo, contar_comparaciones=True)
    
    return {
        'caso': 'PEOR (alternativo)',
        'descripcion': 'Elemento en última posición',
        'tamanio': tamanio,
        'objetivo': objetivo,
        'indice_encontrado': indice,
        'comparaciones': comparaciones,
        'complejidad': 'O(n)'
    }


# ============================================================================
# EJECUCIÓN PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("=" * 90)
    print("EJERCICIO 2.1 — BÚSQUEDA LINEAL O(n)")
    print("=" * 90)
    
    tamanios_prueba = [100, 1000, 10000]
    
    # ========================================================================
    # PARTE 1: EJEMPLO CON LISTA PEQUEÑA
    # ========================================================================
    print("\n" + "=" * 90)
    print("PARTE 1: Ejemplo Ilustrativo (lista pequeña)")
    print("=" * 90)
    
    lista_pequena = [10, 5, 8, 15, 3, 20, 1, 12]
    
    print(f"\nLista: {lista_pequena}")
    print("\n▼ Búsqueda del valor 1:")
    indice, comps = busqueda_lineal(lista_pequena, 1, contar_comparaciones=True)
    print(f"  → Encontrado en índice {indice}")
    print(f"  → Comparaciones: {comps}")
    print(f"  → Recorrido: {lista_pequena[:indice+1]}")
    
    print("\n▼ Búsqueda del valor 15:")
    indice, comps = busqueda_lineal(lista_pequena, 15, contar_comparaciones=True)
    print(f"  → Encontrado en índice {indice}")
    print(f"  → Comparaciones: {comps}")
    print(f"  → Recorrido: {lista_pequena[:indice+1]}")
    
    print("\n▼ Búsqueda del valor 100 (no existe):")
    indice, comps = busqueda_lineal(lista_pequena, 100, contar_comparaciones=True)
    print(f"  → No encontrado (retorna -1)")
    print(f"  → Comparaciones: {comps}")
    print(f"  → Se recorrió: toda la lista")
    
    # ========================================================================
    # PARTE 2: MEJOR CASO
    # ========================================================================
    print("\n" + "=" * 90)
    print("PARTE 2: MEJOR CASO — Elemento en la primera posición")
    print("=" * 90)
    
    print(f"\n{'Tamaño (n)':>12} | {'Objetivo':>10} | {'Comparaciones':>15} | {'Ratio C/n':>12} | {'Complejidad':>12}")
    print("-" * 90)
    
    for tamanio in tamanios_prueba:
        resultado = prueba_mejor_caso(tamanio)
        ratio = resultado['comparaciones'] / resultado['tamanio']
        print(f"{resultado['tamanio']:>12} | {resultado['objetivo']:>10} | "
              f"{resultado['comparaciones']:>15} | {ratio:>12.4f} | {resultado['complejidad']:>12}")
    
    print("\n💡 Análisis:")
    print("  • Las comparaciones siempre son 1, sin importar n")
    print("  • Complejidad: O(1) - Tiempo constante (mejor caso)")
    print("  • Solo ocurre si el elemento buscado está en la 1ª posición")
    
    # ========================================================================
    # PARTE 3: CASO PROMEDIO
    # ========================================================================
    print("\n" + "=" * 90)
    print("PARTE 3: CASO PROMEDIO — Elemento aproximadamente en la mitad")
    print("=" * 90)
    
    print(f"\n{'Tamaño (n)':>12} | {'Objetivo':>10} | {'Comparaciones':>15} | {'Ratio C/n':>12} | {'Complejidad':>12}")
    print("-" * 90)
    
    for tamanio in tamanios_prueba:
        resultado = prueba_caso_promedio(tamanio)
        ratio = resultado['comparaciones'] / resultado['tamanio']
        print(f"{resultado['tamanio']:>12} | {resultado['objetivo']:>10} | "
              f"{resultado['comparaciones']:>15} | {ratio:>12.4f} | {resultado['complejidad']:>12}")
    
    print("\n💡 Análisis:")
    print("  • Las comparaciones son aproximadamente n/2")
    print("  • Ratio C/n ≈ 0.5 (constante)")
    print("  • Complejidad: O(n) - Tiempo lineal")
    print("  • El factor 1/2 se ignora en notación O (se omite constantes)")
    
    # ========================================================================
    # PARTE 4: PEOR CASO (No existe)
    # ========================================================================
    print("\n" + "=" * 90)
    print("PARTE 4: PEOR CASO — Elemento NO existe")
    print("=" * 90)
    
    print(f"\n{'Tamaño (n)':>12} | {'Objetivo':>10} | {'Comparaciones':>15} | {'Ratio C/n':>12} | {'Complejidad':>12}")
    print("-" * 90)
    
    for tamanio in tamanios_prueba:
        resultado = prueba_peor_caso(tamanio)
        ratio = resultado['comparaciones'] / resultado['tamanio']
        print(f"{resultado['tamanio']:>12} | {resultado['objetivo']:>10} | "
              f"{resultado['comparaciones']:>15} | {ratio:>12.4f} | {resultado['complejidad']:>12}")
    
    print("\n💡 Análisis:")
    print("  • Se recorre la LISTA COMPLETA sin encontrarlo")
    print("  • Comparaciones = n (máximo posible)")
    print("  • Ratio C/n = 1.0 (se hacen todas las comparaciones)")
    print("  • Complejidad: O(n) - Tiempo lineal")
    
    # ========================================================================
    # PARTE 5: PEOR CASO (Elemento al final)
    # ========================================================================
    print("\n" + "=" * 90)
    print("PARTE 5: PEOR CASO ALTERNATIVO — Elemento en última posición")
    print("=" * 90)
    
    print(f"\n{'Tamaño (n)':>12} | {'Objetivo':>10} | {'Comparaciones':>15} | {'Ratio C/n':>12} | {'Complejidad':>12}")
    print("-" * 90)
    
    for tamanio in tamanios_prueba:
        resultado = prueba_peor_caso_al_final(tamanio)
        ratio = resultado['comparaciones'] / resultado['tamanio']
        print(f"{resultado['tamanio']:>12} | {resultado['objetivo']:>10} | "
              f"{resultado['comparaciones']:>15} | {ratio:>12.4f} | {resultado['complejidad']:>12}")
    
    print("\n💡 Análisis:")
    print("  • Se encuentra solo al recorrer TODA la lista")
    print("  • Comparaciones = n")
    print("  • Complejidad: O(n) - Tiempo lineal (mismo que peor caso)")
    
    # ========================================================================
    # PARTE 6: COMPARATIVA VISUAL
    # ========================================================================
    print("\n" + "=" * 90)
    print("PARTE 6: COMPARATIVA DE CASOS")
    print("=" * 90)
    
    print("\nPara una lista de tamaño n = 10,000:\n")
    
    casos = []
    for tamanio in [10000]:
        mejor = prueba_mejor_caso(tamanio)
        promedio = prueba_caso_promedio(tamanio)
        peor_no_existe = prueba_peor_caso(tamanio)
        peor_final = prueba_peor_caso_al_final(tamanio)
        
        casos = [
            (mejor['caso'], mejor['comparaciones'], mejor['complejidad']),
            (promedio['caso'], promedio['comparaciones'], promedio['complejidad']),
            (peor_no_existe['caso'], peor_no_existe['comparaciones'], peor_no_existe['complejidad']),
            (peor_final['caso'], peor_final['comparaciones'], peor_final['complejidad'])
        ]
    
    print(f"{'Caso':>20} | {'Comparaciones':>15} | {'Complejidad':>12} | Gráfico")
    print("-" * 90)
    
    for caso, comparaciones, complejidad in casos:
        # Crear barra visual
        barra = "█" * (comparaciones // 500)  # Escala para visualizar
        print(f"{caso:>20} | {comparaciones:>15} | {complejidad:>12} | {barra}")
    
    # ========================================================================
    # RESUMEN TEÓRICO
    # ========================================================================
    print("\n" + "=" * 90)
    print("RESUMEN: ANÁLISIS DE COMPLEJIDAD DE BÚSQUEDA LINEAL")
    print("=" * 90)
    
    resumen = """
    ┌──────────────────────────────────────────────────────────────────┐
    │ BÚSQUEDA LINEAL — ANÁLISIS DE COMPLEJIDAD                       │
    ├──────────────────────────────────────────────────────────────────┤
    │                                                                   │
    │ MEJOR CASO: O(1)                                                 │
    │ ───────────────────────────────────────────────────────────────  │
    │ • Condición: Elemento está en la 1ª posición                    │
    │ • Comparaciones: 1                                               │
    │ • Análisis: Se encuentra de inmediato                            │
    │ • Probabilidad: 1/n (1 entre n posibles)                        │
    │                                                                   │
    │ CASO PROMEDIO: O(n)                                              │
    │ ───────────────────────────────────────────────────────────────  │
    │ • Condición: Elemento en posición aleatoria (aprox. mitad)      │
    │ • Comparaciones: ~n/2                                            │
    │ • Análisis: Se recorre aproximadamente la mitad                  │
    │ • Factor constante 1/2 se ignora → O(n)                         │
    │ • Probabilidad: Alta (la mayoría de casos)                      │
    │                                                                   │
    │ PEOR CASO: O(n)                                                  │
    │ ───────────────────────────────────────────────────────────────  │
    │ • Condición: Elemento no existe O está al final                 │
    │ • Comparaciones: n                                               │
    │ • Análisis: Se recorre LA LISTA COMPLETA                        │
    │ • Es el límite superior de tiempo                                │
    │ • Probabilidad: 1/n (1 entre n posibles)                        │
    │                                                                   │
    │ COMPLEJIDAD ESPACIAL: O(1)                                       │
    │ ───────────────────────────────────────────────────────────────  │
    │ • No se usan estructuras auxiliares                              │
    │ • Solo variables de control (i, comparaciones)                  │
    │                                                                   │
    │ VENTAJAS:                                                        │
    │ ✓ Funciona en listas desordenadas                               │
    │ ✓ Simple de implementar                                          │
    │ ✓ Mejor caso O(1) si el elemento está al inicio                │
    │                                                                   │
    │ DESVENTAJAS:                                                     │
    │ ✗ Lenta para listas grandes (O(n))                              │
    │ ✗ En listas ordenadas, búsqueda binaria es mejor O(log n)      │
    │ ✗ No optimizable sin información adicional                      │
    │                                                                   │
    │ COMPARACIÓN CON BÚSQUEDA BINARIA:                               │
    │ ──────────────────────────────────────────────────────────────  │
    │ n = 100       → Lineal: 100 comps  vs  Binaria: 7 comps        │
    │ n = 1,000     → Lineal: 1,000 comps vs Binaria: 10 comps       │
    │ n = 10,000    → Lineal: 10,000 cmp vs Binaria: 14 comps        │
    │ n = 1,000,000 → Lineal: 1M comps   vs Binaria: 20 comps        │
    │                                                                   │
    └──────────────────────────────────────────────────────────────────┘
    """
    print(resumen)
    
    # ========================================================================
    # CONCLUSIÓN
    # ========================================================================
    print("\n" + "=" * 90)
    print("CONCLUSIÓN")
    print("=" * 90)
    
    print("""
    La búsqueda lineal es O(n) porque:
    
    1. En el peor caso, siempre recorre toda la lista (n elementos)
    2. No hay forma de optimizarla sin ordenar los datos primero
    3. El análisis de complejidad considera el peor caso
    4. Por eso decimos que es "tiempo lineal O(n)"
    
    El mejor caso O(1) es excepcional y no representa el comportamiento típico.
    Por eso en análisis de algoritmos enfatizamos la complejidad promedio/peor.
    """)

