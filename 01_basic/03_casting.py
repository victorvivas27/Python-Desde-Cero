# ==========================================================
# CASTING (CONVERSIÓN DE TIPOS DE DATOS) EN PYTHON
# ==========================================================
# El casting es el proceso de convertir un tipo de dato
# en otro tipo diferente.
#
# Python proporciona funciones integradas para realizar
# estas conversiones de forma explícita.
#
# Funciones de casting más comunes:
#   int()   → Convierte a entero
#   float() → Convierte a número decimal
#   str()   → Convierte a cadena de texto
#   bool()  → Convierte a valor booleano
# ==========================================================


# ----------------------------------------------------------
# CASTING A ENTERO (int)
# ----------------------------------------------------------
print("Casting a entero (int):")

# De float a int:
# Se eliminan los decimales (NO redondea)
print(type(int(10.5)))      # <class 'int'>

# De string a int:
# La cadena debe contener SOLO números enteros
print(type(int("20")))      # <class 'int'>

# De booleano a int:
# True  → 1
# False → 0
print(type(int(True)))      # <class 'int'>
print(type(int(False)))     # <class 'int'>


# ----------------------------------------------------------
# CASTING A FLOTANTE (float)
# ----------------------------------------------------------
print("\nCasting a flotante (float):")

# De int a float
print(float(10))            # 10.0

# De string a float:
# La cadena debe representar un número válido
print(float("20.5"))        # 20.5

# De booleano a float:
# True  → 1.0
# False → 0.0
print(float(True))          # 1.0
print(float(False))         # 0.0


# ----------------------------------------------------------
# CASTING A CADENA DE TEXTO (str)
# ----------------------------------------------------------
print("\nCasting a cadena de texto (str):")

# Convierte números a texto
print(str(10))              # "10"
print(str(3.14))            # "3.14"

# Convierte booleanos a texto
print(str(True))            # "True"
print(str(False))           # "False"


# ----------------------------------------------------------
# CASTING A BOOLEANO (bool)
# ----------------------------------------------------------
print("\nCasting a booleano (bool):")

# NÚMEROS:
# 0        → False
# Cualquier otro número → True
print(bool(10))             # True
print(bool(0))              # False

# CADENAS DE TEXTO:
# Cadena vacía ("") → False
# Cualquier otra cadena → True
print(bool("Hello"))        # True
print(bool(""))             # False


# ----------------------------------------------------------
# RESUMEN IMPORTANTE
# ----------------------------------------------------------
# int()   → Elimina decimales, no redondea
# float() → Agrega decimales
# str()   → Convierte cualquier valor en texto
# bool()  → Evalúa si el valor es "vacío" o "cero"
#
# Valores considerados False en bool():
#   - 0
#   - 0.0
#   - ""
#   - None
#
# Todo lo demás se considera True
# ==========================================================
