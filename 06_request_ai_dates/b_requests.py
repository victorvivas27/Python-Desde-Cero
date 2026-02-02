'''Documentacion consumo de API con requests'''
from os import system
# import urllib.request
# import json

# ----------------------------------------------------------
# USAMOS LA LIBRERÍA requests (MÁS SIMPLE Y LEGIBLE)
# ----------------------------------------------------------
import requests

# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
# Intentamos limpiar la consola según el sistema operativo.
# - "clear" funciona en Linux y macOS
# - "cls" funciona en Windows
# Si el primer comando falla, usamos el segundo.
if system("clear") != 0:
    system("cls")


# ----------------------------------------------------------
# URL BASE DE LA API
# ----------------------------------------------------------
# Usamos JSONPlaceholder, una API pública para pruebas
BASE_URL = "https://jsonplaceholder.typicode.com/posts"


# ----------------------------------------------------------
# PETICIÓN GET USANDO urllib (FORMA NATIVA DE PYTHON)
# ----------------------------------------------------------
# Este bloque queda comentado porque:
# - No usa dependencias externas
# - Es más largo y difícil de leer
# - Sirve solo como ejemplo educativo

# try:
#     # Abrimos la URL y hacemos la petición GET
#     response = urllib.request.urlopen(BASE_URL)
#
#     # Leemos la respuesta (viene en bytes)
#     data = response.read()
#
#     # Convertimos los bytes a string y luego a JSON
#     json_data = json.loads(data.decode('utf-8'))
#
#     # Mostramos la respuesta completa
#     print(json_data)
#
#     # Cerramos la conexión
#     response.close()
# except urllib.error.URLError as e:
#     # Capturamos errores de conexión o URL
#     print(f"Error al hacer la solicitud GET: {e}")


# ----------------------------------------------------------
# PETICIÓN GET
# ----------------------------------------------------------
# Obtenemos todos los posts desde la API
try:
    print("Usando la libreria requests")
    print("\nHacemos la peticion GET: ")

    # Hacemos la solicitud GET
    response = requests.get(BASE_URL, timeout=10)

    # Convertimos la respuesta automáticamente a JSON
    data = response.json()

    # Mostramos solo el primer post
    print(data[0])

except requests.exceptions.RequestException as e:
    # Capturamos cualquier error de red
    print(f"Error al hacer la solicitud GET: {e}")


# ----------------------------------------------------------
# PETICIÓN POST
# ----------------------------------------------------------
# Creamos un nuevo recurso (post)
try:
    print("\nHacemos la peticion POST: ")

    response = requests.post(
        BASE_URL,
        timeout=10,
        json={
            "title": "foo",     # Título del post
            "body": "bar",      # Contenido del post
            "userId": 1,        # ID del usuario
        }
    )

    # Mostramos el código de estado HTTP
    print(response.status_code)

    # Mostramos la respuesta en formato JSON
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"Error al hacer la solicitud POST: {e}")


# ----------------------------------------------------------
# PETICIÓN PUT
# ----------------------------------------------------------
# Actualizamos COMPLETAMENTE el recurso con ID = 1
# PUT requiere enviar el objeto completo
try:
    print("\nHacemos la peticion PUT: ")

    response = requests.put(
        BASE_URL + "/1",
        timeout=10,
        json={
            "title": "Victor",  # Nuevo título
            "body": "Garcia",   # Nuevo contenido
            "userId": 1,        # Usuario asociado
        }
    )

    print(response.status_code)
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"Error al hacer la solicitud PUT: {e}")


# ----------------------------------------------------------
# PETICIÓN PATCH
# ----------------------------------------------------------
# Actualizamos SOLO los campos indicados
# PATCH no requiere enviar el objeto completo
try:
    print("\nHacemos la peticion PATCH: ")

    response = requests.patch(
        BASE_URL + "/1",
        timeout=10,
        json={
            "title": "Maria",   # Campo a modificar
            "body": "peron",   # Campo a modificar
        }
    )

    print(response.status_code)
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"Error al hacer la solicitud PATCH: {e}")
