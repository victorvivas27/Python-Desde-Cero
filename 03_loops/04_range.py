# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
import os
os.system('clear')  # En Windows suele usarse 'cls'


# ==========================================================
# range()
# ==========================================================
# La función range() se utiliza para generar una secuencia
# de números enteros.
#
# IMPORTANTE:
# - range NO devuelve una lista
# - Devuelve un objeto iterable de tipo range
# - Se evalúa de forma "perezosa" (lazy)
#
# Sintaxis general:
# range(inicio, fin, paso)
#
# - inicio: número desde donde comienza (incluido)
# - fin:    número donde termina (EXCLUÍDO)
# - paso:   incremento o decremento
# ==========================================================


# ----------------------------------------------------------
# range con UN solo parámetro
# ----------------------------------------------------------
# range(5) genera números desde 0 hasta 4
numeros = range(5)

print(type(numeros))   # <class 'range'>
print(numeros)         # range(0, 5)


# ----------------------------------------------------------
# CONVERTIR range A LISTA
# ----------------------------------------------------------
# Para ver los valores explícitamente
numeros = list(range(5))
print(numeros)


# ==========================================================
# ITERAR range CON for
# ==========================================================

print("\nRange un parámetro")

for num in range(5):
    print(f"Número del 0 al 4: {num}")


# ----------------------------------------------------------
# range CON DOS PARÁMETROS
# ----------------------------------------------------------
# range(inicio, fin)
# Comienza en inicio y termina en fin - 1

print("\nRange dos parámetros")

for num in range(0, 10):
    print(f"Número del 0 al 9: {num}")


# ----------------------------------------------------------
# range CON TRES PARÁMETROS
# ----------------------------------------------------------
# range(inicio, fin, paso)
# En este caso avanza de 2 en 2

print("\nRange tres parámetros")

for num in range(0, 10, 2):
    print(f"Números de a dos: {num}")


# ----------------------------------------------------------
# range CON NÚMEROS NEGATIVOS
# ----------------------------------------------------------
# El paso negativo permite recorrer hacia atrás
# IMPORTANTE: el paso DEBE ser negativo

print("\nRange con números negativos (decrementando)")

for num in range(10, 0, -1):
    print(f"Número: {num}")


# ==========================================================
# USO DE range PARA REPETIR n VECES
# ==========================================================
# A veces no necesitamos el valor del índice,
# solo queremos repetir algo n veces.
#
# La variable "_" es una convención:
# indica que el valor NO se va a usar.

print("\nRange con _")

for _ in range(5):
    print("Hola")
