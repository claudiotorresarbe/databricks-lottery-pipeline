import time
from src import gravar_json, file_exists
from loteria_caixa import *

concurso_atual = MegaSena().numero()

for concurso in range(1,concurso_atual+1):

    tudo = MegaSena(concurso).todosDados()

    file = f'data/01_bronze/01_pending/concurso_{concurso}.json'

    if not file_exists(file):
        
        gravar_json(file,tudo)

    time.sleep(0.05)