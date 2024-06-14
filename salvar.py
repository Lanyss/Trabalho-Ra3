import json
def salvararquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for item in lista:
            json.dump(item, arquivo, ensure_ascii=False)
            arquivo.write('\n')

def carregararquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        lista = json.loads(conteudo.replace("'", "\"")) 
        for item in lista:
            print(item)