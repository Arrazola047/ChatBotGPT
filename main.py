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
prompt = "Cuenta una historia breve de maximo 100 tokens, sobre un viaje a un país latinoamericano, debes mencionar el nombre del país por lo menos una vez"

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
print("***")

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
modelo_spacy = spacy.load("es_core_news_md")
#Debemos descargar el modelo es core news md desde terminal para python 
#python -m spacy download es_core_news_md

analisis = modelo_spacy(texto_generado) # Analizamos y guardamos en una variable, en este caso la llamaremos analisis

"""
# Hacemos uso de un for para imprimir los tokens generados de manera individual 
for token in analisis:
    print(token.text, token.dep_, token.head.text)
    # Token text imprime los tokens por texto y token.pos_ nos imprime la categoria gramatical (en ingles)de cada palabra
    # token.dep imprime la dependencia y token.head.text imprime el encabezado
     
"""

# identificamos las identidades

"""
for ent in analisis.ents:
    print(ent.text, ent.label_)
    # ent.text imprime las entidades del texto y ent.label imprime las etiquetas que identifican a la entidad
"""
    
    
"""
Luego de analizar la respuesta podemos utilizar la informacion extraida para mejorar la interaccion con chat gpt 
podemos analiazr la respuesta y usarla para dar una respuesta mas especifica para chat gpt
Supongamos que en la respuesta obtenemos una entidad de tipo loc, que se refiere a localizacíon y deseamos obtener mas información especifica sobre esa ubicación

Por ejemplo, generaremos una respuesta con relación a francia 
"""

"""
ubicación = None

# Usamos un for para recorrer el arreglo de strings (texto) en busca de entidades relacionadas con localizaciónes, para almacenarlas en la variable ubicación 

for ent in analisis.ents:
    if ent.label_ == 'LOC':
        ubicación = ent
        break # Es necesario hacer uso de un break para detener el loop en el momento en el que se encuentre una localización
    
# ahora generamos un nuevo pedido en base a esta palabra 
if ubicación: 
    prompt2 = f"Dime más acerca de {ubicación} en español"
    respuesta2 = openai.Completion.create(
        engine = modelo,
        prompt = prompt2,
        n=1,
        max_tokens = 100
    )
print(respuesta2.choices[0].text.strip())
"""