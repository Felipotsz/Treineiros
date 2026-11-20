# Enem 2014, 2º dia, caderno azul: Linguagens com Espanhol (questões 1–5 de Espanhol; 6–45 comuns). Conteúdo em ../enem_2014_linguagens_comum.py.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
import enem_2014_linguagens_comum as C

ID = "enem-2014-linguagens-espanhol"
META = {"id": ID, "banca": "Enem", "ano": 2014, "titulo": "Enem 2014: Linguagens (Espanhol)", "fonte": "Inep", "dataExame": "2014-11-09",
        "duracaoMinutos": 150, "area": "Linguagens (Espanhol)", "caderno": "azul", "dia": 2}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
Q = C.montar("espanhol")
completar(Q, R)
