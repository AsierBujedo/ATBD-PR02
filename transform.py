import pandas as pd
import numpy as np
from datetime import datetime

file_path = './data/all_players.csv'
dataset = pd.read_csv(file_path)

dataset['Year_Born'] = pd.to_numeric(dataset['Born'], errors='coerce')

current_year = datetime.now().year

def calculate_start_year(row):
    if row['Starts'] > 0:
        return np.random.randint(current_year - 6, current_year - 2)
    elif not pd.isna(row['Year_Born']):
        return int(row['Year_Born'] + 18 + np.random.randint(-2, 3))
    else:
        return None

dataset['Estimated_Start_Year'] = dataset.apply(calculate_start_year, axis=1)

columns_to_drop = ['Year_Born']
cleaned_dataset = dataset.drop(columns=columns_to_drop)

output_file = 'dataset.csv'
cleaned_dataset.to_csv("./data/" + output_file, index=False)
