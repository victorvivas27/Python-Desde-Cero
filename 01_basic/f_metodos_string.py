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
texto = "hola mundo"
print(texto.upper())  # HOLA MUNDO


# ----------------------------------------------------------
# MÉTODO .lower()
# ----------------------------------------------------------
# Convierte todos los caracteres de una cadena a minúsculas
texto = "HOLA MUNDO"
print(texto.lower())  # hola mundo


# ----------------------------------------------------------
# MÉTODO .capitalize()
# ----------------------------------------------------------
# Convierte la primera letra de la cadena a mayúscula
# y el resto a minúsculas
texto = "hola mundo"
print(texto.capitalize())  # Hola mundo


# ----------------------------------------------------------
# MÉTODO .title()
# ----------------------------------------------------------
# Convierte la primera letra de cada palabra a mayúscula
texto = "hola mundo"
print(texto.title())  # Hola Mundo


# ----------------------------------------------------------
# MÉTODO .swapcase()
# ----------------------------------------------------------
# Convierte mayúsculas en minúsculas y minúsculas en mayúsculas
texto = "Hola Mundo"
print(texto.swapcase())  # hOLA mUNDO


# ----------------------------------------------------------
# MÉTODO .count()
# ----------------------------------------------------------
# Cuenta cuántas veces aparece una subcadena dentro de la cadena
texto = "hola mundo hola"
print(texto.count("hola"))  # 2


# ----------------------------------------------------------
# MÉTODO .find()
# ----------------------------------------------------------
# Busca la primera ocurrencia de una subcadena
# Devuelve el índice donde comienza o -1 si no se encuentra
texto = "hola mundo"
print(texto.find("hola"))  # 0
print(texto.find("python"))  # -1


# ----------------------------------------------------------
# MÉTODO .replace()
# ----------------------------------------------------------
# Reemplaza una subcadena por otra
texto = "hola mundo"
print(texto.replace("hola", "adios"))  # adios mundo


# ----------------------------------------------------------
# MÉTODO .split()
# ----------------------------------------------------------
# Divide una cadena en una lista usando un separador
# Por defecto, separa por espacios
texto = "hola mundo"
print(texto.split())  # ['hola', 'mundo']


# ----------------------------------------------------------
# OPERADOR in
# ----------------------------------------------------------
# Verifica si una subcadena se encuentra dentro de la cadena
texto = "hola mundo"
print("hola" in texto)  # True
print("python" in texto)  # False

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
texto = "   hola mundo   "
print(texto.strip())  # hola mundo


# ----------------------------------------------------------
# MÉTODO .startswith()
# ----------------------------------------------------------
# Verifica si la cadena comienza con una subcadena
texto = "hola mundo"
print(texto.startswith("hola"))  # True
print(texto.startswith("mundo"))  # False


# ----------------------------------------------------------
# MÉTODO .endswith()
# ----------------------------------------------------------
# Verifica si la cadena termina con una subcadena
texto = "hola mundo"
print(texto.endswith("mundo"))  # True
print(texto.endswith("hola"))  # False


# ==========================================================
# ENCADENAMIENTO DE MÉTODOS DE STRING
# ==========================================================
# Los métodos de string pueden encadenarse porque cada uno
# devuelve una nueva cadena.

texto = "   hola mundo   "

# Ejemplo 1
print(texto.strip().capitalize())  # Hola mundo

# Ejemplo 2
print(texto.strip().capitalize().upper())  # HOLA MUNDO

# Ejemplo 3
print(texto.strip().capitalize().upper().replace("H", "X"))  # XOLA MUNDO

# Ejemplo 4
print(texto.strip().capitalize().upper().replace("H", "X").split())
# ['XOLA', 'MUNDO']

# Ejemplo 5
print(texto.strip().capitalize().upper().replace("H", "X").split()[0])
# XOLA

# Ejemplo 6
print(texto.strip().capitalize().upper().replace("H", "X").split()[0][0])
# X
