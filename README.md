# ProyectoSistemas-Raul

## Descripción

Este repositorio contiene dos scripts que interactúan con unha API e MongoDB. O primeiro script conecta á API a intervalos regulares para obter e almacenar os datos nunha base de datos MongoDB. O segundo script recupera os datos almacenados e os exporta a un dataframe de pandas, exportando os datos en formatos CSV e Parquet.

---

## Script 1: Conexión á API e Almacenamento en MongoDB

### Descripción

Este script realiza unha conexión á API a intervalos regulares (configurables, por exemplo, cada X minutos) e obtén datos para almacenalos nunha base de datos MongoDB. A execución do script non para ata que se cancele manualmente.

### Funcionalidade

- Conéctase á API a intervalos regulares (e.g., cada 10 segundos).
- Obtén os datos de resposta da API.
- Almacena os datos na base de datos MongoDB.
- A execución do script continuará sen interrupción ata que se cancele manualmente.

### Código do Script

```python
import requests
from pymongo import MongoClient
import time

# Configuración
endpoint = 'https://api.citybik.es/v2/networks/bicicorunha'  # URL da API de CityBike para obter datos de estacións
mongo_uri = "mongodb+srv://Rep-7:changame@cluster0.m9dpb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # URI de conexión a MongoDB
db_name = "bicicoruna"  # Nome da base de datos de MongoDB
collection_name = "stations"  # Nome da colección onde se almacenarán as estacións

# Conexión a MongoDB
client = MongoClient(mongo_uri)  # Establecer a conexión coa base de datos MongoDB
db = client[db_name]  # Acceder á base de datos específica
collection = db[collection_name]  # Acceder á colección específica

# Función para solicitar y almacenar los datos
def fetch_and_store_data():
    response = requests.get(endpoint)  # Solicitar datos á API

    if response.status_code == 200:  # Se a resposta é correcta
        data = response.json()  # Obter os datos en formato JSON
        stations = data['network']['stations']  # Obter a lista de estacións

        # Engadir unha marca de tempo a todas as estacións
        for station in stations:
            station["timestamp"] = time.time()

        # Insertar ou actualizar todos os datos na colección MongoDB
        collection.insert_many(stations, ordered=False)

        print(f"Datos de {len(stations)} estacións almacenados con éxito en MongoDB.")
    else:
        print(f"Erro ao conectar á API: {response.status_code}")  # Mostrar erro en caso de falla na conexión

# Executar de maneira continua
try:
    while True:
        fetch_and_store_data()  # Solicitar y almacenar los datos
        time.sleep(10)  # Esperar 10 segundos antes de solicitar os datos novamente
except KeyboardInterrupt:
    print("Ejecución detenida manualmente.")  # Mensaxe ao interromper a execución manualmente

# Cerrar conexión a MongoDB
client.close()
print("Conexión a MongoDB pechada.")
