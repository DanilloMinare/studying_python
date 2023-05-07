import os
from time import sleep
#menu_abas =['Portifólio','Alugar','Devolver']
def teste():
    print('funciona')
    sleep(3)

carros = ['BMW 320i','Porshe 911','Audi RS5']
valores = {'BMW 320i':250,'Porshe 911':450,'Audi RS5':600}
alugados = []

def alugar():
    
    while True:
        os.system('cls')
        x = 0
        for i in carros:
            print('{} - {}: R${}'.format(x,carros[x],valores[carros[x]]))
            x = x + 1
        print('')
        print('Digite o código do carro:')
        car_select = int(input(''))
        print('Digite a quantidade de dias:')
        quant_dias = int(input())
        total = quant_dias * valores[carros[car_select]]
        print('O valor total é de R$ {}, deseja alugar? 0 - Sim | 1 - Não'.format(total))
        vali_alug = input()
        while True:
            if vali_alug == '0':
                alugados.append(carros.pop(car_select))
                print('Alugado!')
                sleep(2)
                break
            elif vali_alug == '1':
                break
            else: 
                print('Digite um valor válido') 
                vali_alug = input()
        os.system('cls')
        break

        
                

def portifolio():
    x = 0
    for i in carros:
        print('{} - {}: R${}'.format(x,carros[x],valores[carros[x]]))
        x = x + 1
            
    while True:    
        print('Deseja alugar? 0 - Sim | 1 - Não')
        validador=input('')
        if validador == '0':
                alugar()
        elif validador == '1':
                os.system('cls')
                break
        else:
            print('Digite um valor válido.')

def apresentacao():
    
    print('########################################################')
    print('')
    print('Bem Vindo a nossa Rent Car!')
    print('')
    print('########################################################')

def menu():    
    while True:
        sleep(1)
        print('Selecione uma opção:')
        print('')
        menu_abas =['Portifólio','Alugar','Devolver','Sair']
        lista_menu=[]
        x = 0
        for i in menu_abas:        
            lista_menu.append( " {} - {} | ".format(x,menu_abas[x]))
            x = x + 1
        print(" ".join(str(elemento) for elemento in lista_menu))
        print('')
        drive = input()   
        if drive == '0':
            portifolio()
        elif drive == '1':
            alugar()
        elif drive == '2':
            teste()
        elif drive == '3':
            break
        else:
            print('Digite uma opção válida.')
            print('')
    print('')    
    print('Até logo!! :)')
    sleep(2)
    os.system('cls')

os.system('cls')
apresentacao()
menu()

