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
    width = 800;
    height = 800
    pygame.display.set_caption("Демонстрационная Игра")
    screen = pygame.display.set_mode((width, height))
    background = pygame.display.set_mode()
    image_back = pygame.image.load("background2.bmp").convert_alpha(background)
    
    run1 = pygame.image.load("run1.bmp").convert_alpha(background)
    run2 = pygame.image.load("run2.bmp").convert_alpha(background)
    run3 = pygame.image.load("run3.bmp").convert_alpha(background)
    run4 = pygame.image.load("run4.bmp").convert_alpha(background)
    run5 = pygame.image.load("run5.bmp").convert_alpha(background)
    run6 = pygame.image.load("run6.bmp").convert_alpha(background)
    run7 = pygame.image.load("run7.bmp").convert_alpha(background)
    run8 = pygame.image.load("run8.bmp").convert_alpha(background)
    run9 = pygame.image.load("run9.bmp").convert_alpha(background)
    run10 = pygame.image.load("run10.bmp").convert_alpha(background)

    jump = pygame.image.load("jump.bmp").convert_alpha(background)
   
    image = [run1, run2, run3, run4, run5, run6, run7, run8, run9, run10]

    x1 = 0;
    y1 = 600;
    

        

    
    
    screen.blit(image_back,(0,0))
    screen.blit(run1,(x1,y1))
    pygame.display.update()
    print(" ")
    
    
    constant = -0.0075
    constant2 = math.sqrt(40000)

    x2 = (constant2 * - 1)
    y2 = 0

    constant3 = (constant2 * 2) / 100
    count = 0
    num = 0

    def running(image, num, x1):
        screen.blit(image_back,(0,0))
        screen.blit(image[num],(x1,y1))
        pygame.display.update()
        
        pygame.time.delay(100)
    
    while x1 != 120:
        if num != 9:
            num += 1
        else:
            num = 0

        x1 += 7.5
        running(image, num, x1)
    

    print("X = {}          Y = {}" .format(int(x1), int(y1)))
    
    while x2 <= round(constant2):
        square = x2 * x2
        y2 =  float((constant * square) + 300)
        
        x1 = x2 + constant2 + 120
        y1 = 600 - y2
        print("X = {}          Y = {}" .format(int(x1), int(y1)))
        screen.blit(image_back,(0,0))
        screen.blit(jump,(x1,y1))
        pygame.display.update()
        x2 += constant3


    while x1 < 640:
        if num != 9:
            num += 1
        else:
            num = 0

        x1 += 7.5
        running(image, num, x1)
    
    
    screen.blit(image_back,(0,0))
    screen.blit(run1,(x1,y1))
    pygame.display.update()
    


    

    print(" ")                  
    finalQ = raw_input("Хотите начать все сначала?")
    print(" ")
    print(" ")

    if finalQ != "да":
        pygame.quit()
        sys.exit()


pygame.quit()
