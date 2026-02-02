'''Documentacion de scrping usando beautiful soup'''
import re
import os            # Librería para interactuar con el sistema operativo
import sys
import requests      # Librería para hacer peticiones HTTP (GET, POST, etc.)
from bs4 import BeautifulSoup


# ----------------------------------------------------------
# LIMPIAR CONSOLA (OPCIONAL)
# ----------------------------------------------------------
# Intenta limpiar la consola en sistemas Linux / macOS ("clear")
# Si falla, intenta hacerlo en Windows ("cls")
if os.system("clear") != 0:
    os.system("cls")
# ------------------------------------------
# Scraping con BeautifulSoup
# ------------------------------------------
# Pro y contras de BeautifulSoup

# Pro
# Muy rápido y eficiente
# No depende de un navegador
# Fácil de implementar Y FACIL de encontrar atributos ,elementos y filtrar


# Contras
# No puede saltarse captchas o paywalls
# No ejecuta JavaScript
# No se puede navegar

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
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
title_tag = soup.title
if title_tag:
    # Se puede usar tambien .text
    print(f"El títutlo de la página es: {title_tag.string}\n")

metas = soup.title.parent.findAll('meta')
# Se puede usar tambien .text (metas)
print(f"Los metas de la página son: {metas}\n")

# Precio unitario del producto
# Saber que etiqueta contiene el precio unitario ayuda pero no es obligatorio
price_tag = soup.find('span', class_='nowrap')
print(f"El precio unitario del producto es: {price_tag.string}\n")


# Todos los precios unitarios de los productos
price_tags = soup.find_all('span', class_='nowrap')
for price in price_tags:
    print(f"Todos los precios unitarios del producto son: {price.text}\n")

# Todos los precios mas caractristicas  y titulo

# ----------------------------------------------------------
# URL A SCRAPEAR
# ----------------------------------------------------------
URL = "https://www.falabella.com/falabella-cl/brand/SAMSUNG"

# ----------------------------------------------------------
# PETICIÓN HTTP
# ----------------------------------------------------------
response = requests.get(URL, timeout=10)

if response.status_code == 200:
    print("Petición exitosa")
else:
    print("Error en la petición")
    sys.exit(1)

# ----------------------------------------------------------
# PARSEO DEL HTML
# ----------------------------------------------------------
soup = BeautifulSoup(response.text, 'html.parser')

# ----------------------------------------------------------
# OBTENER TÍTULO DE LA PÁGINA
# ----------------------------------------------------------
title_tag = soup.title
if title_tag:
    print(f"El título de la página es: {title_tag.string}\n")

# ----------------------------------------------------------
# BUSCAR BLOQUES DE PRODUCTOS
# ----------------------------------------------------------
products = soup.find_all(class_='jsx-636341914')

# ----------------------------------------------------------
# RECORRER PRODUCTOS
# ----------------------------------------------------------

# Recorremos cada producto
for product in products:

    # ----------------------------
    # NOMBRE DEL PRODUCTO
    # ----------------------------
    name_tag = product.find('b', class_='pod-subTitle')
    if not name_tag:
        continue

    name = name_tag.text.strip()

    # ----------------------------
    # PRECIO DEL PRODUCTO
    # ----------------------------
    PRECIO = None

    # Buscamos TODOS los span dentro del producto
    spans = product.find_all('span')

    for span in spans:
        text = span.text.strip()

        # Regex: busca precios tipo $ 899.990
        if re.search(r'\$\s*\d{1,3}(\.\d{3})*', text):
            PRECIO = text
            break

    # ----------------------------
    # MOSTRAR RESULTADO
    # ----------------------------
    if PRECIO:
        print(f"Producto: {name}")
        print(f"Precio: {PRECIO}\n")
