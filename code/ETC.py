import pygame
import sys
import os
import random
import time
pygame.init()


class money:
    def __init__(self):
        # money info #
        self.moneywidth = 30
        self.moneyhight = 35
        self.money_image = pygame.image.load(os.path.join('Assets', 'moneybag2.png'))
        self.money_image = pygame.transform.scale(self.money_image, (self.moneywidth, self.moneyhight))
        self.moneybaglist = []

    def moneybagmake(self,bullet, moneybaglist):
        bag = pygame.Rect(bullet.x, bullet.y, self.moneywidth, self.moneyhight)
        moneybaglist.append(bag)

    def moneybagmoving(self,player1):
        for bag in self.moneybaglist:
            bag.y = bag.y + 4
            if bag.colliderect(player1.player_XY):
                self.moneybaglist.remove(bag)
                player1.money_amount=player1.money_amount+100
            if bag.y > 500:
                self.moneybaglist.remove(bag)


class meteor:
    def __init__(self):
        self.meteorwidth = 40
        self.meteorhight = 45
        self.meteor_image = pygame.image.load(os.path.join('Assets', 'meteor2.png'))
        self.meteor_image = pygame.transform.scale(self.meteor_image, (self.meteorwidth, self.meteorhight))
        self.meteor_image = pygame.transform.rotate(pygame.transform.scale(self.meteor_image, (self.meteorwidth, self.meteorhight)), 65)
        self.meteorlist = []

    def meteorspawn(self):
        randomx = random.randint(0, 450)
        meteor = pygame.Rect(randomx, 10, 20, 25)
        self.meteorlist.append(meteor)

    def movingmeteor(self,player1):
        for meteor in self.meteorlist:
            meteor.x = meteor.x + 3
            meteor.y = meteor.y + 3
            if meteor.x > 900:
                self.meteorlist.remove(meteor)
            elif meteor.y > 500:
                self.meteorlist.remove(meteor)
            if meteor.colliderect(player1.player_XY):
                player1.HP=player1.HP-5
                self.meteorlist.remove(meteor)