"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():
    file_path = 'clusters_report.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    data = []
    current_cluster = {}
    keywords = []

    for line in lines:
        clean_line = line.strip()
        match = re.match(r'^\s*(\d+)\s+(\d+)\s+([\d,]+)\s+%', clean_line)
        if match:
            if current_cluster:
                current_cluster['principales_palabras_clave'] = ', '.join(keywords)
                data.append(current_cluster)
                keywords = []

            current_cluster = {
                'cluster': int(match.group(1)),
                'cantidad_de_palabras_clave': int(match.group(2)),
                'porcentaje_de_palabras_clave': float(match.group(3).replace(',', '.'))
            }
        
        elif clean_line:
            keywords.extend([word.strip() for word in clean_line.split(',')])

    if current_cluster:
        current_cluster['principales_palabras_clave'] = ', '.join(keywords)
        data.append(current_cluster)

    df = pd.DataFrame(data)

    df.columns = [col.replace(' ', '_').lower() for col in df.columns]
    return df