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

# API Keys obtenidas desde variables de entorno
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

# ----------------------------------------------------------
# LIMPIAR LA CONSOLA (OPCIONAL)
# ----------------------------------------------------------
# Intentamos limpiar la consola según el sistema operativo:
# - "clear" → Linux / macOS
# - "cls"   → Windows
if system("clear") != 0:
    system("cls")

# ==========================================================
# OPENAI - RESPONSES API (MODELO MODERNO)
# ==========================================================
def call_openai_api(api_key, prompt):
    """
    Realiza una petición POST a la API de OpenAI usando el endpoint
    moderno /v1/responses.

    Este endpoint reemplaza a:
    - /v1/chat/completions
    - /v1/completions

    Parámetros:
    ----------
    api_key : str
        Clave de autenticación de OpenAI.

    prompt : str
        Texto que se envía al modelo.

    Retorna:
    -------
    dict
        Respuesta completa de la API en formato JSON.
    """

    url = "https://api.openai.com/v1/responses"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # En Responses API se usa "input", NO "messages"
    data = {
        "model": "gpt-4.1-mini",
        "input": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()


# ==========================================================
# DEEPSEEK - CHAT COMPLETIONS (OPENAI COMPATIBLE)
# ==========================================================
def call_DeepSeek_api_corrected(api_key, prompt):
    """
    Realiza una petición POST a la API de DeepSeek usando el endpoint
    compatible con OpenAI: /v1/chat/completions.

    IMPORTANTE:
    - DeepSeek NO usa Responses API
    - Usa Chat Completions (formato clásico)

    Parámetros:
    ----------
    api_key : str
        Clave de autenticación de DeepSeek.

    prompt : str
        Texto enviado al modelo.

    Retorna:
    -------
    str | dict
        - Texto generado por el modelo si la petición es exitosa
        - JSON con error si la petición falla
    """

    url = "https://api.deepseek.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # En Chat Completions se usa "messages"
    data = {
        "model": "deepseek-chat",  # Alternativa: "deepseek-reasoner"
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        # En chat completions, el texto está en choices
        return result["choices"][0]["message"]["content"]
    else:
        # Devuelve el error completo para debugging
        return response.json()


# ==========================================================
# PRUEBAS
# ==========================================================
# --- DeepSeek ---
# try:
#     respuesta_deepseek = call_DeepSeek_api_corrected(
#         DEEPSEEK_API_KEY,
#         "Escribe un breve poema sobre la programacion en Python"
#     )
#     print("Respuesta DeepSeek:\n")
#     print(respuesta_deepseek)
# except Exception as e:
#     print(f"Error DeepSeek: {e}")

# --- OpenAI (descomentar si querés probarlo) ---
api_response_openai = call_openai_api(
    OPENAI_API_KEY,
    "Escribe un breve poema sobre la programacion en Python"
)
print("\nRespuesta OpenAI:\n")
print(api_response_openai["output"][0]["content"][0]["text"])
