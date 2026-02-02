'''Documentacion de manipulacion de listas en Python'''
# ==========================================================
# MANIPULACIÓN DE LISTAS EN PYTHON
# ==========================================================
# En este archivo se trabajan las operaciones más comunes
# sobre listas:
# - Agregar elementos
# - Eliminar elementos
# - Ordenar listas
# - Buscar y contar elementos
#
# Las listas en Python son:
# - Ordenadas
# - Mutables
# - Permiten elementos repetidos
# ==========================================================


# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
import os
os.system('clear')  # En Windows suele usarse 'cls'


# ==========================================================
# AGREGAR ELEMENTOS A UNA LISTA
# ==========================================================

lista_01 = ['a', 'b', 'c', 'd', 'e']
print("Lista original:", lista_01)


# ----------------------------------------------------------
# append()
# ----------------------------------------------------------
# Agrega UN SOLO elemento al final de la lista
lista_01.append('f')
print("Después de append('f'):", lista_01)


# ----------------------------------------------------------
# insert()
# ----------------------------------------------------------
# Inserta un elemento en una posición específica
# insert(indice, elemento)
# El índice comienza en 0
lista_01.insert(2, '@')
print("Después de insert(2, '@'):", lista_01)


# ----------------------------------------------------------
# extend()
# ----------------------------------------------------------
# Agrega VARIOS elementos al final de la lista
# Recibe un iterable (lista, tupla, etc.)
lista_01.extend(['🤠', '😊'])
print("Después de extend(['🤠','😊']):", lista_01)


# ==========================================================
# ELIMINAR ELEMENTOS DE UNA LISTA
# ==========================================================

# ----------------------------------------------------------
# remove()
# ----------------------------------------------------------
# Elimina la PRIMERA aparición del valor indicado
# Si el elemento no existe → ValueError
lista_01.remove('@')
print("Después de remove('@'):", lista_01)


# ----------------------------------------------------------
# pop()
# ----------------------------------------------------------
# Elimina y devuelve el ÚLTIMO elemento de la lista
lista_01.pop()
print("Después de pop():", lista_01)


# ----------------------------------------------------------
# pop(indice)
# ----------------------------------------------------------
# Elimina el elemento en la posición indicada
lista_01.pop(0)
print("Después de pop(0):", lista_01)


# ----------------------------------------------------------
# del
# ----------------------------------------------------------
# Elimina un elemento por índice
del lista_01[2]
print("Después de del lista_01[2]:", lista_01)


# ----------------------------------------------------------
# clear()
# ----------------------------------------------------------
# Vacía completamente la lista
lista_01.clear()
print("Después de clear():", lista_01)


# ==========================================================
# ELIMINAR RANGO DE ELEMENTOS
# ==========================================================

lista_01 = ['🙈', '🙉', '🙊', '🐵']
print("Lista original:", lista_01)

# Elimina los elementos desde el índice 1 hasta el 3 (excluido)
del lista_01[1:3]
print("Después de del lista_01[1:3]:", lista_01)


# ==========================================================
# ORDENAR LISTAS
# ==========================================================

# ----------------------------------------------------------
# sort()
# ----------------------------------------------------------
# Ordena la lista original (MODIFICA la lista)
numeros = [5, 1, 2, 3, 4]
print("Lista original:", numeros)

numeros.sort()
print("Después de sort():", numeros)


# ----------------------------------------------------------
# sorted()
# ----------------------------------------------------------
# Devuelve una NUEVA lista ordenada
numeros_ordenados = [110, 23, 78, 99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista original:", numeros_ordenados)

sorted_numeros = sorted(numeros_ordenados)
print("Después de sorted():", sorted_numeros)


# ----------------------------------------------------------
# ORDENAR STRINGS
# ----------------------------------------------------------
lista_frutas = ['manzana', 'pera', 'naranja', 'anana', 'banana', 'kiwi']
print("Lista original:", lista_frutas)

sorted_frutas = sorted(lista_frutas)
print("Después de sorted():", sorted_frutas)


# ----------------------------------------------------------
# PROBLEMA CON MAYÚSCULAS
# ----------------------------------------------------------
# Las mayúsculas se ordenan antes que las minúsculas
lista_frutas = ['Manzana', 'Pera', 'naranja', 'anana', 'banana', 'kiwi']
print("Lista original:", lista_frutas)

sorted_frutas = sorted(lista_frutas)
print("Orden incorrecto:", sorted_frutas)


# ----------------------------------------------------------
# ORDEN CORRECTO USANDO key
# ----------------------------------------------------------
# key=str.lower fuerza la comparación en minúsculas
sorted_frutas = sorted(lista_frutas, key=str.lower)
print("Orden correcto con sorted():", sorted_frutas)

# Lo mismo usando sort()
lista_frutas.sort(key=str.lower)
print("Orden correcto con sort():", lista_frutas)


# ==========================================================
# BUSCAR Y CONTAR ELEMENTOS
# ==========================================================

animales = ['🐺', '🦊', '🐵', '🐷', '🐺', '🐹', '🐼', '🐻', '🐺', '🐵']


# ----------------------------------------------------------
# len()
# ----------------------------------------------------------
# Devuelve la cantidad total de elementos
print("Cantidad de elementos:", len(animales))


# ----------------------------------------------------------
# count()
# ----------------------------------------------------------
# Cuenta cuántas veces aparece un elemento
print("Cuántas veces aparece '🐺':", animales.count('🐺'))
print("Cuántas veces aparece '🐵':", animales.count('🐵'))


# ----------------------------------------------------------
# OPERADOR in
# ----------------------------------------------------------
# Devuelve True o False
print("'🐺' está en la lista:", '🐺' in animales)
print("'🐵' está en la lista:", '🐵' in animales)
print("'🦧' está en la lista:", '🦧' in animales)
