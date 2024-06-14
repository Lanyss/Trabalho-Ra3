<<<<<<< Updated upstream
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
=======
from bebidas import bebidas as Bebidas # importa a lista de bebidas
from entradas import entradas as Entradas # importa a lista de entradas
from principais import principais as principais # importa a lista de pratos principais
from sobremesas import sobremesas as Sobremesas # importa a lista de sobremesas
from adicionar import adicionar # importa a função adicionar
from excluir import excluir # importa a função excluir
from alterar import alterar # importa a função alterar
from buscar import buscar # importa a função buscar
def espaçamento(x): # função que retorna um espaço com o valor de x
    return " " * x 
>>>>>>> Stashed changes

def menu_principal(): # função que exibe o menu principal
    menu_principal = ['Bebidas','Entradas','Pratos Principais','Sobremesas'] # lista de opções do menu principal
    sair = ['Sair'] 

    tamls = len(menu_principal) # tamanho da lista de opções do menu principal

    ind = 0 # índice
    con = 0 # contador

    tamanho = [len(word) for word in menu_principal] # lista com o tamanho de cada palavra da lista de opções do menu principal

<<<<<<< Updated upstream
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
=======
    print("_____________________________| Principal |_____________________________") # imprime o cabeçalho
    while con < tamls: # enquanto o contador for menor que o tamanho da lista de opções do menu principal
    
        print(f'|\t\t\t\t{con} - {menu_principal[ind]}{espaçamento(35 - tamanho[con])}|') # imprime a opção do menu principal
        con += 1 # incrementa o contador
        ind += 1 # incrementa o índice
    print(f"|\t\t\t\t{con} - {sair[0] + espaçamento(35 - len(sair[0]))}|") # imprime a opção de sair
    print("|______________________________________________________________________|") # imprime o rodapé
    opcao = int(input("Escolha uma opção: ")) # solicita a opção
    if opcao == menu_principal.index('Bebidas'): # se a opção for 'Bebidas'
        MenuBebidas() # chama a função MenuBebidas
    elif opcao == menu_principal.index('Entradas'): # se a opção for 'Entradas'
        MenuEntradas() # chama a função MenuEntradas
    elif opcao == menu_principal.index('Pratos Principais'): # se a opção for 'Pratos Principais'
        MenuPrincipais() # chama a função MenuPrincipais
    elif opcao == menu_principal.index('Sobremesas'): # se a opção for 'Sobremesas'
        MenuSobremesas() # chama a função MenuSobremesas
    elif opcao == tamls: # se a opção for 'Sair'
        print("Saindo do programa...") # imprime a mensagem
        exit() # sai do programa
    elif opcao > tamls: # se a opção for maior que o tamanho da lista de opções do menu principal
        print("Opção inválida, tente novamente...") # imprime a mensagem
        menu_principal() # chama a função menu_principal



def MenuBebidas(): # função que exibe o menu de bebidas
    nome_arquivo = 'bebidas' # nome do arquivo
    menu_bebidas = Bebidas # lista de bebidas
    Voltar = ['Voltar'] # opção de voltar
    Alterar = ['Alterar'] # opção de alterar
    Adicionar = ['Adicionar'] # opção de adicionar
    Excluir = ['Excluir'] # opção de excluir
    Buscar = ['Buscar'] # opção de buscar
    tamls = len(menu_bebidas) # tamanho da lista de bebidas

    ind = 0 # índice
    con = 0 # contador

    tamanho = [len(str(item["nome"])) for item in menu_bebidas]  # lista com o tamanho de cada nome da lista de bebidas 
    tamanho_valor = [len(str(item["valor"])) for item in menu_bebidas] # lista com o tamanho de cada valor da lista de bebidas
    tamanho_con = [len(str(con)) for con in range(tamls)] # lista com o tamanho de cada contador da lista de bebidas 

    print("______________________________| BEBIDAS |______________________________") # imprime o cabeçalho
    while con < tamls: # enquanto o contador for menor que o tamanho da lista de bebidas
    
        print(f'|\t\t\t\t{con} - {(menu_bebidas)[ind]["nome"]} - R${str((menu_bebidas)[ind]["valor"])}{espaçamento(31 - tamanho[con] - tamanho_valor[con] - tamanho_con[con])}|') # imprime o nome e o valor da bebida de acordo com o índice e subtrai o tamanho do nome, do valor e do contador do espaço para alinhar as linhas do menu
        con += 1 # incrementa o contador
        ind += 1 # incrementa o índice
    print(f"|\t\t\t\t{con} - {Adicionar[0] + espaçamento(31 - len(Voltar[0]))}|") # imprime a opção de adicionar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+1} - {Alterar[0] + espaçamento(33 - len(Voltar[0]))}|") # imprime a opção de alterar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+2} - {Excluir[0] + espaçamento(33 - len(Voltar[0]))}|") # imprime a opção de excluir subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+3} - {Buscar[0] + espaçamento(33 - len(Voltar[0]))}|") # imprime a opção de buscar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+4} - {Voltar[0] + espaçamento(34 - len(Voltar[0]))}|") # imprime a opção de voltar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print("|______________________________________________________________________|") # imprime o rodapé
    opcao = int(input("Escolha uma opção: ")) # solicita a opção
    if opcao == con: # se a opção for igual ao contador
        print("Adcionando bebidas...") # imprime a mensagem
        adicionar(menu_bebidas, nome_arquivo) # chama a função adicionar
    elif opcao == con+1: # se a opção for igual ao contador + 1
        print("Alterando bebidas...") # imprime a mensagem
        alterar(menu_bebidas, nome_arquivo) # chama a função alterar
    elif opcao == con+2: # se a opção for igual ao contador + 2
        print("Excluindo bebidas...") # imprime a mensagem
        excluir(menu_bebidas, nome_arquivo) # chama a função excluir
    elif opcao == con+3: # se a opção for igual ao contador + 3
        print("Buscando itens...") # imprime a mensagem
        buscar(menu_bebidas) # chama a função buscar
    elif opcao == con+4: # se a opção for igual ao contador + 4
        print("Voltando ao menu principal...") # imprime a mensagem
        menu_principal() # chama a função menu_principal
>>>>>>> Stashed changes

def MenuEntradas(): # função que exibe o menu de entradas
    nome_arquivo = 'entradas' # nome do arquivo
    menu_entradas = Entradas # lista de entradas
    Voltar = ['Voltar'] # opção de voltar
    Alterar = ['Alterar'] # opção de alterar
    Adicionar = ['Adicionar'] # opção de adicionar
    Excluir = ['Excluir'] # opção de excluir
    Buscar = ['Buscar'] # opção de buscar
    tamls = len(menu_entradas) # tamanho da lista de entradas

<<<<<<< Updated upstream
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
=======
    ind = 0 # índice
    con = 0 # contador

    tamanho = [len(str(item["nome"])) for item in menu_entradas] # lista com o tamanho de cada nome da lista de entradas
    tamanho_valor = [len(str(item["valor"])) for item in menu_entradas] # lista com o tamanho de cada valor da lista de entradas
    tamanho_con = [len(str(con)) for con in range(tamls)] # lista com o tamanho de cada contador da lista de entradas

    print("______________________________| Entradas |______________________________") # imprime o cabeçalho
    while con < tamls: # enquanto o contador for menor que o tamanho da lista de entradas
    
        print(f'|\t\t\t\t{con} - {(menu_entradas)[ind]["nome"]} - R${str((menu_entradas)[ind]["valor"])}{espaçamento(31 - tamanho[con] - tamanho_valor[con] - tamanho_con[con])}|') # imprime o nome e o valor da entrada de acordo com o índice e subtrai o tamanho do nome, do valor e do contador do espaço para alinhar as linhas do menu
        con += 1 # incrementa o contador
        ind += 1 # incrementa o índice
    print(f"|\t\t\t\t{con} - {Adicionar[0] + espaçamento(31 - len(Voltar[0]))}|") # imprime a opção de adicionar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+1} - {Alterar[0] + espaçamento(33 - len(Voltar[0]))}|") # imprime a opção de alterar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+2} - {Excluir[0] + espaçamento(33 - len(Voltar[0]))}|") # imprime a opção de excluir subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+3} - {Buscar[0] + espaçamento(33 - len(Voltar[0]))}|") # imprime a opção de buscar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+4} - {Voltar[0] + espaçamento(34 - len(Voltar[0]))}|") # imprime a opção de voltar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print("|______________________________________________________________________|") # imprime o rodapé
    opcao = int(input("Escolha uma opção: ")) # solicita a opção
    if opcao == con: # se a opção for igual ao contador
        print("Adcionando entradas...") # imprime a mensagem
        adicionar(menu_entradas, nome_arquivo) # chama a função adicionar
    elif opcao == con+1: # se a opção for igual ao contador + 1
        print("Alterando entradas...") # imprime a mensagem
        alterar(menu_entradas, nome_arquivo) # chama a função alterar
    elif opcao == con+2: # se a opção for igual ao contador + 2
        print("Excluindo entradas...")  # imprime a mensagem
        excluir(menu_entradas, nome_arquivo) # chama a função excluir
    elif opcao == con+3: # se a opção for igual ao contador + 3
        print("Buscando itens...") # imprime a mensagem
        buscar(menu_entradas) # chama a função buscar
    elif opcao == con+4: # se a opção for igual ao contador + 4
        print("Voltando ao menu principal...") # imprime a mensagem
        menu_principal() # chama a função menu_principal


def MenuPrincipais(): # função que exibe o menu de pratos principais
    nome_arquivo = 'principais' # nome do arquivo
    menu_principais = principais    # lista de pratos principais
    Voltar = ['Voltar'] # opção de voltar
    Alterar = ['Alterar'] # opção de alterar
    Adicionar = ['Adicionar']   # opção de adicionar
    Excluir = ['Excluir']   # opção de excluir
    Buscar = ['Buscar'] # opção de buscar
    tamls = len(menu_principais)    # tamanho da lista de pratos principais

    ind = 0 # índice
    con = 0 # contador

    tamanho = [len(str(item["nome"])) for item in menu_principais]  # lista com o tamanho de cada nome da lista de pratos principais
    tamanho_valor = [len(str(item["valor"])) for item in menu_principais]   # lista com o tamanho de cada valor da lista de pratos principais
    tamanho_con = [len(str(con)) for con in range(tamls)]       # lista com o tamanho de cada contador da lista de pratos principais

    print("______________________________| Pratos Principais |______________________________")  # imprime o cabeçalho
    while con < tamls:  # enquanto o contador for menor que o tamanho da lista de pratos principais
    
        print(f'|\t\t\t\t{con} - {(menu_principais)[ind]["nome"]} - R${str((menu_principais)[ind]["valor"])}{espaçamento(31 - tamanho[con] - tamanho_valor[con] - tamanho_con[con])}|') # imprime o nome e o valor do prato principal de acordo com o índice e subtrai o tamanho do nome, do valor e do contador do espaço para alinhar as linhas do menu
        con += 1    # incrementa o contador
        ind += 1    # incrementa o índice
    print(f"|\t\t\t\t{con} - {Adicionar[0] + espaçamento(31 - len(Voltar[0]))}|")   # imprime a opção de adicionar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+1} - {Alterar[0] + espaçamento(33 - len(Voltar[0]))}|")   # imprime a opção de alterar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+2} - {Excluir[0] + espaçamento(33 - len(Voltar[0]))}|")   # imprime a opção de excluir subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+3} - {Buscar[0] + espaçamento(33 - len(Voltar[0]))}|")    # imprime a opção de buscar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+4} - {Voltar[0] + espaçamento(34 - len(Voltar[0]))}|")    # imprime a opção de voltar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print("|______________________________________________________________________|")   # imprime o rodapé
    opcao = int(input("Escolha uma opção: "))   # solicita a opção
    if opcao == con:    # se a opção for igual ao contador
        print("Adcionando Pratos...")   # imprime a mensagem
        adicionar(menu_principais, nome_arquivo)    # chama a função adicionar
    elif opcao == con+1:    # se a opção for igual ao contador + 1  
        print("Alterando Pratos...")    # imprime a mensagem
        alterar(menu_principais, nome_arquivo)  # chama a função alterar
    elif opcao == con+2:    # se a opção for igual ao contador + 2
        print("Excluindo Pratos...")    # imprime a mensagem
        excluir(menu_principais, nome_arquivo)  # chama a função excluir
    elif opcao == con+3:   # se a opção for igual ao contador + 3
        print("Buscando itens...")  # imprime a mensagem
        buscar(menu_principais) # chama a função buscar
    elif opcao == con+4:    # se a opção for igual ao contador + 4  
        print("Voltando ao menu principal...")  # imprime a mensagem
        menu_principal()    # chama a função menu_principal
>>>>>>> Stashed changes


<<<<<<< Updated upstream
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
=======
def MenuSobremesas():   # função que exibe o menu de sobremesas
    nome_arquivo = 'sobremesas' # nome do arquivo
    menu_sobremesas = Sobremesas    # lista de sobremesas
    Voltar = ['Voltar'] # opção de voltar
    Alterar = ['Alterar']   # opção de alterar
    Adicionar = ['Adicionar']   # opção de adicionar
    Excluir = ['Excluir']   # opção de excluir
    Buscar = ['Buscar'] # opção de buscar
    tamls = len(menu_sobremesas)    # tamanho da lista de sobremesas

    ind = 0 # índice
    con = 0 # contador

    tamanho = [len(str(item["nome"])) for item in menu_sobremesas]  # lista com o tamanho de cada nome da lista de sobremesas
    tamanho_valor = [len(str(item["valor"])) for item in menu_sobremesas]   # lista com o tamanho de cada valor da lista de sobremesas
    tamanho_con = [len(str(con)) for con in range(tamls)]    # lista com o tamanho de cada contador da lista de sobremesas

    print("______________________________| Sobremesas |______________________________")   # imprime o cabeçalho
    while con < tamls:  # enquanto o contador for menor que o tamanho da lista de sobremesas
    
        print(f'|\t\t\t\t{con} - {(menu_sobremesas)[ind]["nome"]} - R${str((menu_sobremesas)[ind]["valor"])}{espaçamento(31 - tamanho[con] - tamanho_valor[con] - tamanho_con[con])}|') # imprime o nome e o valor da sobremesa de acordo com o índice e subtrai o tamanho do nome, do valor e do contador do espaço para alinhar as linhas do menu
        con += 1    # incrementa o contador
        ind += 1        # incrementa o índice   
    print(f"|\t\t\t\t{con} - {Adicionar[0] + espaçamento(31 - len(Voltar[0]))}|")   # imprime a opção de adicionar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+1} - {Alterar[0] + espaçamento(33 - len(Voltar[0]))}|")   # imprime a opção de alterar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+2} - {Excluir[0] + espaçamento(33 - len(Voltar[0]))}|")   # imprime a opção de excluir subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+3} - {Buscar[0] + espaçamento(33 - len(Voltar[0]))}|")    # imprime a opção de buscar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print(f"|\t\t\t\t{con+4} - {Voltar[0] + espaçamento(34 - len(Voltar[0]))}|")    # imprime a opção de voltar subtraindo o tamanho da opção de voltar do espaço para alinhar as linhas do menu
    print("|______________________________________________________________________|")   # imprime o rodapé
    opcao = int(input("Escolha uma opção: "))   # solicita a opção
    if opcao == con:    # se a opção for igual ao contador
        print("Adcionando Sobremesas...")   # imprime a mensagem
        adicionar(menu_sobremesas, nome_arquivo)    # chama a função adicionar
    elif opcao == con+1:    # se a opção for igual ao contador + 1
        print("Alterando Sobremesas...")    # imprime a mensagem
        alterar(menu_sobremesas, nome_arquivo)  # chama a função alterar
    elif opcao == con+2:    # se a opção for igual ao contador + 2
        print("Excluindo Sobremesas...")    # imprime a mensagem
        excluir(menu_sobremesas, nome_arquivo)  # chama a função excluir
    elif opcao == con+3:    # se a opção for igual ao contador + 3
        print("Buscando itens...")  # imprime a mensagem
        buscar(menu_sobremesas) # chama a função buscar
    elif opcao == con+4:    # se a opção for igual ao contador + 4
        print("Voltando ao menu principal...")  # imprime a mensagem
        menu_principal()    # chama a função
>>>>>>> Stashed changes

menu_principal()    # chama a função menu_principal