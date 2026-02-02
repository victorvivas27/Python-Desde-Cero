# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
from os import system
import re

# Intentamos limpiar consola en Linux / macOS.
# Si falla (retorna distinto de 0), usamos el comando de Windows.
if system("clear") != 0:
    system("cls")


# ==========================================================
# CUANTIFICADORES EN EXPRESIONES REGULARES (regex)
# ==========================================================
# Los cuantificadores indican CUÁNTAS VECES debe aparecer
# un patrón para que exista coincidencia.
#
# IMPORTANTE:
# El cuantificador SIEMPRE actúa sobre el elemento
# inmediatamente anterior.
# ==========================================================


# ----------------------------------------------------------
# 1) *  (cero o más repeticiones)
# ----------------------------------------------------------
# * permite que el patrón aparezca:
# - muchas veces
# - una vez
# - o ninguna vez (por eso puede devolver cadenas vacías)

TEXTO = "Holaa"
PATRON = r"a*"

found = re.findall(PATRON, TEXTO)
print("\n1) Uso de * (cero o más)")
print("Patrón:", PATRON)
print("Texto :", TEXTO)
print("Coincidencias:", found)

# Nota:
# Aparecen strings vacíos '' porque 'a*' también coincide
# cuando NO hay ninguna 'a'.


# ----------------------------------------------------------
# 2) +  (uno o más)
# ----------------------------------------------------------
# + exige que el patrón aparezca AL MENOS UNA VEZ.
# NO permite coincidencias vacías.

TEXTO = "Holaa a balon a"
PATRON = r"a+"

found = re.findall(PATRON, TEXTO)
print("\n2) Uso de + (uno o más)")
print("Patrón:", PATRON)
print("Texto :", TEXTO)
print("Coincidencias:", found)

# Aquí:
# - 'aa' es una coincidencia
# - 'a' también
# - NO hay strings vacíos


# ----------------------------------------------------------
# 3) ?  (cero o una vez)
# ----------------------------------------------------------
# ? hace que el carácter anterior sea OPCIONAL.

TEXTO = "Holaa a balon ab b"
PATRON = r"a?b"

found = re.findall(PATRON, TEXTO)
print("\n3) Uso de ? (cero o uno)")
print("Patrón:", PATRON)
print("Texto :", TEXTO)
print("Coincidencias:", found)

# Explicación:
# a?b significa:
# - puede haber una 'a' o no
# - PERO la 'b' es obligatoria
#
# Coincide con:
# - 'ab'
# - 'b'
# NO coincide con 'a' sola


# ----------------------------------------------------------
# 4) {n}  (exactamente n veces)
# ----------------------------------------------------------
# {n} exige que el patrón aparezca EXACTAMENTE n veces
# y además de forma CONSECUTIVA.

TEXTO = "Holaaa balon aba aaa a aa"
PATRON = r"a{3}"

found = re.findall(PATRON, TEXTO)
print("\n4) Uso de {n} (exactamente n)")
print("Patrón:", PATRON)
print("Texto :", TEXTO)
print("Coincidencias:", found)

# Solo coincide con:
# - 'aaa'
# NO coincide con:
# - 'aa'
# - 'a a'
# - 'aba'


# ----------------------------------------------------------
# 5) {m,n}  (entre m y n veces)
# ----------------------------------------------------------
# {m,n} busca entre m y n repeticiones CONSECUTIVAS.

TEXTO = "Holaaaa balon abaaaa aaa a aa"
PATRON = r"a{2,3}"

found = re.findall(PATRON, TEXTO)
print("\n5) Uso de {m,n} (entre m y n)")
print("Patrón:", PATRON)
print("Texto :", TEXTO)
print("Coincidencias:", found)

# IMPORTANTE:
# - SIEMPRE es consecutivo
# - No suma letras separadas
#
# 'aaaa' devuelve 'aaa'
# 'aa' devuelve 'aa'
# 'a a' NO coincide


# ----------------------------------------------------------
# 6) Palabras de 1 a 6 caracteres
# ----------------------------------------------------------
# \b   -> límite de palabra
# \w   -> letra, número o _
# {1,6} -> entre 1 y 6 caracteres

TEXTO = "ala casa árbol léon cinco murcielago"
PATRON = r"\b\w{1,6}\b"

found = re.findall(PATRON, TEXTO)
print("\n6) Palabras de 1 a 6 caracteres")
print("Patrón:", PATRON)
print("Texto :", TEXTO)
print("Coincidencias:", found)

# \b evita que se tomen partes de palabras largas


# ----------------------------------------------------------
# 7) Palabras de 6 o más caracteres
# ----------------------------------------------------------
# {6,} significa:
# - mínimo 6
# - sin límite máximo

TEXTO = "ala casa árbol léon cinco murcielago extraordinario"
PATRON = r"\b\w{6,}\b"

found = re.findall(PATRON, TEXTO)
print("\n7) Palabras de 6 o más caracteres")
print("Patrón:", PATRON)
print("Texto :", TEXTO)
print("Coincidencias:", found)

# NOTA:
# \w puede NO incluir letras con acento
# dependiendo del motor de regex
