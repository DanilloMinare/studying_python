import random
import os

os.system('cls')

class Velha:
    def __init__(self):
        self.tabuleiro = [i for i in range(9)]
        self.lances = {}
        self.reiniciar_partida()
    
    def reiniciar_partida(self):
        self.lances = {i: ' ' for i in self.tabuleiro}

    def menu(self):
        #self.apresentacao()
        self.mapa_partida(0)
        self.menu_jogada()
        
    
    def apresentacao(self):
        print('|==============================================|')
        print('|>>> Bem vindo ao jogo da velha!! by Dan :P <<<|')
        print('|==============================================|')
        print('')
        print("Vamos jogar, você será o 'X'!!")        

    def menu_jogada(self):
        print('')
        print('Com base no mapa acima, selecione a posição que deseja marcar:')
        jogada = input()
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
        print(" | ".join(str(elemento) for elemento in linha1.values()))
        print(" | ".join(str(elemento) for elemento in linha2.values()))
        print(" | ".join(str(elemento) for elemento in linha3.values())) 


    def jogar(self,jogada):
        print('Jogou!')



jogo = Velha()

jogo.apresentacao()
jogo.menu()
jogo.mapa_partida(1)