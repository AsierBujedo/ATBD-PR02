import os
import time
from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv
import logging as log

load_dotenv()
SERVER = os.getenv("SERVER")
PORT = os.getenv("PORT")
UNAME = quote_plus(os.getenv("USR"))
UPASS = quote_plus(os.getenv("PWD"))

try:
    client = MongoClient(f'mongodb://{UNAME}:{UPASS}@{SERVER}:{PORT}/')
    db = client['football']
    collection = db['players']

    # UPDATE PLAYER Teresa Abilleira

    name1 = "Teresa Abilleira"
    start_time = time.time()
    collection.update_one(
        {"Player": name1},
        {"$set": {"Player": name1.upper()}}
    )
    end_time = time.time()
    execution_time1 = end_time - start_time
    print(f"Actualización de {name1} ejecutada en {execution_time1:.6f} segundos.")
    input("Presiona enter para ejecutar la segunda modificación")

    # UPDATE PLAYER Jessica Aby

    name2 = "Jessica Aby"
    start_time = time.time()
    collection.update_one(
        {"Player": name2},
        {"$set": {"Player": name2.upper()}}
    )
    end_time = time.time()
    execution_time2 = end_time - start_time
    print(f"Actualización de {name2} ejecutada en {execution_time2:.6f} segundos.")

except Exception as e:
    log.error("Could not modify registries: " + str(e))
    print("Error durante las actualizaciones:", str(e))

