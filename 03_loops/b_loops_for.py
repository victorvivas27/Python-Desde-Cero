# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
import os
os.system('clear')  # En Windows suele usarse 'cls'


# ==========================================================
# BUCLE for
# ==========================================================
# El bucle for permite ejecutar un bloque de código
# recorriendo (iterando) un objeto iterable.
#
# Un iterable puede ser:
# - Lista
# - Cadena (string)
# - Tupla
# - Rango (range)
# - Etc.
# ==========================================================


# ----------------------------------------------------------
# ITERAR UNA LISTA
# ----------------------------------------------------------
frutas = ["manzana", "banana", "kiwi", "mango"]

# Para cada elemento dentro de la lista "frutas"
# se ejecuta una iteración del bucle
for fruta in frutas:
    print(fruta)


# ----------------------------------------------------------
# ITERAR UNA CADENA (STRING)
# ----------------------------------------------------------
cadena = "Python"

# Cada carácter del string se recorre uno por uno
for letra in cadena:
    print(letra)


# ==========================================================
# USO DE enumerate()
# ==========================================================
# enumerate() permite obtener:
# - El índice
# - El valor del iterable
# en cada iteración

frutas = ["manzana", "banana", "kiwi", "mango"]

for index, fruta in enumerate(frutas):
    print(f"Índice: {index} | Fruta: {fruta}")


# ==========================================================
# BUCLES for ANIDADOS
# ==========================================================
# Un bucle for puede estar dentro de otro for.
# El bucle interno se ejecuta COMPLETO por cada
# iteración del bucle externo.

frutas = ["manzana", "banana", "kiwi", "mango"]

for index, fruta in enumerate(frutas):
    print(f"\nÍndice: {index} | Fruta: {fruta}")

    # Bucle interno: recorre cada letra de la fruta
    for letra in fruta:
        print(letra)


# ----------------------------------------------------------
# ¿CÓMO FUNCIONAN LOS for ANIDADOS?
# ----------------------------------------------------------
# 1) El for externo toma un elemento
# 2) El for interno se ejecuta COMPLETO
# 3) Cuando termina el for interno,
#    el for externo pasa al siguiente elemento
# ----------------------------------------------------------


# ==========================================================
# USO DE break EN for
# ==========================================================
# break finaliza el bucle cuando se cumple una condición

print("\nBreak")

animales = ["perro", "gato", "conejo"]

for index, animal in enumerate(animales):
    print(animal)

    if animal == "gato":
        print(f"El gato se encontró en el índice {index}")
        break


# ==========================================================
# USO DE continue EN for
# ==========================================================
# continue salta la iteración actual
# y pasa directamente a la siguiente

print("\nContinue")

animales = ["perro", "gato", "conejo", "loro", "mono"]

for index, animal in enumerate(animales):

    if animal == "gato":
        continue   # Salta el print de "gato"

    print(animal)


# ==========================================================
# COMPRENSIÓN DE LISTAS (List Comprehension)
# ==========================================================
# Es una forma corta y eficiente de crear listas
# a partir de otra lista o iterable.
#
# Sintaxis básica:
# [expresión for elemento in iterable]
# ==========================================================

animales = ["perro", "gato", "conejo", "loro", "mono"]

# Convertir todos los elementos a mayúsculas
animales_mayusculas = [animal.upper() for animal in animales]
print(animales_mayusculas)


# ----------------------------------------------------------
# COMPRENSIÓN DE LISTAS CON CONDICIÓN
# ----------------------------------------------------------
# Sintaxis:
# [expresión for elemento in iterable if condición]

numeros = [2, 4, 67, 34, 89, 6, 5, 2, 45, 67, 89]

# Crear una lista solo con números pares
numeros_pares = [num for num in numeros if num % 2 == 0]
print(numeros_pares)
