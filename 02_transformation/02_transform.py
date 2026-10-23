import os
import json
from src import ler_json, list_to_text, move_file

__RAWPATH__ = 'data/raw'
__PROCESSEDPATH__ = 'data/processed'

for filename in os.listdir(__RAWPATH__):
    data = ler_json(f'{__RAWPATH__}/{filename}')
    concurso = data.get('numero')
    dezenas = list_to_text(data.get('listaDezenas'))
    print(f'{concurso},{dezenas}')
    # falta processar os dados no databricks
    move_file(f'{__RAWPATH__}/{filename}', f'{__PROCESSEDPATH__}/{filename}')
    break