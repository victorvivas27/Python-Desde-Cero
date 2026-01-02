# ==========================================================
# TIPOS DE DATOS EN PYTHON
# ==========================================================
# Python es un lenguaje de tipado dinámico, lo que significa
# que no es necesario declarar el tipo de dato de una variable.
# El tipo se asigna automáticamente según el valor.
#
# Tipos de datos más comunes en Python:
# int, float, complex, NoneType, str, bool,
# list, tuple, dict, set
#
# La función type() devuelve el tipo de dato de un valor
# o de una variable.
# ==========================================================


# ----------------------------------------------------------
# TIPO DE DATO ENTERO (int)
# ----------------------------------------------------------
print("Tipo de dato int:")

# Números enteros positivos, negativos y cero
print(type(10))                             # <class 'int'>
print(type(0))                              # <class 'int'>
print(type(-10))                            # <class 'int'>

# Python soporta enteros de tamaño ilimitado
print(type(104563748498287476467378282883377373773646643))
# <class 'int'>


# ----------------------------------------------------------
# TIPO DE DATO FLOTANTE (float)
# ----------------------------------------------------------
print("\nTipo de dato float:")

# Números con decimales
print(type(10.5))                           # <class 'float'>
print(type(0.0))                            # <class 'float'>
print(type(-3.14))
