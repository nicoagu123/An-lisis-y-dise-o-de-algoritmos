

"""
Ejercicio 2.2 — Inserción en Orden (en Lista Ordenada)
Análisis de complejidad: Búsqueda + Desplazamientos
"""


def insertar_en_orden(lista, numero):
    """
    Inserta 'numero' en 'lista' (ordenada ascendentemente) manteniendo el orden.
    """
    # Buscar la posición donde debería ir el número
    posic = 0
    while posic < len(lista) and lista[posic] < numero:
        posic += 1
    # Insertar en la posición encontrada
    lista.insert(posic, numero)

# Ejemplo de uso
lista = [1, 3, 5, 7, 9]
nuevo_numero = int(input("Ingrese un número para insertar en la lista ordenada: "))
insertar_en_orden(lista, nuevo_numero)
print("Lista después de la inserción:", lista)
