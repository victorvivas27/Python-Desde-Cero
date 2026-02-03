'''Docstring para 06_request_ai_dates.e_clase_api_chat.py'''
from dataclasses import dataclass
import os
import requests
from dotenv import load_dotenv

# ----------------------------------------------------------
# LIMPIAR CONSOLA (OPCIONAL)
# ----------------------------------------------------------
if os.system("clear") != 0:
    os.system("cls")

# ----------------------------------------------------------
# CARGA DE VARIABLES DE ENTORNO
# ----------------------------------------------------------
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError(
        "ERROR: OPENAI_API_KEY no está definida en el archivo .env")

# ----------------------------------------------------------
# CLASE PARA CONSUMIR LA API DE OPENAI
# ----------------------------------------------------------


@dataclass
class ApiChat:
    '''Clase para consumir la API de OpenAI'''
    # ----------------------------------------------------------
    # CONSTRUCTOR
    # Dentro del __init__ se definen los atributos de la clase
    # Si definimos los atributos de la clase, podemos acceder a ellos
    # desde cualquier método de la clase
    # El parámetro model recibe un dato de tipo str y lo indicamos con model: str.
    # Esto se llama type hints (pistas de tipo).
    # ----------------------------------------------------------

    def __init__(self, api_key: str, url: str, model: str):
        self.api_key = api_key
        self.url = url
        self.model = model

    def generate_response(self, prompt: str) -> str:
        '''Genera una respuesta de la API de OpenAI'''
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": self.model,
            "input": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        try:
            response = requests.post(
                self.url,
                json=data,
                headers=headers,
                timeout=30
            )
# ----------------------------------------------------------
# TRATAMIENTO DE ERRORES
# Usando raise_for_status(), que es un método del objeto response (requests)
# y lanza una excepción si la petición HTTP devuelve un error (4xx o 5xx)
# ----------------------------------------------------------
            response.raise_for_status()
            res_json = response.json()

            return res_json["output"][0]["content"][0]["text"]

        except requests.exceptions.Timeout:
            return "Error: tiempo de espera agotado"

        except requests.exceptions.HTTPError as e:
            return f"Error HTTP: {e}"

        except requests.exceptions.RequestException as e:
            return f"Error de conexión: {e}"

        except (KeyError, IndexError):
            return "Error: formato inesperado de la respuesta"


# ----------------------------------------------------------
# USO DE LA CLASE
# ----------------------------------------------------------
# Si colocamos una condición con:
# if __name__ == "__main__":
# nos aseguramos de que ESTE ARCHIVO se ejecute directamente
# y que NO se ejecute automáticamente cuando se importa
if __name__ == "__main__":
    open_ia = ApiChat(
        api_key=OPENAI_API_KEY,
        url="https://api.openai.com/v1/responses",
        model="gpt-4.1-mini"
    )

    texto_ingreso = "Escribe un breve poema sobre la programación en Python"
    respuesta = open_ia.generate_response(texto_ingreso)

    print("\n--- RESPUESTA DEL MODELO ---\n")
    print(respuesta)
    print("\n--- FIN DEL PROGRAMA ---")
