'''Documentacion de expresiones regulares en Python'''
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
# METACARACTERES EN EXPRESIONES REGULARES (regex)
# ==========================================================
# Los metacaracteres son símbolos especiales que, dentro
# de una expresión regular, tienen un significado particular.
#
# En este archivo se practican metacaracteres como:
# - .   (comodín)
# - \.  (punto literal)
# - \\  (barra invertida literal)
# - \d  (dígito)
# - \w  (alfanumérico + _)
# - \s  (espacios en blanco)
# - ^   (inicio de cadena)
# - $   (fin de cadena)
# - \b  (límite de palabra)
# - |   (OR)
#
# Además se ven cuantificadores:
# - +       (uno o más)
# - {n}     (exactamente n)
# - {m,n}   (entre m y n)
# ==========================================================


# ----------------------------------------------------------
# 1) EL PUNTO . (comodín)
# ----------------------------------------------------------
# El punto coincide con "cualquier carácter" EXCEPTO salto de línea (\n)
TEXTO = "Hola mundo ,H#la soy victor ,HOla que tal"
PATRON = r"H.la"

found = re.findall(PATRON, TEXTO)
print("\n1) Uso de .")
print("Patrón:", PATRON)
print("Texto :", TEXTO)
print("Coincidencias:", found if found else "No encontrado")

# Ejemplo con palabras similares: c.sa encuentra "casa", "cosa", "cisa", "cesa"...
TEXTO = "casa caasa cosa cisa cesa causa"
PATRON = r"c.sa"

found = re.findall(PATRON, TEXTO)
print("\n1b) Otro ejemplo de .")
print("Patrón:", PATRON)
print("Texto :", TEXTO)
print("Coincidencias:", found if found else "No encontrado")


# ----------------------------------------------------------
# 2) BUSCAR UN PUNTO LITERAL \.
# ----------------------------------------------------------
# Como . es comodín, para buscar un punto REAL usamos \.
# La barra invertida "\" "escapa" al metacarácter.
TEXTO = "www.ejemplo.com www.ejemplo1.com www.ejemplo2.com"
PATRON = r"\."

found = re.findall(PATRON, TEXTO)
print("\n2) Punto literal con \\. (escape)")
print("Patrón:", PATRON)
print("Texto :", TEXTO)
print("Coincidencias:", found if found else "No encontrado")


# ----------------------------------------------------------
# 3) BUSCAR UNA BARRA INVERTIDA LITERAL \\
# ----------------------------------------------------------
# En regex, "\" es carácter de escape.
# Para buscar una "\" literal, necesitamos "\\"
# Usamos raw string r"\\", que es lo más cómodo.
TEXTO = r"C:\Users\Victor\Documents"
PATRON = r"\\"

found = re.findall(PATRON, TEXTO)
print("\n3) Barra invertida literal")
print("Patrón:", PATRON)
print("Texto :", TEXTO)
print("Coincidencias:", found if found else "No encontrado")


# ----------------------------------------------------------
# 4) \d (dígitos) + cuantificadores
# ----------------------------------------------------------
# \d coincide con un dígito (0-9)
TEXTO = "Mi numero de telefono es 1234567890"

PATRON = r"\d"
found = re.findall(PATRON, TEXTO)
print("\n4) \\d devuelve dígitos individuales")
print(found)

# + significa "uno o más" (junta la secuencia completa)
PATRON = r"\d+"
found = re.findall(PATRON, TEXTO)
print("\n4b) \\d+ junta secuencias de dígitos")
print(found)

# {10} significa "exactamente 10 dígitos"
PATRON = r"\d{10}"
found = re.findall(PATRON, TEXTO)
print("\n4c) \\d{10} busca exactamente 10 dígitos")
print(found)


# ----------------------------------------------------------
# 5) Buscar un prefijo específico (ej: +351) + número
# ----------------------------------------------------------
# Aquí usamos:
# - \+  para el signo + literal
# - \d{7} exactamente 7 dígitos
# - espacio literal
TEXTO = "Mi numero de telefono es +351 7178283"
PATRON = r"\+351 \d{7}"

found = re.search(PATRON, TEXTO)
print("\n5) Prefijo +351 y 7 dígitos")
print("Encontrado:", found.group() if found else "No encontrado")


# ----------------------------------------------------------
# 6) \w (alfanumérico y guion bajo)
# ----------------------------------------------------------
# \w coincide con:
# - letras a-z A-Z
# - números 0-9
# - guion bajo _
TEXTO = "variable1 _var2 3var var-4@$%"
PATRON = r"\w"

found = re.findall(PATRON, TEXTO)
print("\n6) \\w (caracteres alfanuméricos y _)")
print(found)

# Si quisieras "palabras completas" (secuencias), podrías usar:
PATRON = r"\w+"
# -> ['variable1', '_var2', '3var', 'var', '4']
palabras_completas = re.findall(PATRON, TEXTO)
print("\n6b) \\w+ (palabras completas)")
print(palabras_completas)


# ----------------------------------------------------------
# 7) \s (espacios en blanco)
# ----------------------------------------------------------
# \s coincide con:
# - espacio " "
# - tabulación "\t"
# - salto de línea "\n"
TEXTO = "Hola\tmundo\nEsto es una prueba "
PATRON = r"\s"

found = re.findall(PATRON, TEXTO)
print("\n7) \\s (espacios, tabs y saltos de línea)")
print(found)


# ----------------------------------------------------------
# 8) ^ (inicio de cadena)
# ----------------------------------------------------------
# ^ es un "ancla": NO busca en cualquier parte,
# obliga a que el patrón ocurra al INICIO.
#
# Ejemplo: ^\w significa "el primer carácter es alfanumérico o _"
TEXTO = "2334_name%%"
PATRON = r"^\w"

valid = re.search(PATRON, TEXTO)
print("\n8) ^ inicio de cadena")
print("Válido" if valid else "No válido")

# Validar comienzo de teléfono:
# ^\+\d{1,3}  significa:
# - empieza con "+"
# - seguido de 1 a 3 dígitos (código de país)
# - seguido de un espacio
TEXTO = "+222 7178283"
PATRON = r"^\+\d{1,3} "

valid = re.search(PATRON, TEXTO)
print("\n8b) Validar comienzo de teléfono")
print("Teléfono válido" if valid else "Teléfono no válido")


# ----------------------------------------------------------
# 9) $ (fin de cadena)
# ----------------------------------------------------------
# $ es otro ancla: obliga a que el patrón termine al FINAL.
TEXTO = "2334_name."
PATRON = r"name$"   # busca que la cadena termine exactamente en "name"

valid = re.search(PATRON, TEXTO)
print("\n9) $ fin de cadena")
print("Válido" if valid else "No válido")

# En este caso dará "No válido" porque el TEXTO termina en "name."
# (tiene un punto al final)


# ----------------------------------------------------------
# 10) \b (límite de palabra)
# ----------------------------------------------------------
# \b NO es "backspace" aquí.
# En regex significa "word boundary" (límite de palabra).
#
# Un "límite de palabra" es el punto donde cambia:
# - de letra/dígito/_  -> a algo que NO es letra/dígito/_
# o al revés.
#
# Ejemplo:
# \bc.sa\b significa:
# - empieza en un límite de palabra
# - luego "c" + cualquier caracter + "sa"
# - termina en un límite de palabra
#
# Esto evita capturar dentro de palabras más largas.
TEXTO = "casa caasa cosa cisa cesa causa casa"
PATRON = r"\bc.sa\b"

found = re.findall(PATRON, TEXTO)
print("\n10) \\b límites de palabra")
print(found)
# Aquí suelen salir: ['casa', 'cosa', 'cisa', 'cesa', 'casa']
# y NO suele incluir "caasa" ni "causa" porque no tienen 4 letras exactas con ese patrón.


# ----------------------------------------------------------
# 11) OR | (alternativas)
# ----------------------------------------------------------
# | permite buscar "una cosa u otra"
TEXTO = "Me gusta el color rojo y tambien el color azul, pero el azul es mejor que el rojo"
PATRON = r"rojo|azul"

found = re.findall(PATRON, TEXTO)
print("\n11) OR con |")
print(found)


# ----------------------------------------------------------
# 12) OR + metacaracteres (combinaciones)
# ----------------------------------------------------------
TEXTO = "pera,manzana,platano,piña,melón,aguacate,guayaba"

# Este patrón busca:
# - "palta" OR "melón" OR "p..a" OR cualquier palabra de 6 letras completa
# - p..a coincide con: p + (cualquier) + (cualquier) + a  -> ej: "pera", "piña" (según acentos)
# - \b\w{6}\b: palabra de exactamente 6 caracteres alfanuméricos/_ (ojo con acentos)
PATRON = r"palta|melón|p..a|\b\w{6}\b"

found = re.findall(PATRON, TEXTO)
print("\n12) OR combinado")
print(found)

# Nota importante:
# \w normalmente NO incluye letras con acento (depende del motor/configuración).
# Por eso palabras con "ó" o "ñ" pueden comportarse distinto con \w{6}.
