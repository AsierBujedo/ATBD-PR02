import os
import pandas as pd
import logging as logger
from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Initialize logger
log = logger.getLogger("pr02")
logger.basicConfig(filename='pr02.log', level=logger.INFO)

# Load environment variables
load_dotenv() 
SERVER = os.getenv("SERVER")
PORT = os.getenv("PORT")
UNAME = quote_plus(os.getenv("USERNAME"))
UPASS = quote_plus(os.getenv("PASSWORD"))

# Transform data grouping by stats and other stats
def transform_row(row):
    return {
        "Player": row["Player"],
        "Nation": row["Nation"],
        "Position": row["Pos"].split(",") if pd.notnull(row["Pos"]) else [],
        "Squad": row["Squad"],
        "Age": int(row["Age"].split("-")[0]) if pd.notnull(row["Age"]) else None,
        "Born": int(row["Born"]) if pd.notnull(row["Born"]) else None,
        "EstimatedStartYear": int(row["Estimated_Start_Year"]) if pd.notnull(row["Estimated_Start_Year"]) else None,
        "Stats": {
            "MatchesPlayed": row["MP"] if pd.notnull(row["MP"]) else 0,
            "Starts": row["Starts"] if pd.notnull(row["Starts"]) else 0,
            "MinutesPlayed": row["Min"] if pd.notnull(row["Min"]) else 0,
            "Goals": row["Gls"] if pd.notnull(row["Gls"]) else 0,
            "Assists": row["Ast"] if pd.notnull(row["Ast"]) else 0,
            "TacklesWon": row["TklW"] if pd.notnull(row["TklW"]) else 0,
            "AerialDuels": {
                "Won": row["AerialDuels_Won"] if pd.notnull(row["AerialDuels_Won"]) else 0,
                "Lost": row["AerialDuels_Lost"] if pd.notnull(row["AerialDuels_Lost"]) else 0
            }
        },
        "OtherStats": {
            "Crosses": row["Crs"] if pd.notnull(row["Crs"]) else 0,
            "Recoveries": row["Recov"] if pd.notnull(row["Recov"]) else 0,
            "OwnGoals": row["OG"] if pd.notnull(row["OG"]) else 0
        }
}

# Import and load data into pandas
csv_file = './data/all_players.csv'
data = pd.read_csv(csv_file)
data_subset = data.head(100)
documents = [transform_row(row) for _, row in data_subset.iterrows()]

try:
    client = MongoClient(f'mongodb://{UNAME}:{UPASS}@{SERVER}:{PORT}/') # Connects to mongo
    db = client['football']
    collection = db['players']

    collection.drop() # Drops the collection to avoid redundance
    log.info(f"Collection {collection.name} dropped")
    result = collection.insert_many(documents) # Inserts 100 registers
    log.info(f"Inserted {len(result.inserted_ids)} register(s) to mongo")
except Exception as e:
    log.error("Could not connect to mongo: " + str(e))

