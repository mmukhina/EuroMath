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
    blue_square = pygame.image.load("player.bmp").convert_alpha(background)
    x1 = 0;
    y1 = 620;
    
    screen.fill((255,255,255))
    screen.blit(blue_square,(x1,y1))
    pygame.display.update()
    print(" ")
    
    
    constant = -0.005
    constant2 = math.sqrt(60000)

    x2 = constant2 * - 1
    y2 = 0

    constant3 = (constant2 * 2) / 122

    stage6 = raw_input("          Этап 6 ")
    print("Координат x Cинего квадрата = {} " .format(x1))
    print("Координат у Cинего квадрата = {} " .format(y1))
    if stage6 == "":
        while x2 <= round(constant2):
            square = x2 * x2
            y2 =  float((constant * square) + 300)
            
            x1 = x2 + constant2
            y1 = 620 - y2
            print("X = {}          Y = {}" .format(int(x1), int(y1)))
            screen.fill((255,255,255))
            screen.blit(blue_square,(x1,y1))
            pygame.display.update()
            x2 += constant3

        


    

                          
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
