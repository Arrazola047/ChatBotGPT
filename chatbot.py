# Establecemos las bibliotecas
import openai 
import os 
from dotenv import load_dotenv

# Configuracion basica para nuestras api 
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

#Configuracion para mantener el contexto de las conversaciones 
preguntas_anteriores = []
respuestas_anteriores = []

def preguntar_chat_gpt(prompt, modelo="text-davinci-002"):
    respuesta = openai.Completion.create(
        engine = modelo, 
        prompt = prompt,
        n = 1,
        max_tokens = 150,
        temperature = 0.7
    )
    return respuesta.choices[0].text.strip()

print("Bienvenido a chatbot v0.0.1 (BETA). Escribe 'Adios' cuando quieras terminar")

while True:
    conversacion_historica = "" # variable que se alimentara de las preguntas y respuestas del chat
    ingreso_usuario = input("\nUsuario - ")
    if ingreso_usuario.lower() == "adios":
        prompt = "despidete en español"
        respuesta_gpt = preguntar_chat_gpt(prompt)
        print(f"ChatBot: {respuesta_gpt}")
        break
    
    for pregunta, respuesta in zip (preguntas_anteriores, respuestas_anteriores):
        conversacion_historica += f"El usuario pregunta: {pregunta}\n"
        conversacion_historica += f"GPT responde: {respuesta}\n"
        
    prompt = f"El usuario pregunta: {ingreso_usuario}"
    conversacion_historica += prompt
    respuesta_gpt = preguntar_chat_gpt(prompt)
    print(f"{respuesta_gpt}") 
    
    preguntas_anteriores.append(ingreso_usuario) # Agregamos a nuestro array correspondiente las preguntas hechas por el usuario
    respuestas_anteriores.append(respuesta_gpt) # Agregamos a nuestro array correspondiente las respuestas hechas por el modelo IA 
    
"""
Para mantener el contexto de las conversaciones podemos hacer uso de una variable string para almacenar los mensajes anteriores 
al enviar esta cadena junto con la nueva pregunta para gpt el modelo va a poder dar una pregunta mas especifica y mas coherente
ahora lo que necesitamos es configurar una base datos con sql para conectarla por medio de python 
"""