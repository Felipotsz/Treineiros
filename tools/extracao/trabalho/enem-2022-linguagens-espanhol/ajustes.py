# Enem 2022, 1º dia, caderno azul: Linguagens com Espanhol (questões 1–5 de Espanhol; 6–45 comuns). Conteúdo em ../enem_2022_linguagens_comum.py.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from aj import completar
import enem_2022_linguagens_comum as C

ID = "enem-2022-linguagens-espanhol"
META = {"id": ID, "banca": "Enem", "ano": 2022, "titulo": "Enem 2022: Linguagens (Espanhol)", "fonte": "Inep", "dataExame": "2022-11-13",
        "duracaoMinutos": 150, "area": "Linguagens (Espanhol)", "caderno": "azul", "dia": 1}
R = {n: {"numero": n, "enunciado": "", "alternativas": {}} for n in range(1, 46)}
Q = C.montar("espanhol")
completar(Q, R)
