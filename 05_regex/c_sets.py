# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
# Importamos la función system para ejecutar comandos del sistema
from os import system
import re  # Módulo de expresiones regulares

# Intentamos limpiar la consola en Linux / macOS.
# Si falla (retorna distinto de 0), usamos el comando de Windows.
if system("clear") != 0:
    system("cls")

# ==========================================================
# USO DE [ ] EN EXPRESIONES REGULARES (REGEX)
# ==========================================================
# Los corchetes [ ] permiten definir un CONJUNTO de caracteres.
# Indican qué caracteres SON VÁLIDOS para UNA posición.
#
# Ejemplo:
#   [abc]  → puede ser 'a', 'b' o 'c'
#   [0-9]  → cualquier número
#   [a-z]  → letras minúsculas
#
# Dentro de los corchetes:
# - El punto (.) NO significa "cualquier carácter"
# - Muchos metacaracteres pierden su significado especial
# ==========================================================


# ----------------------------------------------------------
# 1) VALIDACIÓN DE UN USERNAME
# ----------------------------------------------------------
NOMBRE_USUARIO = "rub.%ius_69+"

# ^  → inicio de la cadena
# $  → fin de la cadena
# [\w.%+-] → conjunto de caracteres permitidos
# +  → uno o más caracteres del conjunto
#
# \w incluye:
# - letras (a-z, A-Z)
# - números (0-9)
# - guión bajo (_)
#
# El patrón valida que TODA la cadena sea válida
PATRON = r"^[\w.%+-]+$"

match = re.search(PATRON, NOMBRE_USUARIO)

print("\n1) Uso de [ ] para definir un conjunto de caracteres")
if match:
    print(match.group())
    print(f"El NOMBRE_USUARIO '{NOMBRE_USUARIO}' es válido")
else:
    print(f"El NOMBRE_USUARIO '{NOMBRE_USUARIO}' NO es válido")


# ----------------------------------------------------------
# 2) ENCONTRAR VOCALES EN UN TEXTO
# ----------------------------------------------------------
TEXTO = "Hola Mundo, hoy es un buen día para aprender regex."

# Buscamos vocales, incluyendo vocales con tilde
PATRON = r"[aeiouáéíóú]"

# findall devuelve TODAS las coincidencias
found = re.findall(PATRON, TEXTO)

print("\n2) Uso de [ ] para encontrar vocales en un TEXTO")
print(found)


# ----------------------------------------------------------
# 3) ENCONTRAR PALABRAS ESPECÍFICAS CON UN CONJUNTO
# ----------------------------------------------------------
# Queremos encontrar:
# man, fan y ban
#
# [mfb] → la palabra puede empezar con m, f o b
# an     → termina en 'an'
TEXTO = "man ran fan ban pan tan"

PATRON = r"[mfb]an"
found = re.findall(PATRON, TEXTO)

print("\n3) Uso de [ ] para encontrar fan, man y ban")
print(found)


# ----------------------------------------------------------
# 4) USO DE LÍMITES DE PALABRA (\b)
# ----------------------------------------------------------
# \b indica un LÍMITE de palabra
# Evita encontrar coincidencias dentro de palabras más largas
TEXTO = "amniman fanatico man bandana"

PATRON = r"\b[mfb]an\b"
found = re.findall(PATRON, TEXTO)

print("\n4) Uso de [ ] con límites de palabra")
print(found)


# ----------------------------------------------------------
# 5) ENCONTRAR DÍGITOS EN UN TEXTO
# ----------------------------------------------------------
TEXTO = "Los números de la suerte son 3, 7, 13, 21 y 42."

# [0-9] → cualquier dígito
PATRON = r"[0-9]"
found = re.findall(PATRON, TEXTO)

print("\n5) Uso de [ ] para encontrar dígitos en un TEXTO")
print(found)


# ----------------------------------------------------------
# 6) USO DE RANGOS NUMÉRICOS
# ----------------------------------------------------------
TEXTO = "Los números del 1 al 10 son: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10."

# [2-5] → solo números del 2 al 5
PATRON = r"[2-5]"
found = re.findall(PATRON, TEXTO)

print("\n6) Uso de [ ] para encontrar dígitos del 2 al 5")
print(found)


# ----------------------------------------------------------
# 7) LETRAS MAYÚSCULAS Y MINÚSCULAS
# ----------------------------------------------------------
TEXTO = "Abecedario: A, B, C, D, E, F, G, H, I, J, K, L."

# [a-zA-Z] → cualquier letra, sin importar mayúscula o minúscula
PATRON = r"[a-zA-Z]"
found = re.findall(PATRON, TEXTO)

print("\n7) Uso de [ ] para encontrar letras")
print(found)


# ----------------------------------------------------------
# 8) NEGACIÓN DE UN CONJUNTO
# ----------------------------------------------------------
# ^ dentro de [ ] significa NEGACIÓN
# Es decir: "todo lo que NO sea..."
TEXTO = "Vocales y consonantes: a, e, i, o, u, b, c, d, f, g."

# Encuentra todo lo que NO es vocal
PATRON = r"[^aeiou]"
found = re.findall(PATRON, TEXTO)

print("\n8) Uso de [ ] para encontrar caracteres que NO son vocales")
print(found)
