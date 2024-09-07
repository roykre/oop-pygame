import pygame
import sys
import os
import random
import time
pygame.init()

class store:
    def __init__(self):
        self.store_image = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'store.png')), (900, 500))
        self.GREEN = (127, 255, 0)
        self.font = pygame.font.SysFont('', 50)
        self.massage = self.font.render('', True, self.GREEN)
        self.massage1=0

    def buying_double_shot(self,player1):
        if player1.money_amount>2000 and player1.double_shot==False and player1.triple_shot==False:
            player1.money_amount-=2000
            player1.single_shot=False
            player1.double_shot=True
            self.font = pygame.font.SysFont('you just bought double shot!', 50)
            self.massage = self.font.render('you just bought double shot!', True, self.GREEN)
            self.massage1 = 1
    def buying_triple_shot(self,player1):
        if player1.money_amount>5000 and player1.triple_shot==False:
            player1.money_amount-=5000
            player1.single_shot=False
            player1.double_shot=False
            player1.triple_shot=True
            self.font = pygame.font.SysFont('you just bought triple shot!', 50)
            self.massage = self.font.render('you just bought triple shot!', True, self.GREEN)
            self.massage1 = 1
    def buying_HP(self,player1):
        if player1.money_amount>1000:
            player1.money_amount-=1000
            player1.HP=player1.HP+30
            self.font = pygame.font.SysFont('you just bought 30 HP!', 50)
            self.massage = self.font.render('you just bought 30 HP', True, self.GREEN)
            self.massage1 = 1
    def set_massage(self):
        self.font = pygame.font.SysFont('', 50)
        self.massage = self.font.render('', True, self.GREEN)




