# Enem 2021, 1º dia, caderno azul: Linguagens com Inglês (questões 1–5 de Inglês; 6–45 comuns). Conteúdo em ../enem_2021_linguagens_comum.py.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
import enem_2021_linguagens_comum as C

ID = "enem-2021-linguagens-ingles"
META = {"id": ID, "banca": "Enem", "ano": 2021, "titulo": "Enem 2021: Linguagens (Inglês)", "fonte": "Inep", "dataExame": "2021-11-21",
        "duracaoMinutos": 150, "area": "Linguagens (Inglês)", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
Q = C.montar("ingles")
completar(Q, R)
