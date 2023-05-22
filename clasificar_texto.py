import openai 
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def clasificar_texto(texto):
    categorias = [
        "arte",
        "Ciencia",
        "Deportes",
        "Economia",
        "Educación",
        "Entretenimiento",
        "Medio Ambiente",
        "Politica",
        "Salud",
        "Tecnologia"
    ]
    
    prompt = f"Clasifica el siguiente texto '{texto}' solamente en una de estas categorias {','.join(categorias)}. La categoria es: "
    respuesta = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        n = 1,
        max_tokens = 50,
        temperature = 0.5
    )
    return respuesta.choices[0].text.strip()

texto_para_clasificar = input("Ingrese un texto: ")
clasificación = clasificar_texto(texto_para_clasificar)
print(clasificación)