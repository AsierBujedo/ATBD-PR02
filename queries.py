import time, os, json
from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
SERVER = os.getenv("SERVER")
PORT = os.getenv("PORT")
UNAME = quote_plus(os.getenv("USERNAME"))
UPASS = quote_plus(os.getenv("PASSWORD"))

# Conexión a MongoDB
client = MongoClient(f'mongodb://{UNAME}:{UPASS}@{SERVER}:{PORT}/')
db = client['football']
collection = db['players']

def measure_query_time(query):
    start_time = time.time()  # Tiempo inicial
    result = list(collection.find(query))  # Ejecuta la consulta
    end_time = time.time()  # Tiempo final
    execution_time = end_time - start_time  # Calcula el tiempo

    # Mostrar resultados en JSON
    pretty_result = json.dumps(result, indent=4, default=str)  # Formato JSON legible
    return execution_time, pretty_result

# a.i Filtrar por el año de comienzo mayor a 2020
query_ai = {"EstimatedStartYear": {"$gt": 2020}}
time_ai, result_ai = measure_query_time(query_ai)
print("Resultado: \n" + str(result_ai))
print(f"Consulta a.i ejecutada en {time_ai:.6f} segundos}")
input("Presiona enter para ejecutar la consulta a.ii")

# a.ii Filtrar por un equipo cuyo nombre empieza con "Manchester"
query_aii = {"Squad": {"$regex": "^Manchester", "$options": "i"}}
time_aii, result_aii = measure_query_time(query_aii)
print("Resultado: \n" + str(result_aii))
print(f"Consulta a.ii ejecutada en {time_aii:.6f} segundos")
input("Presiona enter para ejecutar la consulta a.ii")

# b Consulta por un país específico (por ejemplo, España)
query_b = {"Nation": "es ESP"}
time_b, result_b = measure_query_time(query_b)
print("Resultado: \n" + str(result_b))
print(f"Consulta b ejecutada en {time_b:.6f} segundos")
