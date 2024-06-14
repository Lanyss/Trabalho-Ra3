from salvar import salvararquivo
from bebidas import bebidas
import io

def nomevariavel(var):
    for name, value in globals().items():
        if value is var:
            return name
## adiciona um produto ao dicionário
def adicionar(dicionario, nome_arquivo):
        for i, item in enumerate(dicionario): # lista o dicionário
            print(f"{i}. {item['nome']} - R${item['valor']}") # imprime o nome e o valor do produto
        print("digite o nome do novo produto: ") # solicita o nome do novo produto
        nome = input() # recebe o nome do novo produto
        print("digite o valor do novo produto: ") # solicita o valor do novo produto
        valor = float(input()) # recebe o valor do novo produto
        dicionario.append({"nome": nome, "valor": valor}) # adiciona o novo produto ao dicionário
        print("Produto adicionado com sucesso!") 
        print("Produtos disponíveis:")
        for i, item in enumerate(dicionario): # lista o dicionário
            print(f"{i}. {item['nome']} - R${item['valor']}") # imprime o nome e o valor do produto 
        print("deseja adicionar mais algum produto? (s/n)") 
        opcao = input() # solicita a opção de adicionar mais um produto
        if opcao == "s": # se a opção for 's'
            adicionar(dicionario)   # chama a função adicionar
        else: # se a opção não for 's'
            salvararquivo(dicionario, nome_arquivo + ".json") # salva o arquivo
            return