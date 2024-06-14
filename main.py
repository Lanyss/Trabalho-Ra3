import os
import sys
from bebidas import bebidas as Bebidas
from entradas import entradas as Entradas
from principais import principais as principais
from sobremesas import sobremesas as Sobremesas
from adicionar import adicionar
from excluir import excluir
from alterar import alterar
from buscar import buscar
def espaçamento(x):
    return " " * x

def menu_principal():
    menu_principal = ['Bebidas','Entradas','Pratos Principais','Sobremesas']
    sair = ['Sair']

    tamls = len(menu_principal)

    ind = 0
    con = 0

    tamanho = [len(word) for word in menu_principal]

    print("_____________________________| Principal |_____________________________")
    while con < tamls:
    
        print(f'|\t\t\t\t{con} - {menu_principal[ind]}{espaçamento(35 - tamanho[con])}|')
        con += 1
        ind += 1
    print(f"|\t\t\t\t{con} - {sair[0] + espaçamento(35 - len(sair[0]))}|")
    print("|______________________________________________________________________|")
    opcao = int(input("Escolha uma opção: "))
    if opcao == menu_principal.index('Bebidas'):
        MenuBebidas()
    elif opcao == menu_principal.index('Entradas'):
        MenuEntradas()
    elif opcao == menu_principal.index('Pratos Principais'):
        MenuPrincipais()
    elif opcao == menu_principal.index('Sobremesas'):
        MenuSobremesas()
    elif opcao == tamls:
        print("Saindo do programa...")
        exit()
    elif opcao > tamls:
        print("Opção inválida, tente novamente...")
        menu_principal()



def MenuBebidas():
    nome_arquivo = 'bebidas'
    menu_bebidas = Bebidas
    Voltar = ['Voltar']
    Alterar = ['Alterar']
    Adicionar = ['Adicionar']
    Excluir = ['Excluir']
    Buscar = ['Buscar']
    tamls = len(menu_bebidas)

    ind = 0
    con = 0

    tamanho = [len(str(item["nome"])) for item in menu_bebidas]
    tamanho_valor = [len(str(item["valor"])) for item in menu_bebidas]
    tamanho_con = [len(str(con)) for con in range(tamls)]

    print("______________________________| BEBIDAS |______________________________")
    while con < tamls:
    
        print(f'|\t\t\t\t{con} - {(menu_bebidas)[ind]["nome"]} - R${str((menu_bebidas)[ind]["valor"])}{espaçamento(31 - tamanho[con] - tamanho_valor[con] - tamanho_con[con])}|')
        con += 1
        ind += 1
    print(f"|\t\t\t\t{con} - {Adicionar[0] + espaçamento(31 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+1} - {Alterar[0] + espaçamento(33 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+2} - {Excluir[0] + espaçamento(33 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+3} - {Buscar[0] + espaçamento(33 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+4} - {Voltar[0] + espaçamento(34 - len(Voltar[0]))}|")
    print("|______________________________________________________________________|")
    opcao = int(input("Escolha uma opção: "))
    if opcao == con:
        print("Adcionando bebidas...")
        adicionar(menu_bebidas, nome_arquivo)
    elif opcao == con+1:
        print("Alterando bebidas...")
        alterar(menu_bebidas, nome_arquivo)
    elif opcao == con+2:
        print("Excluindo bebidas...")
        excluir(menu_bebidas, nome_arquivo)
    elif opcao == con+3:
        print("Buscando itens...")
        buscar(menu_bebidas)
    elif opcao == con+4:
        print("Voltando ao menu principal...")
        menu_principal()

def MenuEntradas():
    nome_arquivo = 'entradas'
    menu_entradas = Entradas
    Voltar = ['Voltar']
    Alterar = ['Alterar']
    Adicionar = ['Adicionar']
    Excluir = ['Excluir']
    Buscar = ['Buscar']
    tamls = len(menu_entradas)

    ind = 0
    con = 0

    tamanho = [len(str(item["nome"])) for item in menu_entradas]
    tamanho_valor = [len(str(item["valor"])) for item in menu_entradas]
    tamanho_con = [len(str(con)) for con in range(tamls)]

    print("______________________________| Entradas |______________________________")
    while con < tamls:
    
        print(f'|\t\t\t\t{con} - {(menu_entradas)[ind]["nome"]} - R${str((menu_entradas)[ind]["valor"])}{espaçamento(31 - tamanho[con] - tamanho_valor[con] - tamanho_con[con])}|')
        con += 1
        ind += 1
    print(f"|\t\t\t\t{con} - {Adicionar[0] + espaçamento(31 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+1} - {Alterar[0] + espaçamento(33 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+2} - {Excluir[0] + espaçamento(33 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+3} - {Buscar[0] + espaçamento(33 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+4} - {Voltar[0] + espaçamento(34 - len(Voltar[0]))}|")
    print("|______________________________________________________________________|")
    opcao = int(input("Escolha uma opção: "))
    if opcao == con:
        print("Adcionando entradas...")
        adicionar(menu_entradas, nome_arquivo)
    elif opcao == con+1:
        print("Alterando entradas...")
        alterar(menu_entradas, nome_arquivo)
    elif opcao == con+2:
        print("Excluindo entradas...")
        excluir(menu_entradas, nome_arquivo)
    elif opcao == con+3:
        print("Buscando itens...")
        buscar(menu_entradas)
    elif opcao == con+4:
        print("Voltando ao menu principal...")
        menu_principal()


def MenuPrincipais():
    nome_arquivo = 'principais'
    menu_principais = principais
    Voltar = ['Voltar']
    Alterar = ['Alterar']
    Adicionar = ['Adicionar']
    Excluir = ['Excluir']
    Buscar = ['Buscar']
    tamls = len(menu_principais)

    ind = 0
    con = 0

    tamanho = [len(str(item["nome"])) for item in menu_principais]
    tamanho_valor = [len(str(item["valor"])) for item in menu_principais]
    tamanho_con = [len(str(con)) for con in range(tamls)]

    print("______________________________| Pratos Principais |______________________________")
    while con < tamls:
    
        print(f'|\t\t\t\t{con} - {(menu_principais)[ind]["nome"]} - R${str((menu_principais)[ind]["valor"])}{espaçamento(31 - tamanho[con] - tamanho_valor[con] - tamanho_con[con])}|')
        con += 1
        ind += 1
    print(f"|\t\t\t\t{con} - {Adicionar[0] + espaçamento(31 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+1} - {Alterar[0] + espaçamento(33 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+2} - {Excluir[0] + espaçamento(33 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+3} - {Buscar[0] + espaçamento(33 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+4} - {Voltar[0] + espaçamento(34 - len(Voltar[0]))}|")
    print("|______________________________________________________________________|")
    opcao = int(input("Escolha uma opção: "))
    if opcao == con:
        print("Adcionando Pratos...")
        adicionar(menu_principais, nome_arquivo)
    elif opcao == con+1:
        print("Alterando Pratos...")
        alterar(menu_principais, nome_arquivo)
    elif opcao == con+2:
        print("Excluindo Pratos...")
        excluir(menu_principais, nome_arquivo)
    elif opcao == con+3:
        print("Buscando itens...")
        buscar(menu_principais)
    elif opcao == con+4:
        print("Voltando ao menu principal...")
        menu_principal()


def MenuSobremesas():
    nome_arquivo = 'sobremesas'
    menu_sobremesas = Sobremesas
    Voltar = ['Voltar']
    Alterar = ['Alterar']
    Adicionar = ['Adicionar']
    Excluir = ['Excluir']
    Buscar = ['Buscar']
    tamls = len(menu_sobremesas)

    ind = 0
    con = 0

    tamanho = [len(str(item["nome"])) for item in menu_sobremesas]
    tamanho_valor = [len(str(item["valor"])) for item in menu_sobremesas]
    tamanho_con = [len(str(con)) for con in range(tamls)]

    print("______________________________| Sobremesas |______________________________")
    while con < tamls:
    
        print(f'|\t\t\t\t{con} - {(menu_sobremesas)[ind]["nome"]} - R${str((menu_sobremesas)[ind]["valor"])}{espaçamento(31 - tamanho[con] - tamanho_valor[con] - tamanho_con[con])}|')
        con += 1
        ind += 1
    print(f"|\t\t\t\t{con} - {Adicionar[0] + espaçamento(31 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+1} - {Alterar[0] + espaçamento(33 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+2} - {Excluir[0] + espaçamento(33 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+3} - {Buscar[0] + espaçamento(33 - len(Voltar[0]))}|")
    print(f"|\t\t\t\t{con+4} - {Voltar[0] + espaçamento(34 - len(Voltar[0]))}|")
    print("|______________________________________________________________________|")
    opcao = int(input("Escolha uma opção: "))
    if opcao == con:
        print("Adcionando Sobremesas...")
        adicionar(menu_sobremesas, nome_arquivo)
    elif opcao == con+1:
        print("Alterando Sobremesas...")
        alterar(menu_sobremesas, nome_arquivo)
    elif opcao == con+2:
        print("Excluindo Sobremesas...")
        excluir(menu_sobremesas, nome_arquivo)
    elif opcao == con+3:
        print("Buscando itens...")
        buscar(menu_sobremesas)
    elif opcao == con+4:
        print("Voltando ao menu principal...")
        menu_principal()

menu_principal()