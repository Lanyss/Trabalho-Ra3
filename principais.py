import json
principais = []
with open('principais.json', encoding='utf-8') as file:
    for line in file:
        principais.append(json.loads(line))