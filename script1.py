import requests
from pymongo import MongoClient
import time

# Configuración
endpoint = 'https://api.citybik.es/v2/networks/bicicorunha'
mongo_uri = "mongodb+srv://Rep-7:changame@cluster0.m9dpb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
db_name = "bicicoruna"
collection_name = "stations"

# Conexión a MongoDB
client = MongoClient(mongo_uri)
db = client[db_name]
collection = db[collection_name]

# Función para solicitar y almacenar los datos
def fetch_and_store_data():
    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()
        stations = data['network']['stations']

        # Añadir marca de tiempo a todas las estaciones
        for station in stations:
            station["timestamp"] = time.time()

        # Insertar o actualizar todos los datos a la vez
        collection.insert_many(stations, ordered=False)

        print(f"Datos de {len(stations)} estacións almacenados con éxito en MongoDB.")
    else:
        print(f"Erro ao conectar á API: {response.status_code}")

# Ejecutar de manera continua
try:
    while True:
        fetch_and_store_data()  # Solicitar y almacenar los datos
        time.sleep(300) 
except KeyboardInterrupt:
    print("Ejecución detenida manualmente.")

# Cerrar conexión a MongoDB
client.close()
print("Conexión a MongoDB pechada.")
