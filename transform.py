import pandas as pd
import numpy as np
from datetime import datetime

# Cargar el dataset desde un archivo CSV
file_path = './data/all_players.csv'  # Cambia esto por la ruta a tu archivo
dataset = pd.read_csv(file_path)

# Extraer el año de nacimiento del campo 'Born'
dataset['Year_Born'] = pd.to_numeric(dataset['Born'], errors='coerce')

# Año actual
current_year = datetime.now().year

# Función para calcular el año de inicio estimado con aleatoriedad controlada
def calculate_start_year(row):
    if row['Starts'] > 0:
        # Si hay titularidades, generar un inicio aleatorio entre el año actual - 6 y actual - 2
        return np.random.randint(current_year - 6, current_year - 2)
    elif not pd.isna(row['Year_Born']):
        # Si no hay titularidades, asumir 18 años tras el nacimiento +/- 2 años
        return int(row['Year_Born'] + 18 + np.random.randint(-2, 3))
    else:
        # Si faltan datos, dejar el valor como NaN
        return None

# Aplicar la función al dataset
dataset['Estimated_Start_Year'] = dataset.apply(calculate_start_year, axis=1)

# Eliminar columnas redundantes
columns_to_drop = ['Year_Born']  # Se eliminan las columnas relacionadas
cleaned_dataset = dataset.drop(columns=columns_to_drop)

# Guardar el resultado en un nuevo archivo CSV
output_file = 'dataset.csv'
cleaned_dataset.to_csv("./data/" + output_file, index=False)

print(f"El archivo procesado se ha guardado en: {output_file}")
