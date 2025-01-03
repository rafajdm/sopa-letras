import requests
import json
import os
import random

from dotenv import load_dotenv
load_dotenv()

# Configurar la clave de API de OpenRouter y otros datos
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # Asegúrate de definir esta clave en tus variables de entorno
YOUR_SITE_URL = "https://tuaplicacion.com"  # Cambia al dominio de tu aplicación
YOUR_APP_NAME = "SopaDeLetrasGenerator"  # Cambia al nombre de tu aplicación

def get_related_words():
    """Genera palabras únicas que estén relacionadas entre sí por un tema general."""
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": f"{YOUR_SITE_URL}",
        "X-Title": f"{YOUR_APP_NAME}",
    }

    # Lista de temas posibles
    temas = ["frutas", "animales", "colores", "países", "ciudades", "comida", "deportes", "música", "películas", "libros"]
    tema_aleatorio = random.choice(temas)

    prompt = (
        f"Genera una lista de entre 20 y 30 palabras únicas en español relacionadas entre sí por el tema '{tema_aleatorio}'. "
        "Pueden ser nombres, verbos, adjetivos, etc. Las palabras han de tener un maximo de 10 caracteres. "
        "Solo responde con las palabras separadas por comas, sin repeticiones, sin números, sin introducciones, sin explicaciones. "
        "Por ejemplo, si el tema es 'frutas', podrías responder con 'manzana, pera, uva, fresa'. No incluyas palabras ofensivas o inapropiadas. "
        "Solo responde con lista de palabras separadas por comas, no incluyas datos del tema o cualquier informacion adicional."
    )
    data = json.dumps({
        "model": "meta-llama/llama-3.2-3b-instruct:free",  # Cambia si deseas usar otro modelo
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        result = response.json()
        completion = result['choices'][0]['message']['content'].strip()
        print("Respuesta completa del modelo:")
        print(completion)  # Imprime la respuesta completa, debería ser solo la lista de palabras

        # Procesar las palabras, asegurando que sean únicas
        words = [word.strip() for word in completion.split(",") if word.strip()]
        unique_words = list(dict.fromkeys(words))  # Eliminar duplicados manteniendo el orden
        return unique_words
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []