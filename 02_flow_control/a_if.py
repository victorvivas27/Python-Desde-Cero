'''Documentacion de sentencias condicionales en Python'''
# ==========================================================
# SENTENCIAS CONDICIONALES (if, elif, else)
# ==========================================================
# Las sentencias condicionales permiten ejecutar diferentes
# bloques de código según si una condición es verdadera
# o falsa.
#
# Python evalúa las condiciones en tiempo de ejecución.
# ==========================================================


# ----------------------------------------------------------
# ESTRUCTURA BÁSICA DE if
# ----------------------------------------------------------
# Sintaxis:
#
# if condición:
#     bloque de código si la condición es verdadera
# else:
#     bloque de código si la condición es falsa
#
# IMPORTANTE:
# - Python usa indentación (tabulación) para definir bloques
# - No se utilizan llaves {}
# ----------------------------------------------------------


# ----------------------------------------------------------
# EJEMPLO BÁSICO DE if - else
# ----------------------------------------------------------
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# ----------------------------------------------------------
# USO DE elif (múltiples condiciones)
# ----------------------------------------------------------
# elif permite evaluar varias condiciones en orden.
# Python ejecuta SOLO el primer bloque verdadero.

NOTA = 7

# Operadores lógicos:
# and → ambas condiciones deben cumplirse
# or  → se cumple al menos una condición
# not → invierte el resultado de la condición

if NOTA >= 9:
    print("Sobresaliente")
elif NOTA >= 7:
    print("Notable")
elif NOTA >= 5:
    print("Aprobado")
else:
    print("No estás calificado")


# ----------------------------------------------------------
# CONDICIONES MÚLTIPLES CON OPERADORES LÓGICOS
# ----------------------------------------------------------
print("Condiciones múltiples con operadores lógicos\n")

EDAD = 25
TIENE_LICENCIA = True

if EDAD >= 18 and TIENE_LICENCIA:
    print("Puedes conducir un vehículo 🚘")
else:
    print("No puedes conducir un vehículo 🚫")


# ----------------------------------------------------------
# OPERADORES DE COMPARACIÓN
# ----------------------------------------------------------
# ==  Igualdad
# !=  Desigualdad
# >   Mayor que
# <   Menor que
# >=  Mayor o igual que
# <=  Menor o igual que

A = 10
B = 20

if A < B:
    print(f"{A} es menor que {B}")

if A != B:
    print(f"{A} es diferente de {B}")

if A <= B:
    print(f"{A} es menor o igual que {B}")

if A == 10:
    print(f"{A} es igual A 10")

if B >= 15:
    print(f"{B} es mayor o igual que 15")

if B > A:
    print(f"{B} es mayor que {A}")


# ----------------------------------------------------------
# EJEMPLO DE if ANIDADO (nested if)
# ----------------------------------------------------------
# Un if dentro de otro if

numero = int(input("Ingresa un número entero: "))

if numero >= 0:
    if numero == 0:
        print("El número es cero.")
    else:
        print("El número es positivo.")
else:
    print("El número es negativo.")


# ----------------------------------------------------------
# COMPARACIÓN DE CADENAS DE TEXTO (str)
# ----------------------------------------------------------
# El operador == también puede comparar strings.
# Compara el CONTENIDO de la cadena carácter por carácter.
# NO compara el tipo ni la cantidad de cadenas.
# Compara el CONTENIDO carácter por carácter.

print(
    "Comparación de cadenas:",
    'manzana' == 'manzana'   
)  # True
print('manzana' == 'manzana')   # True
print('manzana' == 'Manzana')   # False (mayúscula ≠ minúscula)
print('manzana' == 'pera')      # False
# ==========================================================
# OPERADOR TERNARIO (EXPRESIÓN CONDICIONAL)
# ==========================================================
# El operador ternario permite evaluar una condición
# y devolver un valor u otro en una sola línea.
#
# Es una forma corta de escribir un if - else simple.
# ==========================================================


# ----------------------------------------------------------
# SINTAXIS DEL OPERADOR TERNARIO
# ----------------------------------------------------------
# valor_si_verdadero if condición else valor_si_falso


# ----------------------------------------------------------
# EJEMPLO BÁSICO DE TERNARIA
# ----------------------------------------------------------
RESULTADO = "Iguales" if 'hola' == 'hola' else "Diferentes"
print("Las cadenas son:", RESULTADO)


# ----------------------------------------------------------
# COMPARACIÓN DE CADENAS EN TERNARIA
# ----------------------------------------------------------
# Las comparaciones de strings son sensibles a
# mayúsculas y minúsculas.

print('Hola' == 'hola')  # False


# ----------------------------------------------------------
# EQUIVALENTE USANDO if - else TRADICIONAL
# ----------------------------------------------------------
# El operador ternario es solo una forma abreviada
# de escribir este bloque:

if 'hola' == 'hola':
    RESULTADO = "Iguales"
else:
    RESULTADO = "Diferentes"

print("Las cadenas son:", RESULTADO)
