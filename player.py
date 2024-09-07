import pygame
import sys
import os
import random
import time
pygame.init()


class player:

    def __init__(self):
        self.playerwidth = 55
        self.playerheight = 40
        self.GREEN = (127, 255, 0)
        self.BLACK=(0,0,0)

        # player image #
        self.player_image = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
        self.player_image = pygame.transform.scale(self.player_image, (self.playerwidth, self.playerheight))
        self.player_image = pygame.transform.rotate(pygame.transform.scale(self.player_image, (self.playerwidth, self.playerheight)), 180)

        # shooting info #
        self.playershootimage = pygame.image.load((os.path.join('Assets', 'shoot.png')))
        self.playershootimage = pygame.transform.scale(self.playershootimage, (10, 20))
        self.player_bullets = []
        self.single_shot=True
        self.double_shot=False
        self.triple_shot=False

        # player locating #
        self.player_XY=pygame.Rect(100, 300, self.playerwidth, self.playerheight)

        # player stats #
        self.HP=130
        self.money_amount=1000000
        self.kill_count=0



    def set_money(self):
        font1 = pygame.font.SysFont('money : ' + str(self.money_amount), 22)
        moneydisplay = font1.render('money : ' + str(self.money_amount), True, self.GREEN)
        return moneydisplay

    def set_life(self):
        font2 = pygame.font.SysFont('life : ' + str(self.HP), 22)
        lifedisplay = font2.render('life : ' + str(self.HP), True, self.GREEN)
        return lifedisplay

    def lose_massage(self):
        font3 = pygame.font.SysFont('LOOSER!',80 )
        losedisplay = font3.render('LOOSER!', True, self.GREEN)
        return losedisplay
    def set_kills(self):
        font4=pygame.font.SysFont("killed "+str(self.kill_count),22)
        killsdisplay=font4.render("killed "+str(self.kill_count),True,self.GREEN )
        return killsdisplay


    def shootingfunc(self,player_bullets,enemy_objet,money_object,meteor_object):
        for bullet in player_bullets:
            bullet.y -= 7
            if bullet.y < 0:
                player_bullets.remove(bullet)
            for enemy in enemy_objet.enemylist:
                # check if hit enemy
                if enemy.colliderect(bullet):
                    enemy_objet.enemylist.remove(enemy)
                    self.player_bullets.remove(bullet)
                    money_object.moneybagmake(bullet,money_object.moneybaglist)
                    self.kill_count = self.kill_count+1
            for meteor in meteor_object.meteorlist:
                if meteor.colliderect(bullet):
                    money_object.moneybagmake(bullet,money_object.moneybaglist)
                    meteor_object.meteorlist.remove(meteor)
                    self.player_bullets.remove(bullet)


    def create_bullet(self):
        if self.single_shot==True:
            bullet = pygame.Rect(self.player_XY.x + self.playerwidth // 2 - 2,
                                 self.player_XY.y + self.playerheight // 2, 10, 5)
            self.player_bullets.append(bullet)
        elif self.double_shot==True:
            bullet = pygame.Rect(self.player_XY.x + self.playerwidth // 2 - 15,
                                 self.player_XY.y + self.playerheight // 2, 10, 5)
            self.player_bullets.append(bullet)
            bullet = pygame.Rect(self.player_XY.x + self.playerwidth // 2 +15,
                                 self.player_XY.y + self.playerheight // 2, 10, 5)
            self.player_bullets.append(bullet)
        elif self.triple_shot==True:
            bullet = pygame.Rect(self.player_XY.x + self.playerwidth // 2 - 22,
                                 self.player_XY.y + self.playerheight // 2, 10, 5)
            self.player_bullets.append(bullet)
            bullet = pygame.Rect(self.player_XY.x + self.playerwidth // 2 + 0,
                                 self.player_XY.y + self.playerheight // 2-5, 10, 5)
            self.player_bullets.append(bullet)
            bullet = pygame.Rect(self.player_XY.x + self.playerwidth // 2 + 22,
                                 self.player_XY.y + self.playerheight // 2, 10, 5)
            self.player_bullets.append(bullet)

    def playermove(self,keys_pressed,player_XY):
        VEL=5
        if keys_pressed[pygame.K_a]:  # left
            if player_XY.x > 5:
                player_XY.x = player_XY.x - VEL
        if keys_pressed[pygame.K_d]:  # right
            if player_XY.x < 860:
                player_XY.x = player_XY.x + VEL
        if keys_pressed[pygame.K_s]:  # down
            if player_XY.y < 460:
                player_XY.y = player_XY.y + VEL
        if keys_pressed[pygame.K_w]:  # up
            if player_XY.y > 5:
                player_XY.y = player_XY.y - VEL


