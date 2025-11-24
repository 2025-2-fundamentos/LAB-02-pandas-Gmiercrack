"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """

    from pathlib import Path
    import pandas as pd

    repo_root = Path(__file__).resolve().parents[1]   # sube desde homework/ a la raíz
    path = repo_root / "files" / "input" / "tbl1.tsv"
    tbl1 = pd.read_csv(path, sep="\t")
    return sorted(tbl1["c4"].str.upper().unique().tolist())

if __name__ == "__main__":
    print(pregunta_06())