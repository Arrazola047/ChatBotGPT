import os
import openai
from dotenv import load_dotenv

# Cargamos nuestra funcion env del modulo dotenv descargado en pip 
load_dotenv()

#Definimos nuestra API key 
apikey = os.getenv('OPENAI_API_KEY')
#Configuramos la biblioteca de openai
openai.apikey = apikey

#listamos los modelos disponibles para trabajar con la api de openAI y las almacenamos en la variable modelos
modelos = openai.Model.list()