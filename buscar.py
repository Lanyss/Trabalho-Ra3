from salvar import salvararquivo
import io

def nomevariavel(var):
    for name, value in globals().items():
        if value is var:
            return name


def buscar(dicionario):
    print("deseja buscar o nome ou o valor?")
    opcao = input("Digite 'nome' ou 'valor': ")
    if opcao == "nome":
        print("Digite o nome: ")
        nome = input()
        produtos_encontrados = []
        for i, item in enumerate(dicionario):
            if str(nome) in item['nome']:
                produtos_encontrados.append(item)
        if produtos_encontrados:
            print("Produtos encontrados:")
            for produto in produtos_encontrados:
                print(f"{produto['nome']} - R${produto['valor']}")
        else:
            print("Nenhum produto encontrado com esse nome!")
    elif opcao == "valor":
        print("Digite o novo valor: ")
        valor = input()
        produtos_encontrados = []
        for i, item in enumerate(dicionario):
            if item['valor'] == float(valor):
                produtos_encontrados.append(item)
        if produtos_encontrados:
            print("Produtos encontrados:")
            for produto in produtos_encontrados:
                print(f"{produto['nome']} - R${produto['valor']}")
        else:
            print("Nenhum produto encontrado com esse valor!")
    else:
        print("Opção inválida!")
    print("deseja buscar mais algum produto? (s/n)")
    opcao = input()
    if opcao == "s":
        buscar(dicionario)
    else:
        return
    
