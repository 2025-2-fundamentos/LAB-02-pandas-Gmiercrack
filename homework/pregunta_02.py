"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """

    from pathlib import Path
    import pandas as pd

    repo_root = Path(__file__).resolve().parents[1]   # sube desde homework/ a la raíz
    path = repo_root / "files" / "input" / "tbl0.tsv"
    tbl0 = pd.read_csv(path, sep="\t")
    return len(tbl0.columns)

if __name__ == "__main__":
    print(pregunta_02())