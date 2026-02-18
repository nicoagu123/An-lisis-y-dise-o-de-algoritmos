

"""
Mide memoria usada al construir una lista de los primeros n cuadrados
vs crear y consumir un generador que produce los mismos valores.

Uso:
    python medir_cuadrados_memoria.py 100000 1000000

Si no se pasan argumentos, usa n=100000 por defecto.
"""
import tracemalloc

# Tamaño grande para la prueba
n = 1_000_000

# --- Medición con lista ---
print("Creando lista de cuadrados...")
tracemalloc.start()                     # Empezamos a medir memoria
lista_cuadrados = [i**2 for i in range(1, n+1)]  # Creamos la lista
memoria_lista = tracemalloc.get_traced_memory()[1]  # Memoria pico (bytes)
tracemalloc.stop()                      # Paramos medición
memoria_lista_mb = memoria_lista / (1024 * 1024)  # Convertimos a MB

# --- Medición con generador ---
print("Consumiendo generador de cuadrados...")
tracemalloc.start()
gen_cuadrados = (i**2 for i in range(1, n+1))  # Generador (apenas ocupa memoria)
# Consumimos el generador convirtiéndolo a lista para forzar la generación de todos
lista_desde_gen = list(gen_cuadrados)
memoria_gen = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
memoria_gen_mb = memoria_gen / (1024 * 1024)

# Mostramos resultados
print("\n--- Resultados ---")
print(f"n = {n:,} elementos")
print(f"Memoria usada por la lista: {memoria_lista_mb:.2f} MB")
print(f"Memoria usada al consumir el generador (convertido a lista): {memoria_gen_mb:.2f} MB")
print("\nConclusión:")
print("- La lista ocupa memoria O(n) porque almacena todos los elementos a la vez.")
print("- El generador en sí mismo ocupa O(1) (solo guarda el estado), pero al consumirlo")
print("  (por ejemplo convirtiéndolo a lista) se genera la lista completa y ocupa O(n).")
print("  Sin embargo, si iteramos sin almacenar, la memoria se mantiene constante.")
