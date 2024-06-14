import json # importa a biblioteca json
sobremesas = [] # cria uma lista vazia  
with open('sobremesas.json', encoding='utf-8') as file: # abre o arquivo com encoding utf-8 para aceitar acentos
    for line in file: # percorre as linhas do arquivo
        sobremesas.append(json.loads(line)) # adiciona o conteúdo da linha à lista de sobremesas 