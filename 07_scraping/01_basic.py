import requests      # Librería para hacer peticiones HTTP (GET, POST, etc.)
import re            # Librería para trabajar con expresiones regulares (regex)
import os            # Librería para interactuar con el sistema operativo

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
base_url = "https://www.apple.com/cl/shop/buy-mac"

# Realizamos una petición HTTP GET a la URL
response = requests.get(base_url)

# Verificamos si la petición fue exitosa
# Código 200 significa "OK"
if response.status_code == 200:
    print("Petición exitosa")
else:
    print("Error en la petición")
    exit()  # Salimos del programa si la petición falla

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
price_pattern = r'<span class="nowrap">(.*?)</span>'

# Buscamos la primera coincidencia en el HTML
match = re.search(price_pattern, html)

# Verificamos si se encontró algo
if match:
    # group(1) devuelve lo que capturó el (.*?)
    print(f"El precio es: {match.group(1)}")
else:
    print("No se encontró el precio")
