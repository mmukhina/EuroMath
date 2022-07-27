import sys
import random
import pygame
from pygame.locals import *
import math

class Game():
    print(" ")
    print("  *****  Демонстрационная Игра  *****  ")
    print(" ")
    state = True
    
    pygame.init()
    width = 700
    height = 700
    pygame.display.set_caption("Демонстрационная Игра")
    screen = pygame.display.set_mode((width, height))

    red_square = pygame.image.load("images/player2.png")
    blue_square = pygame.image.load("images/player.png")
    
    screen.fill((255,255,255))
    
    pygame.display.update()

    count = 1

    print("Нажмите на экран, чтоб продолжить или повторить; Enter, чтобы завершить")

    while state:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if count == 1:
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
                    count += 1

                elif count == 2:
                    print(" ")
                    print("          Этап 2 ")

                    sidex = abs(x2 - x)
                    print("Сторона х = {}" .format(sidex))

                    sidey = abs(y2 - y)
                    print("Сторона у = {}" .format(sidey))
                   
                    print(" ")
                    count += 1

                elif count == 3:
                    print("          Этап 3 ")
                    hypsqt = (sidex * sidex) + (sidey * sidey )
                    hyp = math.sqrt(hypsqt)
                    print("Гипотенуза = {}" .format(hyp))
                    print(" ")
                    count += 1

                elif count == 4:
                    print("          Этап 4 ")
                    
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
                    count += 1

            elif count == 5:
                print("          Этап 5 ")

                if sidex != 0:
                    gradient = float(sidey) / float(sidex)
                else:
                    gradient = 0
                
                print("Градиент = {}" .format(gradient))
                print(" ")
                step = 0
                
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

                    count = 1

                print("")
                print("Нажмите на экран, чтоб продолжить или повторить; Enter, чтобы завершить")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    ex = Game()

