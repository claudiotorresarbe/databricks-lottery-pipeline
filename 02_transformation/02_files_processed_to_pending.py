import os
from src import move_file

# variavel global 
# camada bronze
__RAWPENDINGPATH__ = 'data/01_bronze/01_pending'
__RAWPROCESSEDPATH__ = 'data/01_bronze/02_processed'

for filename in os.listdir(__RAWPROCESSEDPATH__):
    source = f'{__RAWPROCESSEDPATH__}/{filename}'
    destination = f'{__RAWPENDINGPATH__}/{filename}'
    move_file(source,destination)