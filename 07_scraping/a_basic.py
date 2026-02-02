'''Documentacion scraping de precios de apple usando regex'''
import os            # Librería para interactuar con el sistema operativo
import re            # Librería para hacer peticiones HTTP (GET, POST, etc.)
import sys
import requests

# ----------------------------------------------------------
# LIMPIAR CONSOLA (OPCIONAL)
# ----------------------------------------------------------
# Intenta limpiar la consola en sistemas Linux / macOS ("clear")
# Si falla, intenta hacerlo en Windows ("cls")
if os.system("clear") != 0:
    os.system("cls")

# ----------------------------------------------------------
# SCRAPING DE PRECIOS DE APPLE USANDO REGEX
# ----------------------------------------------------------
# Este método descarga el HTML directamente y busca datos
# usando expresiones regulares (NO usa navegador)
#
# PROS:
# - Muy rápido y eficiente
# - No depende de un navegador (Selenium, Playwright, etc.)
# - Fácil de implementar
#
# CONTRAS:
# - No puede saltarse captchas o paywalls
# - No ejecuta JavaScript
# - Es frágil: si cambia el HTML, el regex puede romperse
# ----------------------------------------------------------

# URL del sitio que queremos analizar
BASE_URL = "https://www.apple.com/cl/shop/buy-mac"

# Realizamos una petición HTTP GET a la URL
response = requests.get(BASE_URL, timeout=10)

# Verificamos si la petición fue exitosa
# Código 200 significa "OK"
if response.status_code == 200:
    print("Petición exitosa")
else:
    print("Error en la petición")
    sys.exit(1)  # Salimos del programa si la petición falla

# Guardamos el contenido HTML de la página como texto
html = response.text

# ----------------------------------------------------------
# EXPRESIÓN REGULAR PARA BUSCAR PRECIOS
# ----------------------------------------------------------
# Este patrón busca:
# <span class="nowrap">PRECIO</span>
#
# (.*?) captura cualquier contenido entre las etiquetas
# de forma no codiciosa (lazy)
PRECIO_PATRON = r'<span class="nowrap">(.*?)</span>'

# Buscamos la primera coincidencia en el HTML
match = re.search(PRECIO_PATRON, html)

# Verificamos si se encontró algo
if match:
    # group(1) devuelve lo que capturó el (.*?)
    print(f"El precio es: {match.group(1)}")
else:
    print("No se encontró el precio")
