import pygame
import sys
import os
import random
import time
pygame.init()
import player
from player import *
import enemy
from enemy import *
import store
from store import *
import ETC
from ETC import *
import math


WIDTH,HEIGHT=900,500
gameboard=pygame.display.set_mode((WIDTH,HEIGHT))
space=pygame.transform.scale(pygame.image.load(os.path.join('Assets','bg.png')),(WIDTH,HEIGHT))
pygame.display.set_caption("lost in space 1")
FPS = 50

def main():
    i=0
    clock = pygame.time.Clock()

    store_object=store()
    enemy_object=enemy()
    player1=player()
    money_object=money()
    meteor_object=meteor()
    startTimeforshooting = time.time()
    startTimeformeteor = time.time()


    #game loop #
    main_run = True
    i = time.time()
    k = 0
    while main_run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_run=False

            # store loop (press p) #
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    store_run=True
                    while store_run:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key==pygame.K_p:
                                    store_run=False
                                elif event.key==pygame.K_1:
                                    store_object.buying_double_shot(player1)
                                    drawstoremassges(store_object)
                                elif event.key==pygame.K_2:
                                    store_object.buying_triple_shot(player1)
                                    drawstoremassges(store_object)
                                elif event.key==pygame.K_3:
                                    store_object.buying_HP(player1)
                                    drawstoremassges(store_object)

                        drawstore(store_object)

            # create player bullet limit of 20 bullets #
            if event.type == pygame.KEYDOWN and len(player1.player_bullets)<20:
                if event.key==pygame.K_h :
                    player1.create_bullet()

            # spawn new enemys if all the enemys dead #
            if len(enemy_object.enemylist) == 0:
                enemy_object.create_enemy1()

        # dying #
        if player1.HP<=0:
            drawlosemassge(player1)
            break
        if k % 100==0:
            a=time.time()
            print("100 loops in ", a-i," total :",k)

            i=time.time()
        k += 1
        #enemy create bullet  #
        Time_now1 = time.time()
        if Time_now1 - startTimeforshooting  >= 1.2:
            startTimeforshooting  = time.time()
            enemy_object.create_enemy_bullet()
        # create meteor
        Time_now2 = time.time()
        if Time_now2 - startTimeformeteor >= 1.2:
            startTimeformeteor = time.time()
            meteor_object.meteorspawn()
        keys_pressed = pygame.key.get_pressed()
        player1.playermove(keys_pressed,player1.player_XY)
        player1.shootingfunc(player1.player_bullets,enemy_object,money_object,meteor_object)
        enemy_object.enemy_move_bullet(player1)
        enemy_object.lvl2_movingfunc()
        money_object.moneybagmoving(player1)
        meteor_object.movingmeteor(player1)
        drawboard(player1,enemy_object,money_object,meteor_object)

def drawboard(player1,enemy_object,money_object,meteor_object):
    gameboard.blit(space, (0, 0))
    gameboard.blit(player1.player_image, (player1.player_XY.x,player1.player_XY.y ))
    for bullet in player1.player_bullets:
        gameboard.blit(player1.playershootimage, (bullet.x, bullet.y))
    for enemy in enemy_object.enemylist:
        gameboard.blit(enemy_object.enemy1_image, (enemy.x, enemy.y))
    for bullet in enemy_object.enemybulletlist:
        gameboard.blit(enemy_object.enemy1_shot_image,(bullet.x,bullet.y))
    for bag in money_object.moneybaglist:
        gameboard.blit(money_object.money_image,(bag.x,bag.y))
    for meteor in meteor_object.meteorlist:
        gameboard.blit(meteor_object.meteor_image,(meteor.x,meteor.y))
    gameboard.blit(player1.set_life(), (770, 430))
    gameboard.blit(player1.set_money(),(770, 450))
    gameboard.blit(player1.set_kills(),(770,470))
    pygame.display.update()

def drawstore(store_object):
    gameboard.blit((store_object.store_image),(0,0))
    pygame.display.update()


def drawstoremassges(store_object):
    if store_object.massage1==1:
        gameboard.blit(space, (0, 0))
        gameboard.blit(store_object.massage,(200,200))
        pygame.display.update()
        time.sleep(2)
        store_object.massage1=0
        store_object.set_massage()
def drawlosemassge(player1):
    gameboard.blit(space, (0, 0))
    gameboard.blit(player1.lose_massage(), (300, 200))
    pygame.display.update()
    time.sleep(2)



if __name__ == '__main__':
    main()


# l = []
# for i in range(200):
#     x = int(50*math.sin(i*2*math.pi/1/(200)))
#     l.append(x+100)
# print(len(l))
# print(l)




def rol():
    list1=[]
    for bet in range(1,36):
        chance=bet/37
        reward=360-(bet*10)
        bet*10*(chance)