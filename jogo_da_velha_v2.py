import random
import os
from time import sleep

class jogo_da_velha:
    def __init__(self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]

    def tabuleiro(self):
        print("")
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("-----------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("-----------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])
        

    def reiniciar_jogo(self):
        pass

    def validar_jogada(self):
        pass

    def jogador(self):
        pass

    def mover(self):
        pass

self = jogo_da_velha()
self.tabuleiro()