# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


import os
import zipfile
import glob
import pandas as pd


def pregunta_01():
    """
    La información requerida para este laboratorio está almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.
    ...
    Genera "train_dataset.csv" y "test_dataset.csv" en la carpeta "files/output/".
    """
    # 1. Descomprimir el archivo zip en la raíz
    zip_path = "files/input.zip"
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(".")

    # Asegurar que la carpeta correcta 'files/output' exista
    os.makedirs("files/output", exist_ok=True)

    # Definir los conjuntos de datos que vamos a procesar
    datasets = ["train", "test"]

    for dataset in datasets:
        phrases = []
        sentiments = []

        # Buscamos todos los archivos .txt dentro de input/train o input/test
        pattern = os.path.join("input", dataset, "*", "*.txt")
        file_paths = glob.glob(pattern)

        for file_path in file_paths:
            # Extraemos el sentimiento del nombre de la carpeta padre
            sentiment = os.path.basename(os.path.dirname(file_path))
            
            # Leer el contenido de la frase
            with open(file_path, "r", encoding="utf-8") as f:
                phrase = f.read().strip()
            
            phrases.append(phrase)
            sentiments.append(sentiment)

        # Crear el dataframe con las columnas requeridas
        df = pd.DataFrame({
            "phrase": phrases,
            "target": sentiments
        })

        # Guardar en la ruta exacta esperada por el test
        output_path = f"files/output/{dataset}_dataset.csv"
        df.to_csv(output_path, index=False)