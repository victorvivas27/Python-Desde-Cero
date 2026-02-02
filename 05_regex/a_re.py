'''Documentacion de expresiones regulares en Python'''


# ¿Por qué aprender Regex?

# -Búsqueda avanzada:
# Encontrar patrones específicos en textos grandes de forma rápida y precisa.

# - Validación de datos:
# Verificar que un email, teléfono, contraseña, etc. tengan el formato correcto.

# - Manipulación de texto:
# Extraer, reemplazar y modificar cadenas fácilmente.

# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
from os import system
# ==========================================================
# IMPORTAR EL MÓDULO re
# ==========================================================
import re

# Intentamos limpiar consola en Linux / macOS
# Si falla (retorna distinto de 0), usamos el comando de Windows
if system("clear") != 0:
    system("cls")


# ==========================================================
# EXPRESIONES REGULARES (regex / re)
# ==========================================================
# Las expresiones regulares son secuencias de caracteres
# que definen un PATRÓN de búsqueda.
#
# Se usan para:
# - Buscar texto
# - Validar datos (email, teléfono, etc.)
# - Extraer información
# - Reemplazar partes de un texto
# ==========================================================

# ==========================================================
# PASO 2: DEFINIR UN PATRÓN
# ==========================================================
# El patrón es una cadena de texto que define
# lo que queremos buscar
PATRON = "Hola"


# ==========================================================
# PASO 3: DEFINIR EL TEXTO DONDE BUSCAR
# ==========================================================
TEXTO = "Hola, este es un ejemplo de expresión regular. Hola de nuevo."


# ==========================================================
# PASO 4: BUSCAR EL PATRÓN EN EL TEXTO
# ==========================================================
# re.search() busca la PRIMERA coincidencia
result = re.search(PATRON, TEXTO)

if result:
    print("Patrón encontrado")
else:
    print("Patrón no encontrado")


# ----------------------------------------------------------
# result.group()
# ----------------------------------------------------------
# Devuelve el texto que coincide con el patrón
print(result.group())


# ----------------------------------------------------------
# result.start() y result.end()
# ----------------------------------------------------------
# Indican la posición donde se encontró la coincidencia
print(f"Patrón encontrado en la posición: {result.start()} - {result.end()}")


# ==========================================================
# BUSCAR TODAS LAS COINCIDENCIAS
# ==========================================================
# re.findall() devuelve una LISTA con todas las coincidencias

TEXTO = "Hola, este es un ejemplo de expresión regular. Hola de nuevo. Hola otra vez."
all_results = re.findall(PATRON, TEXTO)

print(all_results)
print(len(all_results))  # Cantidad de coincidencias encontradas


# ==========================================================
# USO DE re.finditer()
# ==========================================================
# re.finditer() devuelve un ITERADOR con objetos match
# Es útil cuando queremos información detallada
# de cada coincidencia

matches = re.finditer(PATRON, TEXTO)

for match in matches:
    print(match.group(), match.start(), match.end())


# ==========================================================
# MODIFICADORES (FLAGS)
# ==========================================================
# Los modificadores cambian el comportamiento de la búsqueda
#
# re.IGNORECASE o re.I:
# - Ignora mayúsculas y minúsculas

PATRON = "hola"
TEXTO = "Hola, este es un ejemplo de expresión regular. hola de nuevo. Hola otra vez."

all_results = re.findall(PATRON, TEXTO, re.IGNORECASE)
print(all_results)


# ==========================================================
# REEMPLAZAR TEXTO CON re.sub()
# ==========================================================
# re.sub() reemplaza coincidencias del patrón
#
# Parámetros:
# re.sub(patrón, reemplazo, texto, count)
#
# count:
# - Limita la cantidad de reemplazos
# - Por defecto reemplaza TODAS las coincidencias

TEXTO = "Hola, este es un ejemplo de expresión regular. Hola de nuevo."
PATRON = "Hola"
REMPLAZO = "Adiós"

# Reemplaza SOLO la primera ocurrencia
new_text = re.sub(PATRON, REMPLAZO, TEXTO, count=1)
print(new_text)
