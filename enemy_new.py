import pygame
import sys
import os
import random
import time
pygame.init()


class enemy1():
    def __init__(type,self):
        if type==1:
            # enemy lvl 1 info #
            self.enemy1_image = pygame.image.load(os.path.join('Assets', 'enemy.png'))
            self.enemy1_image = pygame.transform.scale(self.enemy1_image, (45, 50))
            self.enemy1_shot_image = pygame.image.load(os.path.join('Assets', 'enemy2 shot.png'))
            self.enemy1_shot_image = pygame.transform.scale(self.enemy1_shot_image, (8, 18))

            # other enemy info #
            self.enemylist = []
            self.enemy1bulletlist = []
            # lvl1#
            self.step = 0

        self.sine_wave_values = [100, 101, 103, 104, 106, 107, 109, 110, 112, 113, 115, 116, 118, 119, 121, 122, 124, 125, 126, 128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 143, 144, 145, 145, 146, 147, 147, 148, 148, 148, 149, 149, 149, 149, 149, 149, 150, 149, 149, 149, 149, 149, 149, 148, 148, 148, 147, 147, 146, 145, 145, 144, 143, 143, 142, 141, 140, 139, 138, 137, 136, 135, 134, 133, 131, 130, 129, 128, 126, 125, 124, 122, 121, 119, 118, 116, 115, 113, 112, 110, 109, 107, 106, 104, 103, 101, 100, 99, 97, 96, 94, 93, 91, 90, 88, 87, 85, 84, 82, 81, 79, 78, 76, 75, 74, 72, 71, 70, 69, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 57, 56, 55, 55, 54, 53, 53, 52, 52, 52, 51, 51, 51, 51, 51, 51, 50, 51, 51, 51, 51, 51, 51, 52, 52, 52, 53, 53, 54, 55, 55, 56, 57, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70, 71, 72, 74, 75, 76, 78, 79, 81, 82, 84, 85, 87, 88, 90, 91, 93, 94, 96, 97, 99]
        if type==2:
            # enemy lvl 1 info #
            self.enemy1_image = pygame.image.load(os.path.join('Assets', 'enemy2.png'))
            self.enemy1_image = pygame.transform.scale(self.enemy1_image, (55, 50))
            self.enemy1_shot_image = pygame.image.load(os.path.join('Assets', 'enemy2 shot.png'))
            self.enemy1_shot_image = pygame.transform.scale(self.enemy1_shot_image, (8, 18))

            # other enemy info #
            self.enemylist = []
            self.enemy2bulletlist = []
            # lvl1#
            self.step = 0
    def create_enemy_bullet(enemylist,self):
        for i in range(0, 5):

            if len(self.enemylist)>0:
                k = random.randint(0, len(self.enemylist) - 1)
                bullet = pygame.Rect(self.enemylist[k].x, self.enemylist[k].y, 5, 15)
                self.enemybulletlist.append(bullet)