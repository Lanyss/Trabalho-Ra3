import json
bebidas = []
with open('bebidas.json', encoding='utf-8') as file:
    for line in file:
        bebidas.append(json.loads(line))