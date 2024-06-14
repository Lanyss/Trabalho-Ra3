import json
from salvar import salvararquivo
def nomevariavel(var): # retorna o nome da variável
    for name, value in globals().items(): # percorre as variáveis globais
        if value is var: # se o valor for igual à variável
            return name # retorna o nome da variável

def alterar(dicionario, nome_arquivo): # altera um produto
    while True: # loop infinito
        for i, item in enumerate(dicionario): # lista o dicionário
            print(f"{i}. {item['nome']} - R${item['valor']}") # imprime o nome e o valor do produto
        print("Digite o índice do produto que deseja alterar: ") # solicita o índice do produto
        indice = int(input()) # recebe o índice do produto
        if indice < 0 or indice >= len(dicionario): # se o índice for inválido
            print("Índice inválido!") # imprime a mensagem
            continue # volta ao início do loop
        print("Deseja alterar o nome ou o valor?") # solicita a opção de alteração
        opcao = input("Digite 'nome' ou 'valor': ").strip().lower() # recebe a opção de alteração em minúsculo e sem espaços no início e no fim da string
        if opcao == "nome": # se a opção for 'nome'
            print("Digite o novo nome: ") # solicita o novo nome
            novo_valor = input().strip() # recebe o novo nome
            dicionario[indice]["nome"] = novo_valor # altera o nome do produto no dicionário
        elif opcao == "valor":  # se a opção for 'valor' 
            print("Digite o novo valor: ") # solicita o novo valor 
            novo_valor = input().strip() # recebe o novo valor 
            dicionario[indice]["valor"] = novo_valor # altera o valor do produto no dicionário 
        else: # se a opção não for 'nome' nem 'valor'
            print("Opção inválida!") # imprime a mensagem
            continue
        
        for i, item in enumerate(dicionario): # lista o dicionário
            print(f"{i}. {item['nome']} - R${item['valor']}") # imprime o nome e o valor do produto
        print("Deseja alterar mais algum produto? (s/n)") # solicita a opção de alterar mais um produto
        opcao = input().strip().lower() # recebe a opção de alterar mais um produto em minúsculo e sem espaços no início e no fim da string
        if opcao != "s": # se a opção não for 's'
            salvararquivo(dicionario, nome_arquivo + ".json") # salva o arquivo
            break
