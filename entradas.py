import json
entradas = []
with open('entradas.json', encoding='utf-8') as file:
    for line in file:
        entradas.append(json.loads(line))