'''Documentación oficial: https://playwright.dev/python/docs/locators'''
# ==============================
# IMPORTS
# ==============================
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright
# sync_playwright:
# API síncrona de Playwright.
# Permite controlar un navegador real (Chromium, Firefox, WebKit)
# como si fuera un usuario humano.

# urljoin:
# Une una url base con una url relativa
# Ej: urljoin("https://midu.dev", "/images/img.png")
# -> https://midu.dev/images/img.png


# ==============================
# url OBJETIVO
# ==============================

url = "https://midu.dev"


# ==============================
# CONTEXTO PLAYWRIGHT
# ==============================
# sync_playwright() inicia el motor de Playwright.
# Se usa como context manager (with) para asegurarse
# de que todos los procesos se cierren correctamente.

with sync_playwright() as p:

    # Lanzamos el navegador Chromium
    # headless=False -> se ve el navegador (modo visual)
    # headless=True  -> modo invisible (más rápido)
    browser = p.chromium.launch(headless=False)

    # Abrimos una nueva pestaña (page)
    page = browser.new_page()

    # Navegamos a la url indicada
    page.goto(url)


    # ==============================
    # INTERACCIÓN CON LA PÁGINA
    # ==============================

    # Buscamos el primer enlace (<a>) dentro de un <article>
    # locator() permite seleccionar elementos con CSS/XPath
    # .first selecciona el primer match
    primer_articulo_anchor = page.locator('article a').first

    # Simulamos un click real del usuario
    primer_articulo_anchor.click()


    # ==============================
    # ESPERAR CARGA DE LA NUEVA PÁGINA
    # ==============================

    # Espera a que la página termine de cargar
    # (network idle, DOM estable, etc.)
    page.wait_for_load_state()


    # ==============================
    # SCRAPING DE CONTENIDO
    # ==============================

    # Localizamos la primera imagen usando XPath absoluto
    # ⚠ XPath absoluto es frágil, pero sirve para ejemplo didáctico
    primera_imagen = page.locator(
        'xpath=/html/body/div[1]/div/div[1]/img'
    )

    # Extraemos el atributo "src" de la imagen
    imagen_src = primera_imagen.get_attribute('src')

    # Unimos la url base con el src de la imagen
    # (por si el src es relativo)
    imagen_url_completa = urljoin(url, imagen_src)

    # Mostramos el resultado
    print(f"La url de la primera imagen es: {imagen_url_completa}")


    # ==============================
    # CIERRE DEL NAVEGADOR
    # ==============================

    browser.close()
