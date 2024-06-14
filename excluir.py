from salvar import salvararquivo
from bebidas import bebidas
import io

def nomevariavel(var):
    for name, value in globals().items():
        if value is var:
            return name


def excluir(dicionario, nome_arquivo):
        for i, item in enumerate(dicionario):
            print(f"{i}. {item['nome']} - R${item['valor']}")
        print("digite o indice do produto que deseja excluir: ")
        indice = int(input())
        if indice < 0 or indice >= len(dicionario):
            print("Índice inválido!")
            return
        del dicionario[indice]
        print("Produto excluído com sucesso!")
        print("Produtos disponíveis:")
        for i, item in enumerate(dicionario):
            print(f"{i}. {item['nome']} - R${item['valor']}")
        print("deseja excluir mais algum produto? (s/n)")
        opcao = input()
        if opcao == "s":
            excluir(dicionario)
        else:
            salvararquivo(dicionario, nome_arquivo + ".json")
            return