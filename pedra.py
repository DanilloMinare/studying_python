import os
import random
from time import sleep

os.system('cls')
sleep(1)
print("=========================================")
print("Bem vindo ao jogo Pedra, Papel ou Tesoura")


jogadas = {0:'Pedra',1:'Papel',2:'Tesoura'}

j1 = 0
j2 = 0

def back(jogada1,jogada2):
    if jogada1 == 0 and jogada2 == 0:
        print('Empate!!')
    elif jogada1 == 0 and jogada2 == 1:
        print('O computador venceu!)')
        j2 = (j2 + 1)
    elif jogada1 == 0 and jogada2 == 2:
        print('Você venceu!')
        j1 = j1 + 1
    elif jogada1 == 1 and jogada2 == 0:
        print('Você venceu!')
        j1 = j1 + 1
    elif jogada1 == 1 and jogada2 == 1:
        print('Empate!')
    elif jogada1 == 1 and jogada2 == 2:
        print('O computador venceu!')
        j2 = j2 + 1
    elif jogada1 == 2 and jogada2 == 0:
        print('O computador venceu!')
        j2 = j2 + 1
    elif jogada1 == 2 and jogada2 == 1:
        print('Você venceu!')
        j1 = j1 + 1
    elif jogada1 == 2 and jogada2 == 2:
        print('Empate')
    return
while True:
    os.system('cls')
    print("=========================================")
    print('')
    print('PLACAR:')
    print('>>> Você: {}'.format(j1))
    print('>>> Computador: {}'.format(j2))
    print('')
    sleep(1)
    print('Escolha seu lance:')
    print('0 - Pedra | 1 - Papel | 2 - Tesoura')
    jogada1 = int(input())
    jogada2 = random.randint(0,2)
    print('')
    print('=====================================')
    print('Sua jogada foi: {}'.format(jogadas[jogada1]))
    print('Jogada do PC: {}'.format(jogadas[jogada2]))
   
    if jogada1 == 0 and jogada2 == 0:
        print('Empate!!')
    elif jogada1 == 0 and jogada2 == 1:
        print('O computador venceu!)')
        j2 = (j2 + 1)
    elif jogada1 == 0 and jogada2 == 2:
        print('Você venceu!')
        j1 = j1 + 1
    elif jogada1 == 1 and jogada2 == 0:
        print('Você venceu!')
        j1 = j1 + 1
    elif jogada1 == 1 and jogada2 == 1:
        print('Empate!')
    elif jogada1 == 1 and jogada2 == 2:
        print('O computador venceu!')
        j2 = j2 + 1
    elif jogada1 == 2 and jogada2 == 0:
        print('O computador venceu!')
        j2 = j2 + 1
    elif jogada1 == 2 and jogada2 == 1:
        print('Você venceu!')
        j1 = j1 + 1
    elif jogada1 == 2 and jogada2 == 2:
        print('Empate')
    print('=====================================')
    print('')
    print('Jogar novamente? 0 - SIM | 1 - NÂO')
    menu = int(input())
    if menu == 1:
        break
    else: continue
