import json
from pathlib import Path

file_path = 'data.json'

def save_file(students):
    with open(file_path, 'w') as f:  
        json.dump(students, f)

def read_file():
    if Path(file_path).exists() and Path(file_path).is_file():
        with open(file_path, 'r') as f:
            students1 = json.load(f)
            return students1
        
    return []