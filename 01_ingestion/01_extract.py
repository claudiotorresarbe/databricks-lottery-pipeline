import time
from src import gravar_json
from loteria_caixa import *

concurso_atual = MegaSena().numero()

for concurso in range(1,concurso_atual+1):
    tudo = MegaSena(concurso).todosDados()
    gravar_json(fr'data\\raw\\concurso_{concurso}.json',tudo)
    time.sleep(0.05)