import json
import shutil

def gravar_json(filename, data):
    
    with open(filename, 'w', encoding='utf-8') as f:
        
        json.dump(data, f, indent=4, ensure_ascii=False)

def ler_json(filename):
    with open(filename,'r') as f:
        file = json.loads(f.read())
        return file

def list_to_text(data):
    return ','.join([x for x in data])

def move_file(source,destination):
    shutil.move(source,destination)