# Enem 2020, 1º dia, caderno azul: Linguagens com Espanhol (questões 1–5 de Espanhol; 6–45 comuns). Conteúdo em ../enem_2020_linguagens_comum.py.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
import enem_2020_linguagens_comum as C

ID = "enem-2020-linguagens-espanhol"
META = {"id": ID, "banca": "Enem", "ano": 2020, "titulo": "Enem 2020: Linguagens (Espanhol)", "fonte": "Inep", "dataExame": "2021-01-17",
        "duracaoMinutos": 150, "area": "Linguagens (Espanhol)", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
Q = C.montar("espanhol")
completar(Q, R)
