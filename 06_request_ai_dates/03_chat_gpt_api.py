from os import system
import requests
import json
import os
from dotenv import load_dotenv

# ----------------------------------------------------------
# CARGA DE VARIABLES DE ENTORNO
# ----------------------------------------------------------
# Cargamos las variables definidas en el archivo .env
load_dotenv()

# Obtenemos la API Key desde las variables de entorno
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
# Intentamos limpiar la consola según el sistema operativo:
# - "clear" funciona en Linux y macOS
# - "cls" funciona en Windows
# Si el primer comando falla, usamos el segundo
if system("clear") != 0:
    system("cls")

# ----------------------------------------------------------
# FUNCIÓN PARA LLAMAR A LA API DE OPENAI (RESPONSES API)
# ----------------------------------------------------------
def call_openai_api(OPENAI_API_KEY, prompt):
    """
    Realiza una petición POST a la API de OpenAI usando el endpoint
    moderno /v1/responses para generar una respuesta de texto.

    Parámetros:
    ----------
    OPENAI_API_KEY : str
        Clave de autenticación de OpenAI obtenida desde variables
        de entorno (.env).

    prompt : str
        Texto de entrada enviado al modelo (lo que el usuario quiere
        que el modelo responda).

    Retorna:
    -------
    dict
        Respuesta completa de la API en formato JSON convertida
        a un diccionario de Python.
    """

    # URL base del endpoint Responses
    URL_BASE = "https://api.openai.com/v1/responses"

    # Headers HTTP requeridos por la API
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    # Cuerpo de la petición
    # Usamos "input" en lugar de "messages" (API moderna)
    data = {
        "model": "gpt-4.1-mini",
        "input": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    # Enviamos la petición POST
    response = requests.post(URL_BASE, json=data, headers=headers)

    # Convertimos la respuesta a JSON y la retornamos
    return response.json()


# ----------------------------------------------------------
# LLAMADA A LA FUNCIÓN
# ----------------------------------------------------------
# Enviamos un prompt al modelo
api_response = call_openai_api(
    OPENAI_API_KEY,
    "Escribe un breve poema sobre la programacion en Python"
)

# ----------------------------------------------------------
# LECTURA DE LA RESPUESTA
# ----------------------------------------------------------
# La Responses API no usa 'choices'
# El texto generado se encuentra en:
# output -> content -> text
print(api_response["output"][0]["content"][0]["text"])
