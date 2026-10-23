import os
import json
from src import grava_csv, ler_json, list_to_text, move_file

# variavel global 
# camada bronze
__RAWPENDINGPATH__ = 'data/01_bronze/01_pending'
__RAWPROCESSEDPATH__ = 'data/01_bronze/02_processed'

# camada silver
__SILVERPATH__ = 'data/02_silver'

for filename in os.listdir(__RAWPENDINGPATH__):

    localpath = f'{__RAWPENDINGPATH__}/{filename}'
    source = f'{__RAWPENDINGPATH__}/{filename}'
    destination = f'{__RAWPROCESSEDPATH__}/{filename}'

    data = ler_json(localpath)
    concurso = data.get('numero')
    dezenas = list_to_text(data.get('listaDezenas'),';')
    cabecalho = f'concurso;d1;d2;d3;d4;d5;d6\n'
    linha = f'{cabecalho}{concurso},{dezenas}'
    grava_csv(f'{__SILVERPATH__}/concurso_{concurso}.csv',linha)
    move_file(source, destination)
