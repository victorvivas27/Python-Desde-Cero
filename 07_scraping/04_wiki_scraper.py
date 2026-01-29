import requests      # Librería para hacer peticiones HTTP (GET, POST, etc.)
import os            # Librería para interactuar con el sistema operativo (por ejemplo, limpiar la consola)
from bs4 import BeautifulSoup  # Parser HTML: convierte el HTML en un “árbol” fácil de recorrer
from urllib.parse import urljoin  # Une una URL base con una URL relativa (ej: "/wiki/Python" -> "https://.../wiki/Python")


# ----------------------------------------------------------
# LIMPIAR CONSOLA (OPCIONAL)
# ----------------------------------------------------------
# En Linux/macOS el comando para limpiar es "clear"
# En Windows es "cls"
# os.system(...) devuelve 0 si el comando funcionó, y distinto de 0 si falló.
if os.system("clear") != 0:
    os.system("cls")


# ----------------------------------------------------------
# FUNCIÓN: OBTENER CONTENIDO DE UNA URL
# ----------------------------------------------------------
def obtener_contenido(url: str):
    # Headers: algunos sitios bloquean bots simples.
    # User-Agent “disfraza” la petición como si fuera un navegador real.
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    # Hacemos la petición HTTP GET a la URL
    # timeout=10: si tarda más de 10s, corta con error (evita que quede colgado)
    response = requests.get(url, headers=headers, timeout=10)

    # status_code: código de respuesta HTTP (200 OK, 404 Not Found, 500 Server Error, etc.)
    print("Código HTTP:", response.status_code)

    # Si no es 200, consideramos que falló y cortamos el programa
    if response.status_code == 200:
        print("✅ Petición exitosa")
    else:
        print("❌ Error en la petición")
        exit()

    # Creamos el "soup": BeautifulSoup parsea el HTML y lo convierte en un objeto navegable
    # 'html.parser' es el parser estándar incluido en Python
    soup = BeautifulSoup(response.text, 'html.parser')

    # ----------------------------------------------------------
    # 1) EXTRAER TODOS LOS TITULOS H1
    # ----------------------------------------------------------
    # soup.find_all('h1') devuelve una lista de etiquetas <h1> encontradas.
    # titulo.get_text(strip=True) saca texto limpio, evitando None y espacios raros.
    titulos_h1 = [titulo.get_text(strip=True) for titulo in soup.find_all('h1')]
    print("Títulos H1 encontrados:", titulos_h1)

    # ----------------------------------------------------------
    # 2) EXTRAER TODOS LOS ENLACES (A <a href="...">)
    # ----------------------------------------------------------
    # soup.find_all('a') devuelve todas las etiquetas <a>.
    # enlace.get('href') obtiene el valor de href (puede ser None si no existe).
    #
    # urljoin(url, href) convierte enlaces relativos en absolutos:
    # - href="/wiki/Python" => "https://es.wikipedia.org/wiki/Python"
    # - href="https://algo.com" queda igual
    enlaces = []
    for enlace in soup.find_all('a'):
        href = enlace.get('href')  # puede ser None
        if href:  # solo agregamos si existe href
            enlaces.append(urljoin(url, href))

    print("Cantidad de enlaces encontrados:", len(enlaces))
    # print(enlaces)  # descomentá si querés verlos todos

    # ----------------------------------------------------------
    # 3) EXTRAER og:image (Open Graph)
    # ----------------------------------------------------------
    # Open Graph (og:...) son metadatos que usan redes sociales / previews.
    # Se suelen ver así:
    # <meta property="og:image" content="https://.../imagen.jpg">
    #
    # OJO: soup.find(...) devuelve la primera coincidencia o None.
    og_image = soup.find('meta', {'property': 'og:image'})
    if og_image:
        # og_image['content'] obtiene el valor del atributo content.
        # Si por alguna razón no existe content, podría tirar KeyError,
        # pero en og:image normalmente siempre está.
        print("og:image (forma 1):", og_image['content'])
    else:
        print("No se encontró og:image (forma 1)")

    # Esta es otra forma equivalente de buscarlo:
    og_image_1 = soup.find("meta", property="og:image")
    if og_image_1:
        print("og:image (forma 2):", og_image_1["content"])
    else:
        print("No se encontró og:image (forma 2)")


# ----------------------------------------------------------
# EJECUCIÓN
# ----------------------------------------------------------
obtener_contenido("https://es.wikipedia.org/wiki/Python")
