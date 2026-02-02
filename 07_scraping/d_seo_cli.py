'''Documentacion de scrping usando beautiful soup'''
# ==============================
# IMPORTS
# ==============================
import sys
# Permite ejecutar comandos del sistema (ej: limpiar consola)
import os
import argparse      # Permite leer argumentos desde la línea de comandos
import requests      # Librería para realizar peticiones HTTP (GET, POST, etc.)
from bs4 import BeautifulSoup  # Parser HTML: convierte el HTML en un árbol navegable


# ==============================
# LIMPIAR CONSOLA (OPCIONAL)
# ==============================
# En Linux / macOS: clear
# En Windows: cls
# os.system() devuelve 0 si el comando fue exitoso
if os.system("clear") != 0:
    os.system("cls")


# ==============================
# ARGUMENTOS DE LÍNEA DE COMANDOS
# ==============================
# Creamos el parser de argumentos
parser = argparse.ArgumentParser(
    description="Scrapea un sitio web y valida títulos HTML"
)

# Argumento obligatorio: URL
parser.add_argument(
    "url",
    type=str,
    help="URL de la página a scrapear"
)

# Parseamos los argumentos ingresados por terminal
args = parser.parse_args()
url = args.url  # Guardamos la URL


# ==============================
# PETICIÓN HTTP
# ==============================
# Headers para simular un navegador real y evitar bloqueos
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# Realizamos la petición GET
response = requests.get(url, headers=headers, timeout=10)

# Mostramos el código de estado HTTP
print("Código HTTP:", response.status_code)

# Validamos si la respuesta fue exitosa
if response.status_code == 200:
    print("✅ Petición exitosa")
else:
    print("❌ Error en la petición")
    sys.exit(1)  # Cortamos el programa si falla


# ==============================
# PARSEO DEL HTML
# ==============================
# Creamos el objeto BeautifulSoup con el HTML recibido
soup = BeautifulSoup(response.text, 'html.parser')


# ==============================
# COLORES ANSI PARA TERMINAL
# ==============================
# Se usan para mejorar la legibilidad de la salida
RESET = "\x1b[0m"               # Resetea estilos
INFO = "\x1b[46m\x1b[30m"      # Fondo cian + texto negro
OK = "\x1b[32m"              # Verde
WARN = "\x1b[33m"              # Amarillo
ERROR = "\x1b[31m"              # Rojo
TITLE = "\x1b[1;34m"            # Azul + negrita


# ==============================
# MENSAJE PRINCIPAL
# ==============================
print(f"{INFO} Revisando la URL: {url} {RESET}\n")


# ==============================
# VALIDACIÓN DEL <title>
# ==============================
# Obtenemos el título de la página (si existe)
titulo_pagina = soup.title.string if soup.title else None

if titulo_pagina:
    print(f"{TITLE}📄 Título de la página:{RESET} {titulo_pagina}\n")

    longitud = len(titulo_pagina)

    # Reglas SEO básicas:
    # - Menos de 30 caracteres → corto
    # - Entre 30 y 70 → correcto
    # - Más de 70 → demasiado largo
    if 30 <= longitud <= 70:
        print(f"{OK}✅ El título es ADECUADO ({longitud} caracteres){RESET}\n")
    elif longitud > 70:
        print(f"{ERROR}❌ El título es DEMASIADO LARGO ({longitud} caracteres){RESET}\n")
    else:
        print(f"{WARN}⚠️ El título es DEMASIADO CORTO ({longitud} caracteres){RESET}\n")
else:
    print(f"{ERROR}❌ La página no tiene título (<title>){RESET}\n")


# ==============================
# VALIDACIÓN DE <h1>
# ==============================
# Extraemos todos los títulos h1
titulos_h1 = [titulo.text.strip() for titulo in soup.find_all('h1')]

if not titulos_h1:
    # No hay ningún h1
    print(f"{ERROR}❌ La página no tiene títulos h1 (<h1>){RESET}\n")

elif len(titulos_h1) > 1:
    # Hay más de un h1 (mala práctica SEO)
    print(f"{WARN}⚠️  La página tiene {len(titulos_h1)} títulos h1{RESET}\n")
    for titulo in titulos_h1:
        print(f"{TITLE}• {titulo}{RESET}")

else:
    # Exactamente un h1 (correcto)
    print(f"{OK}✅ La página tiene un solo título h1 (<h1>){RESET}\n")


# Uso --> navega al archivo cd nombre_archivo.py
# Haces correr el archivo que contien el codigo --> python nombre_archivo.py http://url_ejemplo
