import os
import sys
from bebidas import bebidas as Bebidas
from entradas import Entradas as Entradas
def espaçamento(x):
    return " " * x

def menu_principal():
    menu_principal = ['Bebidas','Entradas','Pratos Principais','Sobremesas']
    sair = ['Sair']

    tamls = len(menu_principal)

    ind = 0
    con = 0

    tamanho = [len(word) for word in menu_principal]

    print("______________________________/ BEBIDAS \______________________________")
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
        print("Pratos Principais")
    elif opcao == menu_principal.index('Sobremesas'):
        print("Sobremesas")
    elif opcao == tamls:
        print("Saindo do programa...")
        exit()
    elif opcao > tamls:
        print("Opção inválida, tente novamente...")
        menu_principal()
    
def MenuBebidas():
    menu_bebidas = Bebidas
    Voltar = ['Voltar']
    tamls = len(menu_bebidas.keys())

    ind = 0
    con = 0

    tamanho = [len(word) for word in menu_bebidas.keys()]
    numeros = [sum(char.isdigit() for char in str(value)) for value in menu_bebidas.values()]

    print("______________________________/ BEBIDAS \______________________________")
    while con < tamls:
    
        print(f'|\t\t\t\t{con} - {list(menu_bebidas.keys())[ind]} - R${list(menu_bebidas.values())[ind]}{espaçamento(29 - tamanho[con] - numeros[ind])}|')
        con += 1
        ind += 1
    print(f"|\t\t\t\t{con} - {Voltar[0] + espaçamento(35 - len(Voltar[0]))}|")
    print("|______________________________________________________________________|")
    opcao = int(input("Escolha uma opção: "))
    if opcao == con:
        print("Voltando ao menu principal...")
        menu_principal()
        
def MenuEntradas():
    menu_entradas = {'Refrigerante': 5.00, 'Suco': 4.00, 'Água': 3.00, 'Cerveja': 6.00, 'Vinho': 8.00, 'Whisky': 1000.00}
    
    tamls = len(menu_entradas.keys())

    ind = 0
    con = 0

    tamanho = [len(word) for word in menu_entradas.keys()]
    numeros = [sum(char.isdigit() for char in str(value)) for value in menu_entradas.values()]

    print("______________________________/ BEBIDAS \______________________________")
    while con < tamls:
    
        print(f'|\t\t\t\t{con} - {list(menu_entradas.keys())[ind]} - R${list(menu_entradas.values())[ind]}{espaçamento(29 - tamanho[con] - numeros[ind])}|')
        con += 1
        ind += 1
    print("|______________________________________________________________________|")

menu_principal()