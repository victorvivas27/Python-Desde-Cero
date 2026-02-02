"""
Documentación de los métodos de string en Python
================================================

Los métodos de string son funciones incorporadas en Python que permiten
manipular cadenas de texto.

IMPORTANTE:
-----------
Los strings en Python son INMUTABLES.
Esto significa que los métodos de string NO modifican la cadena original,
sino que devuelven una nueva cadena con el resultado.
"""
# ==========================================================


# ----------------------------------------------------------
# MÉTODO .upper()
# ----------------------------------------------------------
# Convierte todos los caracteres de una cadena a mayúsculas
TEXTO = "hola mundo"
print(TEXTO.upper())  # HOLA MUNDO


# ----------------------------------------------------------
# MÉTODO .lower()
# ----------------------------------------------------------
# Convierte todos los caracteres de una cadena a minúsculas
TEXTO = "HOLA MUNDO"
print(TEXTO.lower())  # hola mundo


# ----------------------------------------------------------
# MÉTODO .capitalize()
# ----------------------------------------------------------
# Convierte la primera letra de la cadena a mayúscula
# y el resto a minúsculas
TEXTO = "hola mundo"
print(TEXTO.capitalize())  # Hola mundo


# ----------------------------------------------------------
# MÉTODO .title()
# ----------------------------------------------------------
# Convierte la primera letra de cada palabra a mayúscula
TEXTO = "hola mundo"
print(TEXTO.title())  # Hola Mundo


# ----------------------------------------------------------
# MÉTODO .swapcase()
# ----------------------------------------------------------
# Convierte mayúsculas en minúsculas y minúsculas en mayúsculas
TEXTO = "Hola Mundo"
print(TEXTO.swapcase())  # hOLA mUNDO


# ----------------------------------------------------------
# MÉTODO .count()
# ----------------------------------------------------------
# Cuenta cuántas veces aparece una subcadena dentro de la cadena
TEXTO = "hola mundo hola"
print(TEXTO.count("hola"))  # 2


# ----------------------------------------------------------
# MÉTODO .find()
# ----------------------------------------------------------
# Busca la primera ocurrencia de una subcadena
# Devuelve el índice donde comienza o -1 si no se encuentra
TEXTO = "hola mundo"
print(TEXTO.find("hola"))  # 0
print(TEXTO.find("python"))  # -1


# ----------------------------------------------------------
# MÉTODO .replace()
# ----------------------------------------------------------
# Reemplaza una subcadena por otra
TEXTO = "hola mundo"
print(TEXTO.replace("hola", "adios"))  # adios mundo


# ----------------------------------------------------------
# MÉTODO .split()
# ----------------------------------------------------------
# Divide una cadena en una lista usando un separador
# Por defecto, separa por espacios
TEXTO = "hola mundo"
print(TEXTO.split())  # ['hola', 'mundo']


# ----------------------------------------------------------
# OPERADOR in
# ----------------------------------------------------------
# Verifica si una subcadena se encuentra dentro de la cadena
TEXTO = "hola mundo"
print("hola" in TEXTO)  # True
print("python" in TEXTO)  # False

# A diferencia de find():
# - in devuelve True o False
# - find devuelve el índice o -1


# ----------------------------------------------------------
# MÉTODO .join()
# ----------------------------------------------------------
# Une una lista de strings en una sola cadena usando un separador
PALABRAS = ["hola", "mundo","join"]
print(" ".join(PALABRAS))  # hola mundo join


# ----------------------------------------------------------
# MÉTODO .strip()
# ----------------------------------------------------------
# Elimina espacios en blanco al inicio y al final de la cadena
TEXTO = "   hola mundo   "
print(TEXTO.strip())  # hola mundo


# ----------------------------------------------------------
# MÉTODO .startswith()
# ----------------------------------------------------------
# Verifica si la cadena comienza con una subcadena
TEXTO = "hola mundo"
print(TEXTO.startswith("hola"))  # True
print(TEXTO.startswith("mundo"))  # False


# ----------------------------------------------------------
# MÉTODO .endswith()
# ----------------------------------------------------------
# Verifica si la cadena termina con una subcadena
TEXTO = "hola mundo"
print(TEXTO.endswith("mundo"))  # True
print(TEXTO.endswith("hola"))  # False


# ==========================================================
# ENCADENAMIENTO DE MÉTODOS DE STRING
# ==========================================================
# Los métodos de string pueden encadenarse porque cada uno
# devuelve una nueva cadena.

TEXTO = "   hola mundo   "

# Ejemplo 1
print(TEXTO.strip().capitalize())  # Hola mundo

# Ejemplo 2
print(TEXTO.strip().capitalize().upper())  # HOLA MUNDO

# Ejemplo 3
print(TEXTO.strip().capitalize().upper().replace("H", "X"))  # XOLA MUNDO

# Ejemplo 4
print(TEXTO.strip().capitalize().upper().replace("H", "X").split())
# ['XOLA', 'MUNDO']

# Ejemplo 5
print(TEXTO.strip().capitalize().upper().replace("H", "X").split()[0])
# XOLA

# Ejemplo 6
print(TEXTO.strip().capitalize().upper().replace("H", "X").split()[0][0])
# X
