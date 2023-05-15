import random
import os
from time import sleep

# os.system('cls')

class Velha:
    def __init__(self):
        self.tabuleiro = [i for i in range(9)]
        self.lances = {}
        self.jogadas = [i for i in range(9)]
        self.partida = 1
        self.total_jogadas = 0
        self.reiniciar_partida()
    
    def reiniciar_partida(self):
        self.lances = {i: ' ' for i in self.tabuleiro}
        self.jogadas = [i for i in range(9)]
        self.partida = 1
        self.total_jogadas = 0

    def menu(self):
        #self.apresentacao()
        self.menu_jogada()
        
    
    def apresentacao(self):
        print('|==============================================|')
        print('|>>> Bem vindo ao jogo da velha!! by Dan :P <<<|')
        print('|==============================================|')
        print('')
        print("Vamos jogar, você será o 'X'!!")        

    def menu_jogada(self):
        print('')
        print('Com base no mapa abaixo, selecione a posição que deseja marcar:')
        self.mapa_partida(0)
        jogada = int(input())
        self.jogar(jogada)
        

    def mapa_partida(self,mapas): # 0 - Mapa menu | 1 - Mapa Jogadas
        if mapas == 0:
            mapa = {i: '{}'.format(i) for i in self.tabuleiro}
        else:
            mapa = self.lances
        print('')
        linha1 = {} 
        linha2 = {} 
        linha3 = {}  
        for i in mapa:             
            if i < 3:
                formatacao = '\33[4m'        
                linha1[i] = mapa[i]
                linha1[i] = formatacao + linha1[i]        
            elif i < 6:        
                linha2[i] = mapa[i]
                linha2[i] = formatacao + linha2[i] 
            elif i < 9:
                formatacao = '\33[m'
                linha3[i] = mapa[i]  
                linha3[i] = formatacao + linha3[i]
        print(" | ".join(str(elemento) for  elemento in linha1.values()))
        print(" | ".join(str(elemento) for elemento in linha2.values()))
        print(" | ".join(str(elemento) for elemento in linha3.values())) 


    def jogar(self,jogada):
        if self.jogadas[jogada] == jogada:
            self.lances[jogada] = 'x'
            self.jogadas[jogada] = 11
            print('')
            self.mapa_partida(1)
            sleep(1)
            self.validar('Você')
            self.total_jogadas += 1
            if self.partida == 1:
                self.pc_jogada()
        else: 
            print('Já existe uma jogada nesse campo!')
            sleep(2)
            
        
    def pc_jogada(self):
        print('')
        while True:
            pc = int(random.randint(0,8))
            print(pc)
            if self.jogadas[pc] == pc:
                self.lances[pc] = 'o'
                self.jogadas[pc] = 11
                self.total_jogadas += 1
                break
            elif self.total_jogadas >= 9:
                break  
        self.mapa_partida(1)
        self.validar('pc')

    def validar(self,jogador):         
         if self.lances[0] == 'x' and self.lances[1] == 'x' and self.lances[2] == 'x':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0
         elif self.lances[3] == 'x' and self.lances[4] == 'x' and self.lances[5] == 'x':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0
         elif self.lances[6] == 'x' and self.lances[7] == 'x' and self.lances[8] == 'x':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0
         elif self.lances[0] == 'x' and self.lances[3] == 'x' and self.lances[6] == 'x':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0
         elif self.lances[1] == 'x' and self.lances[4] == 'x' and self.lances[7] == 'x':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0
         elif self.lances[2] == 'x' and self.lances[5] == 'x' and self.lances[8] == 'x':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0
         elif self.lances[0] == 'x' and self.lances[4] == 'x' and self.lances[8] == 'x':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0
         elif self.lances[2] == 'x' and self.lances[4] == 'x' and self.lances[6] == 'x':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0 
         elif self.lances[0] == 'o' and self.lances[1] == 'o' and self.lances[2] == 'o':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0
         elif self.lances[3] == 'o' and self.lances[4] == 'o' and self.lances[5] == 'o':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0
         elif self.lances[6] == 'o' and self.lances[7] == 'o' and self.lances[8] == 'o':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0
         elif self.lances[0] == 'o' and self.lances[3] == 'o' and self.lances[6] == 'o':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0
         elif self.lances[1] == 'o' and self.lances[4] == 'o' and self.lances[7] == 'o':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0
         elif self.lances[2] == 'o' and self.lances[5] == 'o' and self.lances[8] == 'o':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0
         elif self.lances[0] == 'o' and self.lances[4] == 'o' and self.lances[8] == 'o':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0
         elif self.lances[2] == 'o' and self.lances[4] == 'o' and self.lances[6] == 'o':
            print('{} ganhou!!'.format(jogador))
            self.partida = 0 
         elif self.total_jogadas >= 9:
            print('Deu velha!!')
            self.partida = 0 
        

    def play(self):
        while self.partida == 1:
            jogo.menu_jogada()


jogo = Velha()
jogo.apresentacao()
while True :
    jogo.play()
    print('Deseja jogar novamente? 0 - Sim | 1 - Não ')
    valid = input()
    if valid == '1':
        break
    else: 
        print('Vamos jogar novamente!')
    jogo.reiniciar_partida()
    sleep(1)
    
