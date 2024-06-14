def alterar ():
    ind = int(input('selecione qual item modificar: '))

    opcao = str(input('deseja alterar o nome(n) ou o valor(v)? '))
    if opcao == 'n':
        item_novo = str(input('digite o novo nome: '))
        itens[ind] = item_novo
    elif opcao == 'v':
        valor_novo = float(input('digite o novo valor: '))
        valor[ind] = valor_novo
    else:
        print('digite uma opção válida')
    print('valor alterado')