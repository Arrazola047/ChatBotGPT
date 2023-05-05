import os
import openai
import spacy
from dotenv import load_dotenv

# Cargamos nuestra funcion env del modulo dotenv descargado en pip 
load_dotenv()

#Definimos nuestra API key 
apiKey = os.getenv('OPENAI_API_KEY')
#Configuramos la biblioteca de openai
openai.api_key = apiKey

"""
#listamos los modelos disponibles para trabajar con la api de openAI y las almacenamos en la variable modelos
modelos = openai.Model.list()

#imprimimos la variable modelos, la cual contiene una lista de los modelos disponibles
print(modelos)
"""

# Ahora usaremos un modelo llamado davinci para generar peticiones desde python

modelo = "text-davinci-002"
#prompt = input("Introduce tu prompt: ")
#temperatura = float(input("Con que temperatura deseas generar tu respuesta?: "))
prompt = "Cuenta una historia breve."

#Enviamos la peticion

respuesta = openai.Completion.create(
    engine = modelo,            # Especificamos el modelo de lenguaje que usaremos
    prompt = prompt,            # Especificamos cual es la pregunta introducida
    n = 1,                      # Podemos especificar el numero de respuestas que queremos recibir
    #temperature = temperatura,  # Especificamos la temperatura de la respuesta
    max_tokens = 100             # Especificamos los tokens por respuesta
)

# Procesamos y mostramos la respuesta


texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)


# Procesamos mas de una respuesta 

"""
for idx, opcion in enumerate(respuesta.choices): 
    texto_generado = opcion.text.strip()
    print(f"Respuesta {idx + 1}: {texto_generado}\n")
"""
    


# Para procesar mas de una respuesta necesitamos hacer uso de un loop for 
"""
Existen varios parametros que nos permiten configurar varios aspectos de nuestro texto a generar
entre ellos se encuentra: 

Temperatura: Se refiere a la creatividad de la respuesta, donde el valor minimo es super rebuscado y puede llegar a repetir palabras
                y el valor maximo es mas general y menos especifico, donde varia mas sus respuestas y que tan aleatorias serán varia en valores de 0.1 hasta 1
                Un valor bajo minimiza la cantidad de riesgos en la ambiguedad de respuestas 
                Un valor alto genera respuestas mas creativas y humanas

Tokens máximos: Se refiere al largo de palabras por respuesta, recordemos que cada token usado tiene un costo dependiendo del modelo utilizado
                por lo que necesitamos una estrategia de cache para reducir costos en el uso de la API 
                
Cantidad de respuestas: Con este parametro definiremos que cantidad de respuesta queremos recibir
"""

# Ahora haremos uso de una API de Spacy, descargando e instalando Spacy desde pip 