
"""
Ejercicio 1.1 — Operaciones O(1)
Programa que realiza operaciones de tiempo constante O(1)
"""


def es_par(n):
    """
    Determina si un número es par o impar.
    
    Tiempo: O(1) - La operación módulo (%) en Python es una operación 
    aritmética básica que toma tiempo constante, independientemente del 
    valor de n.
    
    Espacio: O(1) - Solo usamos una variable booleana para el resultado,
    sin importar qué tan grande sea n.
    """
    resultado = (n % 2 == 0)
    return resultado


def ultimo_digito(n):
    """
    Obtiene el último dígito de un número.
    
    Tiempo: O(1) - La operación módulo (n % 10) es una operación aritmética
    constante que no depende del número de dígitos de n. El número de 
    dígitos en realidad es log₁₀(n), pero acceder a cualquier dígito 
    mediante módulo es O(1).
    
    Espacio: O(1) - Almacenamos solo un entero (el último dígito),
    sin dependencia del tamaño de n.
    """
    resultado = abs(n) % 10  # abs() para manejar números negativos
    return resultado


def maximo_dos_numeros(a, b):
    """
    Devuelve el mayor entre dos números usando una condición.
    
    Tiempo: O(1) - Una comparación entre dos números es una operación
    fundamental que toma tiempo constante. No importa cuán grandes sean
    a y b, la comparación toma siempre el mismo tiempo.
    
    Espacio: O(1) - Solo almacenamos una variable con el resultado,
    sin uso de estructuras de datos adicionales.
    """
    if a >= b:
        resultado = a
    else:
        resultado = b
    return resultado


# Ejemplo alternativo más conciso (con operador ternario):
def maximo_dos_numeros_v2(a, b):
    """Versión alternativa usando operador ternario."""
    return a if a >= b else b


# ============================================================================
# PRUEBAS
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("EJERCICIO 1.1 — OPERACIONES O(1)")
    print("=" * 60)
    
    # Prueba 1: Números pares e impares
    print("\n[OPERACIÓN 1] ¿Es par o impar?")
    print("-" * 60)
    numeros_prueba = [10, 7, 0, -3, 100]
    for n in numeros_prueba:
        es_par_resultado = es_par(n)
        tipo = "par" if es_par_resultado else "impar"
        print(f"  n = {n:4} → {tipo}")
    
    # Prueba 2: Último dígito
    print("\n[OPERACIÓN 2] Obtener el último dígito")
    print("-" * 60)
    numeros_prueba = [12345, 7, 1000, -567, 0]
    for n in numeros_prueba:
        ultimo = ultimo_digito(n)
        print(f"  n = {n:6} → último dígito = {ultimo}")
    
    # Prueba 3: Mayor entre dos números
    print("\n[OPERACIÓN 3] Mayor entre dos números")
    print("-" * 60)
    pares = [(5, 3), (10, 20), (-1, -5), (0, 0), (100, 50)]
    for a, b in pares:
        maximo = maximo_dos_numeros(a, b)
        print(f"  max({a:4}, {b:4}) = {maximo}")
    
    print("\n" + "=" * 60)
    print("ANÁLISIS DE COMPLEJIDAD")
    print("=" * 60)
    
    analisis = """
    ┌─────────────────────────────────────────────────────────────┐
    │ RESUMEN DE COMPLEJIDAD                                      │
    ├─────────────────────────────────────────────────────────────┤
    │                                                              │
    │ 1. es_par(n):                                              │
    │    • Tiempo:  O(1) - Una operación módulo es constante     │
    │    • Espacio: O(1) - Solo una variable booleana            │
    │                                                              │
    │ 2. ultimo_digito(n):                                       │
    │    • Tiempo:  O(1) - Operación módulo es constante         │
    │    • Espacio: O(1) - Solo un entero de salida              │
    │                                                              │
    │ 3. maximo_dos_numeros(a, b):                              │
    │    • Tiempo:  O(1) - Una comparación es constante          │
    │    • Espacio: O(1) - Solo una variable para el resultado   │
    │                                                              │
    │ CONCLUSIÓN: Todas operan en tiempo constante porque:      │
    │ • No iteran sobre los datos                               │
    │ • No recursionan                                            │
    │ • No acceden a estructuras que crecen con el input         │
    │ • Realizan siempre el mismo número de operaciones          │
    │                                                              │
    └─────────────────────────────────────────────────────────────┘
    """
    print(analisis)



