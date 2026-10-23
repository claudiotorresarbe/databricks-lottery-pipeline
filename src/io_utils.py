import os
import json
import shutil

def file_exists(filename):
    if os.path.exists(filename):
        return 1
    else:
        return 0

def grava_csv(filename,row):
    with open(filename,'a+') as f:
        f.write(row) 

def gravar_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def ler_json(filename):
    with open(filename, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return dados

def list_to_text(data,caracter=';'):
    return f'{caracter}'.join([x for x in data])

def move_file(source,destination):
    shutil.move(source,destination)

def delete_file(source):
    os.remove(source)