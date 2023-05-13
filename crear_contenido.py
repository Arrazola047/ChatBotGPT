import openai 
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def crear_contenido(tema, tokens, temperatura, modelo='text-davinci-002'):
    prompt = f"Escribe un articulo en español, que sea corto y hable sobre el siguiente tema: {tema}\n\n"
    respuesta = openai.Completion.create(
        engine = modelo,
        prompt = prompt,
        n = 1,
        max_tokens = tokens,
        temperature = temperatura
    )
    return respuesta.choices[0].text.strip()


def resumir_text(texto, tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Resume el siguiente texto: {texto}\n\n"
    respuesta = openai.Completion.create(
        engine = modelo, 
        prompt = prompt,
        n = 1,
        max_tokens = tokens,
        temperature = temperatura
    )
    return respuesta.choices[0].text.strip()

tema = input("Elije un tema para tu articulo: ")
tokens = int(input("Cuántos tokens maximos tendra tu articulo: "))
temperatura = int(input("Del 1 al 10 que tan creativo quieres que sea tu articulo? \n")) / 10

articulo_creado = crear_contenido(tema, tokens, temperatura)
print(articulo_creado)