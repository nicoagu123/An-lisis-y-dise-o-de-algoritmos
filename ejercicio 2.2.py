

"""
Ejercicio 2.2 — Inserción en Orden (en Lista Ordenada)
Análisis de complejidad: Búsqueda + Desplazamientos
"""


def insertar_en_orden(lista, valor, contar_operaciones=False):
    """
    Inserta un valor en una lista ordenada manteniendo el orden.
    
    Algoritmo:
    1. Buscar la posición correcta (búsqueda lineal)
    2. Desplazar elementos a la derecha si es necesario
    3. Insertar el nuevo valor
    
    Parámetros:
        lista (list): Lista ordenada de enteros
        valor (int): Valor a insertar
        contar_operaciones (bool): Si True, retorna estadísticas
    
    Retorna:
        list o tuple: Lista con el valor insertado
                      Si contar_operaciones=True, retorna (lista, stats_dict)
    
    Complejidad de Tiempo:
    • Mejor Caso (insertar al final):    O(n) - Solo búsqueda, 0 desplazamientos
    • Caso Promedio (insertar en mitad): O(n) - Búsqueda + ~n/2 desplazamientos
    • Peor Caso (insertar al inicio):    O(n) - Búsqueda + n desplazamientos
    
    Complejidad de Espacio: O(1) - No usamos estructuras auxiliares
    (Nota: Python list.insert() crea una copia interna, pero lógicamente es O(1))
    """
    
    comparaciones = 0
    desplazamientos = 0
    
    # PASO 1: Buscar la posición correcta
    posicion = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i] < valor:
            posicion = i + 1
        else:
            break  # Encontramos la posición
    
    # PASO 2: Desplazar elementos a la derecha (contar desplazamientos)
    # Si insertamos al final, no hay desplazamientos
    # Si insertamos al inicio, todos los elementos se desplazan
    desplazamientos = len(lista) - posicion
    
    # PASO 3: Insertar el valor
    lista_copia = lista.copy()  # Hacer copia para no modificar original
    lista_copia.insert(posicion, valor)
    
    if contar_operaciones:
        return lista_copia, {
            'posicion': posicion,
            'comparaciones': comparaciones,
            'desplazamientos': desplazamientos,
            'total_operaciones': comparaciones + desplazamientos
        }
    
    return lista_copia


def insertar_en_orden_binaria(lista, valor, contar_operaciones=False):
    """
    Variante con BÚSQUEDA BINARIA para encontrar la posición.
    (Más eficiente para listas muy grandes)
    
    Complejidad de Tiempo:
    • Búsqueda: O(log n)
    • Desplazamientos: O(n) en peor caso
    • Total: O(n) por los desplazamientos
    
    Nota: La búsqueda binaria mejora el factor de búsqueda pero los
    desplazamientos siguen siendo O(n), así que el total sigue siendo O(n).
    """
    import bisect
    
    comparaciones = int(__import__('math').log2(len(lista)) + 1) if len(lista) > 0 else 0
    desplazamientos = len(lista) - bisect.bisect_left(lista, valor)
    
    lista_copia = lista.copy()
    posicion = bisect.bisect_left(lista_copia, valor)
    lista_copia.insert(posicion, valor)
    
    if contar_operaciones:
        return lista_copia, {
            'posicion': posicion,
            'comparaciones': comparaciones,
            'desplazamientos': desplazamientos,
            'total_operaciones': comparaciones + desplazamientos,
            'metodo': 'Binaria'
        }
    
    return lista_copia


# ============================================================================
# PRUEBAS DE CASOS
# ============================================================================

def prueba_mejor_caso(tamanio):
    """
    MEJOR CASO: Insertar un valor MAYOR que todos los demás (al final)
    
    Análisis:
    • Se recorre la lista completa en búsqueda: n comparaciones
    • No hay desplazamientos: 0 desplazamientos
    • Total: n operaciones
    • Complejidad: O(n) por la búsqueda (no hay desplazamientos)
    """
    lista = list(range(0, tamanio, 1))  # [0, 1, 2, ..., tamanio-1]
    valor = tamanio  # Mayor que todos
    
    lista_resultado, stats = insertar_en_orden(lista, valor, contar_operaciones=True)
    
    return {
        'caso': 'MEJOR',
        'descripcion': 'Insertar al FINAL (valor mayor)',
        'tamanio': tamanio,
        'valor': valor,
        'posicion_insercion': stats['posicion'],
        'comparaciones': stats['comparaciones'],
        'desplazamientos': stats['desplazamientos'],
        'total_operaciones': stats['total_operaciones'],
        'complejidad': 'O(n)'
    }


def prueba_peor_caso(tamanio):
    """
    PEOR CASO: Insertar un valor MENOR que todos (al inicio)
    
    Análisis:
    • Se recorre la lista completa en búsqueda: n comparaciones
    • Todos los elementos se desplazan: n desplazamientos
    • Total: 2n operaciones (pero sigue siendo O(n))
    • Complejidad: O(n)
    """
    lista = list(range(1, tamanio + 1))  # [1, 2, 3, ..., tamanio]
    valor = 0  # Menor que todos
    
    lista_resultado, stats = insertar_en_orden(lista, valor, contar_operaciones=True)
    
    return {
        'caso': 'PEOR',
        'descripcion': 'Insertar al INICIO (valor menor)',
        'tamanio': tamanio,
        'valor': valor,
        'posicion_insercion': stats['posicion'],
        'comparaciones': stats['comparaciones'],
        'desplazamientos': stats['desplazamientos'],
        'total_operaciones': stats['total_operaciones'],
        'complejidad': 'O(n)'
    }


def prueba_caso_promedio(tamanio):
    """
    CASO PROMEDIO: Insertar un valor en la MITAD
    
    Análisis:
    • Búsqueda hasta mitad: ~n/2 comparaciones
    • Desplazamientos de ~n/2 elementos: ~n/2 desplazamientos
    • Total: ~n operaciones
    • Complejidad: O(n)
    """
    lista = list(range(0, tamanio * 2, 2))  # [0, 2, 4, 6, ...]
    valor = tamanio  # Valor aproximadamente en la mitad
    
    lista_resultado, stats = insertar_en_orden(lista, valor, contar_operaciones=True)
    
    return {
        'caso': 'PROMEDIO',
        'descripcion': 'Insertar en la MITAD',
        'tamanio': tamanio,
        'valor': valor,
        'posicion_insercion': stats['posicion'],
        'comparaciones': stats['comparaciones'],
        'desplazamientos': stats['desplazamientos'],
        'total_operaciones': stats['total_operaciones'],
        'complejidad': 'O(n)'
    }


def prueba_caso_primero(tamanio):
    """
    Segundo peor caso: Insertar un valor MUY pequeño (casi al inicio)
    """
    lista = list(range(100, tamanio + 100))
    valor = 50  # Será uno de los primeros
    
    lista_resultado, stats = insertar_en_orden(lista, valor, contar_operaciones=True)
    
    return {
        'caso': 'PEOR (variante)',
        'descripcion': 'Insertar cerca del INICIO',
        'tamanio': tamanio,
        'valor': valor,
        'posicion_insercion': stats['posicion'],
        'comparaciones': stats['comparaciones'],
        'desplazamientos': stats['desplazamientos'],
        'total_operaciones': stats['total_operaciones'],
        'complejidad': 'O(n)'
    }


# ============================================================================
# EJECUCIÓN PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("=" * 100)
    print("EJERCICIO 2.2 — INSERCIÓN EN ORDEN (Lista Ordenada)")
    print("=" * 100)
    
    tamanios = [100, 1000, 10000]
    
    # ========================================================================
    # PARTE 1: Ejemplo ilustrativo
    # ========================================================================
    print("\n" + "=" * 100)
    print("PARTE 1: Ejemplo Ilustrativo")
    print("=" * 100)
    
    lista_ejemplo = [1, 3, 5, 7, 9, 11]
    print(f"\nLista original: {lista_ejemplo}")
    
    print("\n▼ Inserta el valor 6:")
    resultado, stats = insertar_en_orden(lista_ejemplo, 6, contar_operaciones=True)
    print(f"  → Posición de inserción: {stats['posicion']}")
    print(f"  → Comparaciones realizadas: {stats['comparaciones']}")
    print(f"  → Desplazamientos necesarios: {stats['desplazamientos']}")
    print(f"  → Lista resultante: {resultado}")
    
    print("\n▼ Inserta el valor 0 (menor que todos):")
    resultado, stats = insertar_en_orden(lista_ejemplo, 0, contar_operaciones=True)
    print(f"  → Posición de inserción: {stats['posicion']}")
    print(f"  → Comparaciones realizadas: {stats['comparaciones']}")
    print(f"  → Desplazamientos necesarios: {stats['desplazamientos']}")
    print(f"  → Lista resultante: {resultado}")
    
    print("\n▼ Inserta el valor 20 (mayor que todos):")
    resultado, stats = insertar_en_orden(lista_ejemplo, 20, contar_operaciones=True)
    print(f"  → Posición de inserción: {stats['posicion']}")
    print(f"  → Comparaciones realizadas: {stats['comparaciones']}")
    print(f"  → Desplazamientos necesarios: {stats['desplazamientos']}")
    print(f"  → Lista resultante: {resultado}")
    
    # ========================================================================
    # PARTE 2: MEJOR CASO
    # ========================================================================
    print("\n" + "=" * 100)
    print("PARTE 2: MEJOR CASO — Insertar al FINAL (valor mayor que todos)")
    print("=" * 100)
    
    print(f"\n{'Tamaño (n)':>12} | {'Valor':>8} | {'Posición':>10} | {'Comparaciones':>15} | {'Desplazamientos':>17} | {'Total Ops':>10}")
    print("-" * 100)
    
    for tamanio in tamanios:
        resultado = prueba_mejor_caso(tamanio)
        print(f"{resultado['tamanio']:>12} | {resultado['valor']:>8} | {resultado['posicion_insercion']:>10} | "
              f"{resultado['comparaciones']:>15} | {resultado['desplazamientos']:>17} | {resultado['total_operaciones']:>10}")
    
    print("\n💡 Análisis del Mejor Caso:")
    print("  • Se recorre TODA la lista para verificar que el valor es el mayor: n comparaciones")
    print("  • NO hay desplazamientos (insertamos al final): 0 desplazamientos")
    print("  • Total: n operaciones")
    print("  • Complejidad: O(n) - Dominada por la búsqueda")
    
    # ========================================================================
    # PARTE 3: PEOR CASO
    # ========================================================================
    print("\n" + "=" * 100)
    print("PARTE 3: PEOR CASO — Insertar al INICIO (valor menor que todos)")
    print("=" * 100)
    
    print(f"\n{'Tamaño (n)':>12} | {'Valor':>8} | {'Posición':>10} | {'Comparaciones':>15} | {'Desplazamientos':>17} | {'Total Ops':>10}")
    print("-" * 100)
    
    for tamanio in tamanios:
        resultado = prueba_peor_caso(tamanio)
        print(f"{resultado['tamanio']:>12} | {resultado['valor']:>8} | {resultado['posicion_insercion']:>10} | "
              f"{resultado['comparaciones']:>15} | {resultado['desplazamientos']:>17} | {resultado['total_operaciones']:>10}")
    
    print("\n💡 Análisis del Peor Caso:")
    print("  • Se recorre TODA la lista (valor menor: no entra al bucle): n comparaciones")
    print("  • TODOS los elementos se desplazan a la derecha: n desplazamientos")
    print("  • Total: n + n = 2n operaciones (pero sigue siendo O(n))")
    print("  • Complejidad: O(n) - Los desplazamientos dominan el costo")
    
    # ========================================================================
    # PARTE 4: CASO PROMEDIO
    # ========================================================================
    print("\n" + "=" * 100)
    print("PARTE 4: CASO PROMEDIO — Insertar en la MITAD")
    print("=" * 100)
    
    print(f"\n{'Tamaño (n)':>12} | {'Valor':>8} | {'Posición':>10} | {'Comparaciones':>15} | {'Desplazamientos':>17} | {'Total Ops':>10}")
    print("-" * 100)
    
    for tamanio in tamanios:
        resultado = prueba_caso_promedio(tamanio)
        print(f"{resultado['tamanio']:>12} | {resultado['valor']:>8} | {resultado['posicion_insercion']:>10} | "
              f"{resultado['comparaciones']:>15} | {resultado['desplazamientos']:>17} | {resultado['total_operaciones']:>10}")
    
    print("\n💡 Análisis del Caso Promedio:")
    print("  • Se recorre aproximadamente n/2 elementos: ~n/2 comparaciones")
    print("  • Aproximadamente n/2 elementos se desplazan: ~n/2 desplazamientos")
    print("  • Total: ~n operaciones")
    print("  • Complejidad: O(n)")
    
    # ========================================================================
    # PARTE 5: COMPARATIVA DE CASOS
    # ========================================================================
    print("\n" + "=" * 100)
    print("PARTE 5: COMPARATIVA DE CASOS (n = 10,000)")
    print("=" * 100)
    
    tamanio = 10000
    mejor = prueba_mejor_caso(tamanio)
    promedio = prueba_caso_promedio(tamanio)
    peor = prueba_peor_caso(tamanio)
    
    print(f"\n{'Caso':>15} | {'Comparaciones':>15} | {'Desplazamientos':>17} | {'Total Ops':>10} | {'Gráfico':>40}")
    print("-" * 100)
    
    casos_comparativa = [
        ('MEJOR', mejor['comparaciones'], mejor['desplazamientos'], mejor['total_operaciones']),
        ('PROMEDIO', promedio['comparaciones'], promedio['desplazamientos'], promedio['total_operaciones']),
        ('PEOR', peor['comparaciones'], peor['desplazamientos'], peor['total_operaciones'])
    ]
    
    for caso, comp, desp, total in casos_comparativa:
        barra = "█" * (total // 500)
        print(f"{caso:>15} | {comp:>15} | {desp:>17} | {total:>10} | {barra}")
    
    # ========================================================================
    # PARTE 6: RELACIÓN ENTRE DESPLAZAMIENTOS Y COMPLEJIDAD
    # ========================================================================
    print("\n" + "=" * 100)
    print("PARTE 6: RELACIÓN ENTRE DESPLAZAMIENTOS Y COMPLEJIDAD")
    print("=" * 100)
    
    print(f"\n{'Tamaño':>10} | {'Mejor Desp':>15} | {'Peor Desp':>15} | {'Factor (Peor/Mejor)':>20}")
    print("-" * 100)
    
    for tamanio in tamanios:
        mejor = prueba_mejor_caso(tamanio)
        peor = prueba_peor_caso(tamanio)
        factor = peor['desplazamientos'] / (mejor['desplazamientos'] + 1)  # +1 para evitar división por cero
        print(f"{tamanio:>10} | {mejor['desplazamientos']:>15} | {peor['desplazamientos']:>15} | {factor:>20.1f}x")
    
    print("\n💡 Interpretación:")
    print("  • Mejor caso: 0 desplazamientos")
    print("  • Peor caso: n desplazamientos")
    print("  • Los desplazamientos escalan LINEALMENTE con n")
    print("  • Por eso la complejidad es O(n)")
    
    # ========================================================================
    # PARTE 7: ANÁLISIS DETALLADO DE OPERACIONES
    # ========================================================================
    print("\n" + "=" * 100)
    print("PARTE 7: DESGLOSE DE OPERACIONES")
    print("=" * 100)
    
    print("\n▼ MEJOR CASO (insertar al final):")
    mejor = prueba_mejor_caso(1000)
    print(f"  Búsqueda:      {mejor['comparaciones']} comparaciones")
    print(f"  Desplazamiento: {mejor['desplazamientos']} elementos movidos")
    print(f"  Inserción:     1 operación (O(1))")
    print(f"  Total:         {mejor['total_operaciones']} operaciones → O(n)")
    
    print("\n▼ PEOR CASO (insertar al inicio):")
    peor = prueba_peor_caso(1000)
    print(f"  Búsqueda:      {peor['comparaciones']} comparaciones")
    print(f"  Desplazamiento: {peor['desplazamientos']} elementos movidos")
    print(f"  Inserción:     1 operación (O(1))")
    print(f"  Total:         {peor['total_operaciones']} operaciones → O(n)")
    
    print("\n▼ CASO PROMEDIO (insertar en mitad):")
    promedio = prueba_caso_promedio(1000)
    print(f"  Búsqueda:      {promedio['comparaciones']} comparaciones (≈ n/2)")
    print(f"  Desplazamiento: {promedio['desplazamientos']} elementos movidos (≈ n/2)")
    print(f"  Inserción:     1 operación (O(1))")
    print(f"  Total:         {promedio['total_operaciones']} operaciones → O(n)")
    
    # ========================================================================
    # RESUMEN TEÓRICO
    # ========================================================================
    print("\n" + "=" * 100)
    print("RESUMEN: INSERCIÓN EN LISTA ORDENADA")
    print("=" * 100)
    
    resumen = """
    ┌──────────────────────────────────────────────────────────────────┐
    │ ANÁLISIS DE COMPLEJIDAD: INSERCIÓN EN ORDEN                     │
    ├──────────────────────────────────────────────────────────────────┤
    │                                                                   │
    │ ALGORITMO:                                                       │
    │ 1. Buscar la posición correcta (búsqueda lineal)                │
    │ 2. Desplazar elementos a la derecha        │
    │ 3. Insertar el nuevo valor                                      │
    │                                                                   │
    │ MEJOR CASO: O(n)                                                 │
    │ ───────────────────────────────────────────────────────────────  │
    │ • Insertar al FINAL (valor mayor que todos)                    │
    │ • Comparaciones: n (se recorre toda la lista)                  │
    │ • Desplazamientos: 0 (no hay que mover nada)                   │
    │ • Total: n + 0 = n operaciones                                  │
    │ • Conclusión: O(n) por la búsqueda                             │
    │                                                                   │
    │ PEOR CASO: O(n)                                                  │
    │ ───────────────────────────────────────────────────────────────  │
    │ • Insertar al INICIO (valor menor que todos)                   │
    │ • Comparaciones: n (se recorre toda la lista)                  │
    │ • Desplazamientos: n (todos los elementos se desplazan)        │
    │ • Total: n + n = 2n operaciones                                 │
    │ • Conclusión: O(n) - el factor 2 se ignora en notación O       │
    │                                                                   │
    │ CASO PROMEDIO: O(n)                                              │
    │ ───────────────────────────────────────────────────────────────  │
    │ • Insertar en la MITAD                                          │
    │ • Comparaciones: ~n/2                                           │
    │ • Desplazamientos: ~n/2                                         │
    │ • Total: ~n operaciones                                          │
    │ • Conclusión: O(n)                                              │
    │                                                                   │
    │ COMPLEJIDAD ESPACIAL: O(1)                                       │
    │ • No se usan estructuras auxiliares que crezcan con n           │
    │                                                                   │
    │ FACTOR CLAVE: DESPLAZAMIENTOS                                    │
    │ ───────────────────────────────────────────────────────────────  │
    │ • Insertar al final:   0 desplazamientos → O(1)                │
    │ • Insertar en mitad:  ~n/2 desplazamientos → O(n)              │
    │ • Insertar al inicio:  n desplazamientos → O(n)                │
    │                                                                   │
    │ Los desplazamientos son la operación más costosa.              │
    │ Por eso la complejidad total es O(n) incluso en mejor caso.    │
    │                                                                   │
    │ COMPARACIÓN GENERAL:                                             │
    │ ───────────────────────────────────────────────────────────────  │
    │ • Con búsqueda lineal:  O(n) - Búsqueda lineal domina          │
    │ • Con búsqueda binaria: O(n) - Desplazamientos dominan         │
    │   (Búsqueda sería O(log n), pero desplazamientos siguen O(n))  │
    │                                                                   │
    │ ALTERNATIVA: Usar Estructuras Diferentes                        │
    │ ───────────────────────────────────────────────────────────────  │
    │ • Lista enlazada: O(n) búsqueda + O(1) inserción = O(n)        │
    │ • Árbol binario:  O(log n) búsqueda + O(1) inserción = O(log n)│
    │                                                                   │
    └──────────────────────────────────────────────────────────────────┘
    """
    print(resumen)
    
    # ========================================================================
    # CONCLUSIÓN
    # ========================================================================
    print("\n" + "=" * 100)
    print("CONCLUSIÓN Y REFLEXIÓN")
    print("=" * 100)
    
    conclusion = """
    La inserción en una lista ordenada es O(n) porque:
    
    1. BÚSQUEDA: O(n)
       - Recorremos la lista hasta encontrar la posición correcta
       - En peor caso, recorremos toda la lista
    
    2. DESPLAZAMIENTOS: O(n)
       - Mover n elementos toma O(n) tiempo
       - Es especialmente costoso insertar al inicio
    
    3. FACTOR LIMITANTE:
       - Aunque la inserción en sí es O(1), los desplazamientos son O(n)
       - Por eso el total es O(n)
       - No hay forma de optimizarlo sin cambiar la estructura de datos
    
    4. MEJORA CON BÚSQUEDA BINARIA:
       - La búsqueda podría ser O(log n) con búsqueda binaria
       - Pero los desplazamientos siguen siendo O(n)
       - Total seguiría siendo O(n)
    
    5. MEJOR ESTRUCTURA:
       - Para inserción frecuente con lista ordenada → Usar árbol rojo-negro
       - Permite O(log n) búsqueda e inserción
       - Más complejo de implementar pero mucho más eficiente
    """
    print(conclusion)
