import pandas as pd
import os

def test_archivos():
    # Verifica si el dataset existe
    assert os.path.exists("dataset.csv"), "❌ Error: dataset.csv no encontrado"
    print("✅ Archivo dataset.csv: Encontrado")

    # Verifica si pandas puede leerlo
    df = pd.read_csv("dataset.csv")
    assert not df.empty, "❌ Error: El dataset está vacío"
    print("✅ Lectura de datos: OK")

if __name__ == "__main__":
    test_archivos()