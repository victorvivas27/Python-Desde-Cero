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

nota = 7

# Operadores lógicos:
# and → ambas condiciones deben cumplirse
# or  → se cumple al menos una condición
# not → invierte el resultado de la condición

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("No estás calificado")


# ----------------------------------------------------------
# CONDICIONES MÚLTIPLES CON OPERADORES LÓGICOS
# ----------------------------------------------------------
print("Condiciones múltiples con operadores lógicos\n")

edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
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

a = 10
b = 20

if a < b:
    print(f"{a} es menor que {b}")

if a != b:
    print(f"{a} es diferente de {b}")

if a <= b:
    print(f"{a} es menor o igual que {b}")

if a == 10:
    print(f"{a} es igual a 10")

if b >= 15:
    print(f"{b} es mayor o igual que 15")

if b > a:
    print(f"{b} es mayor que {a}")


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
resultado = "Iguales" if 'hola' == 'hola' else "Diferentes"
print("Las cadenas son:", resultado)


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
    resultado = "Iguales"
else:
    resultado = "Diferentes"

print("Las cadenas son:", resultado)


