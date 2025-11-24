"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    
from pathlib import Path
import pandas as pd

def pregunta_01():
    repo_root = Path(__file__).resolve().parents[1]   # sube desde homework/ a la raíz
    path = repo_root / "files" / "input" / "tbl0.tsv"
    tbl0 = pd.read_csv(path, sep="\t")
    return len(tbl0)

print(pregunta_01())