## Limpa Terminal:
import os

def limpar_terminal():
    sistema = os.name
    if sistema == 'nt':
        os.system('cls')
    else:
        os.system('clear')

## Menu Inicial:
def menu_inicial():
    while True:
        limpar_terminal()
        inicial = int(input("Selecione a opção abaixo:\n1 - Office\n2 - Aulas\n3 - Sair\n"))
        
        if inicial == 1:
            office()
        elif inicial == 2:
            aulas()
        elif inicial == 3:
            print("\n2 Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

## Office:
def office():
    while True:
        limpar_terminal()
        office = int(input("Para voltar ao menu inicial digite 2: "))
        if office== 2:
            print("Voltando ao menu inicial...")
            break
        else:
            print("Opção inválida. Tente novamente.")

## Aulas:
def aulas():
    while True:
        limpar_terminal()
        aulas = int(input("Selecione uma opção de Aulas:\n1 - Aulas de Python\n2 - Aulas de Matemática\n3 - Voltar ao menu inicial\n"))
        if aulas == 1:
            print("Você escolheu Aulas de Python.")
        elif aulas == 2:
            print("Você escolheu Aulas de Matemática.")
        elif aulas == 3:
            print("Voltando ao menu inicial...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia:
menu_inicial()