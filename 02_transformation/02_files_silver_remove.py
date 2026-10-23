import os
from src import delete_file

# variavel global 
# camada bronze
__SILVERPATH__ = 'data/02_silver'

for filename in os.listdir(__SILVERPATH__):
    source = f'{__SILVERPATH__}/{filename}'
    delete_file(source)