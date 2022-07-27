#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import sys
import random
import pygame
import math
print(" ")
print("  *****  Демонстрационная Игра  *****  ")
print(" ")
question = raw_input('Напишите да, чтобы начать игру? ')
print(" ")
cancel = "run"
while 1:   
    if question != "да":
        answer = raw_input("Вы уверены, что хотите выйти? ")
        print(" ")
        if answer == "да ":
            pygame.quit()
        else:
            question = "да"
            answer = "нет"
     
    pygame.init()
    width = 700;
    height = 700
    pygame.display.set_caption("Демонстрационная Игра")
    screen = pygame.display.set_mode((width, height))
    background = pygame.display.set_mode()
    red_square = pygame.image.load("player2.bmp").convert_alpha(background)
    blue_square = pygame.image.load("player.bmp").convert_alpha(background)
    x = random.randint(0,620);
    y = random.randint(0,620);
    print(" ")
    print("          Этап 1 ")
    print("Координат x Cинего квадрата = {} " .format(x))
    print("Координат у Cинего квадрата = {} " .format(y))
    print(" ")
    x2 = random.randint(0,620);
    y2 = random.randint(0,620);
    print("Координат x Красного квадрата = {} " .format(x2))
    print("Координат у Красного квадрата = {} " .format(y2))
    screen.fill((255,255,255))
    screen.blit(blue_square,(x,y))
    screen.blit(red_square,(x2,y2))
    pygame.display.update()
    print(" ")

    stage2 = raw_input("          Этап 2 ")
    if stage2 == "":
        sidex = x2 - x
        if sidex > 0:
            print("Сторона х = {}" .format(sidex)) 
        else:
            sidex = x - x2
            print("Сторона х = {}" .format(sidex))
            
    sidey = y2 - y
    if sidey > 0:
        print("Сторона у = {}" .format(sidey))
    else:
        sidey = y - y2
        print("Сторона у = {}" .format(sidey))
    print(" ")

    stage3 = raw_input("          Этап 3 ")
    if stage3 == "":
        hypsqt = (sidex * sidex) + (sidey * sidey )
        hyp = math.sqrt(hypsqt)
        print("Гипотенуза = {}" .format(hyp))
    print(" ")

    stage4 = raw_input("          Этап 4 ")
    if stage4 == "":
        if y2 > y:
            if x2 > x:
                preangle = float(sidey) / float(sidex)
                angle = math.degrees(math.atan(preangle))
                bearing = 270 + angle
            elif x2 < x:
                preangle = float(sidey) / float(sidex)
                angle = math.degrees(math.atan(preangle))
                bearing = 90 - angle
            else:
                angle = 0
                bearing = 0
        elif y2 < y:
            if x2 > x:
                preangle = float(sidex) / float(sidey)
                angle = math.degrees(math.atan(preangle))
                bearing = 180 + angle
            elif x2 < x:
                preangle = float(sidex) / float(sidey)
                angle = math.degrees(math.atan(preangle))
                bearing = 90 + (90 - angle)
            else:
                angle = 0
                bearing = 180
        else:
            if x2 > x:
                angle = 0
                bearing = 270
            elif x2 < x:
                angle = 0
                bearing = 90
            else:
                angle = 0
                bearing = 0
                
    print("Угол = {}" .format(angle))
    print("Пеленг = {}" .format(bearing))
    print(" ")
            
    stage5 = raw_input("          Этап 5 ")

    if sidex != 0:
        gradient = float(sidey) / float(sidex)
    else:
        gradient = 0
    
    print("Градиент = {}" .format(gradient))
    print(" ")
    step = 0
    
    if stage5 == "":
        while (round(x2) != round(x)) or (round(y2) != round(y)):
            if x2 > x:
                step = 1
                if y2 > y:
                    x2 -= 1
                    y2 -= gradient
                elif y2 < y:
                    x2 -= 1
                    y2 += gradient
                else:
                    x2 -= 1
            elif x2 < x:
                step = 1
                if y2 >= y:
                    x2 += 1
                    y2 -= gradient
                elif y2 <= y:
                    x2 += 1
                    y2 += gradient
                else:
                    x2 += 1

            elif step == 0:
                if x2 == x:
                    if y2 > y:
                        y2 -= 1
                    elif y2 < y:
                        y2 += 1

            screen.fill((255,255,255))
            screen.blit(blue_square, (x,y))
            screen.blit(red_square, (x2,y2))
            pygame.display.update()
            print("X = {}          Y = {}" .format(x2, int(y2)))
        
              
    print(" ")
    print("Вы Победили!!!")
    print(" ")
    finalQ = raw_input("Хотите начать все сначала?")
    print(" ")
    print(" ")

    if finalQ != "да":
        pygame.quit()
        sys.exit()


pygame.quit()
