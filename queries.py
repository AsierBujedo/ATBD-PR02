import time, os, json
from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
SERVER = os.getenv("SERVER")
PORT = os.getenv("PORT")
UNAME = quote_plus(os.getenv("USR"))
UPASS = quote_plus(os.getenv("PWD"))

# Conectar a MongoDB
client = MongoClient(f'mongodb://{UNAME}:{UPASS}@{SERVER}:{PORT}/')
db = client['football']
collection = db['players']

# Función para medir el tiempo de ejecución de una consulta
def measure_query_time(collection, query):
    start_time = time.time()
    result = list(collection.find(query)) 
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, result

# Función para ejecutar y almacenar los resultados de una consulta
def execute_and_store_results(query_name, collection, query):
    elapsed_time, result = measure_query_time(collection, query)
    print(f"Resultado {query_name}:")
    for doc in result:
        print(doc)
    print(f"Consulta {query_name} ejecutada en {elapsed_time:.6f} segundos")
    return {
        "query_name": query_name,
        "execution_time": elapsed_time,
        "results": result
    }

# Ejecutar consultas y almacenar resultados
results_data = []

# Consulta a.i
query_ai = {"PersonalInfo.EstimatedStartYear": {"$gt": 2020}}
result_ai = execute_and_store_results("a.i", collection, query_ai)
results_data.append(result_ai)
input("Presiona enter para ejecutar la consulta a.ii")

# Consulta a.ii
query_aii = {"PersonalInfo.SquadInfo.Squad": {"$regex": "^Manchester", "$options": "i"}}
result_aii = execute_and_store_results("a.ii", collection, query_aii)
results_data.append(result_aii)
input("Presiona enter para ejecutar la consulta b")

# Consulta b
query_b = {"PersonalInfo.Nation": "es ESP"}
result_b = execute_and_store_results("b", collection, query_b)
results_data.append(result_b)

# Guardar resultados de cada consulta en archivos JSON separados
for result in results_data:
    query_name = result["query_name"]
    output_file = f"results/query_results_{query_name}.json"
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(result, json_file, default=str, indent=4)
    print(f"Resultados de la consulta {query_name} guardados en {output_file}")