import pandas as pd
from pymongo import MongoClient

# Configuración de MongoDB
mongo_uri = "mongodb+srv://Rep-7:changame@cluster0.m9dpb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
db_name = "bicicoruna"
collection_name = "stations"

def cargar_datos_y_exportar():
    """Cargar datos desde MongoDB y exportar únicamente los campos seleccionados a CSV y Parquet."""
    # Conectar a MongoDB
    client = MongoClient(mongo_uri)
    collection = client[db_name][collection_name]
    
    # Campos que se van a exportar
    campos_a_exportar = ["id", "name", "timestamp", "free_bikes", "empty_slots", "uid", "last_updated", "slots", "normal_bikes", "ebikes"]
    
    # Cargar datos desde MongoDB
    datos = list(collection.find({}, {campo: 1 for campo in campos_a_exportar}))  # Incluir sólo los campos necesarios

    if not datos:
        print("Non se atoparon datos en MongoDB.")
        return

    # Crear DataFrame con los datos seleccionados
    df = pd.DataFrame(datos)
    
    # Exportar a CSV
    df.to_csv("datos.csv", index=False)
    print("Datos exportados a 'datos.csv'.")

    # Exportar a Parquet
    try:
        df.to_parquet("datos.parquet", index=False)
        print("Datos exportados a 'datos.parquet'.")
    except Exception as e:
        print(f"Erro ao exportar a Parquet: {e}")

    # Cerrar conexión
    client.close()

if __name__ == "__main__":
    cargar_datos_y_exportar()