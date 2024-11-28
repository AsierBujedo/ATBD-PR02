import os
import pandas as pd
import logging as logger
from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv

log = logger.getLogger("pr02")
logger.basicConfig(filename='pr02.log', level=logger.INFO)

load_dotenv()
SERVER = os.getenv("SERVER")
PORT = os.getenv("PORT")
UNAME = quote_plus(os.getenv("USER"))
UPASS = quote_plus(os.getenv("PASSWORD"))

def transform_row(row):
    aerial_duels_won = row["AerialDuels_Won"] if pd.notnull(row["AerialDuels_Won"]) else 0
    aerial_duels_lost = row["AerialDuels_Lost"] if pd.notnull(row["AerialDuels_Lost"]) else 0
    aerial_duels_total = aerial_duels_won + aerial_duels_lost
    aerial_duels_success_rate = (aerial_duels_won / aerial_duels_total) * 100 if aerial_duels_total > 0 else 0

    minutes_played = row["Min"] if pd.notnull(row["Min"]) else 0
    matches_played = row["MP"] if pd.notnull(row["MP"]) else 0
    max_minutes_possible = matches_played * 90
    minutes_played_ratio = (minutes_played / max_minutes_possible) * 100 if max_minutes_possible > 0 else 0

    assists = row.get("Ast", 0) if pd.notnull(row.get("Ast", None)) else 0
    assist_per_match = (assists / matches_played) if matches_played > 0 else 0

    return {
        "Player": row["Player"],
        "PersonalInfo": {
            "Nation": row["Nation"],
            "Position": row["Pos"].split(",") if pd.notnull(row["Pos"]) else [],
            "Squad": row["Squad"],
            "SquadID": row["Squad_id"],
            "PlayerID": row["Player_id"],
            "Age": int(row["Age"].split("-")[0]) if pd.notnull(row["Age"]) else None,
            "Born": int(row["Born"]) if pd.notnull(row["Born"]) else None,
            "EstimatedStartYear": int(row["Estimated_Start_Year"]) if pd.notnull(row["Estimated_Start_Year"]) else None,
        },
        "PerformanceStats": {
            "MatchesPlayed": matches_played,
            "Starts": row["Starts"] if pd.notnull(row["Starts"]) else 0,
            "MinutesPlayed": minutes_played,
            "Goals": row["Gls"] if pd.notnull(row["Gls"]) else 0,
            "NonPenaltyGoals": row["G-PK"] if pd.notnull(row["G-PK"]) else 0,
            "PenaltiesScored": row["PK"] if pd.notnull(row["PK"]) else 0,
            "PenaltiesAttempted": row["PKatt"] if pd.notnull(row["PKatt"]) else 0,
            "Assists": assists,
            "AssistPerMatch": round(assist_per_match, 2),
            "SubstituteAppearances": row["Subs"] if pd.notnull(row["Subs"]) else 0,
        },
        "DefensiveStats": {
            "TacklesWon": row["TklW"] if pd.notnull(row["TklW"]) else 0,
            "Recoveries": row["Recov"] if pd.notnull(row["Recov"]) else 0,
            "AerialDuels": {
                "Won": aerial_duels_won,
                "Lost": aerial_duels_lost,
                "SuccessRate": round(aerial_duels_success_rate, 2),
            },
        },
        "DisciplinaryStats": {
            "YellowCards": row["CrdY"] if pd.notnull(row["CrdY"]) else 0,
            "SecondYellowCards": row["2CrdY"] if pd.notnull(row["2CrdY"]) else 0,
            "RedCards": row["CrdR"] if pd.notnull(row["CrdR"]) else 0,
        },
        "SpecialEvents": {
            "Crosses": row["Crs"] if pd.notnull(row["Crs"]) else 0,
            "OwnGoals": row["OG"] if pd.notnull(row["OG"]) else 0,
            "Penalties": {
                "Won": row["PKwon"] if pd.notnull(row["PKwon"]) else 0,
                "Conceded": row["PKcon"] if pd.notnull(row["PKcon"]) else 0,
            },
        },
        "AdvancedStats": {
            "MinutesPlayedRatio": round(minutes_played_ratio, 2),
        },
    }

csv_file = './data/dataset.csv'
data = pd.read_csv(csv_file)
data_subset = data.head(100)
documents = [transform_row(row) for _, row in data_subset.iterrows()]

try:
    client = MongoClient(f'mongodb://root:{UPASS}@{SERVER}:{PORT}/') # Connects to mongo
    db = client['football']
    collection = db['players']

    collection.create_index("PersonalInfo.EstimatedStartYear")
    collection.create_index("PersonalInfo.Player")
    collection.create_index("PersonalInfo.Squad")
    collection.create_index("PersonalInfo.Nation") 

    collection.drop()
    log.info(f"Collection {collection.name} dropped")
    result = collection.insert_many(documents) 
    log.info(f"Inserted {len(result.inserted_ids)} record(s) to mongo")

    # Inserts a player from Manchester City
    manchester_players = data[data['Squad'].str.contains('Manchester', na=False, case=False)]
    if not manchester_players.empty:
        first_manchester_player_row = manchester_players.iloc[0]
        first_manchester_player = transform_row(first_manchester_player_row.to_dict())
        collection.insert_one(first_manchester_player)
        log.info(f"Inserted player {first_manchester_player['PersonalInfo']['Player']} from Manchester.")
    else:
        log.info("No players found with Squad containing 'Manchester'.")

except Exception as e:
    log.error("Could not connect to mongo: " + str(e))
