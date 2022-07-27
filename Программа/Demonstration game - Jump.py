import sys
import random
import pygame
from pygame.locals import *
import math


class Game():
    def __init__(self): 
        print(" ")
        print("  *****  Демонстрационная Игра  *****  ")
        print(" ")
        state = True
        
        pygame.init()
        width = 800
        height = 800
        pygame.display.set_caption("Демонстрационная Игра")
        self.screen = pygame.display.set_mode((width, height))
        self.image_back = pygame.image.load("images/background2.jpg")
        self.screen.blit(self.image_back, (0,0))

        run1 = pygame.image.load("images/run1.png")
        run2 = pygame.image.load("images/run2.png")
        run3 = pygame.image.load("images/run3.png")
        run4 = pygame.image.load("images/run4.png")
        run5 = pygame.image.load("images/run5.png")
        run6 = pygame.image.load("images/run6.png")
        run7 = pygame.image.load("images/run7.png")
        run8 = pygame.image.load("images/run8.png")
        run9 = pygame.image.load("images/run9.png")
        run10 = pygame.image.load("images/run10.png")

        jump = pygame.image.load("images/jump.png")

        image = [run1, run2, run3, run4, run5, run6, run7, run8, run9, run10]

        pygame.display.update()

        print("Нажмите на экран, чтоб продолжить или повторить; Enter, чтобы завершить")

        while state:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    x1 = 0
                    y1 = 600
                    self.screen.blit(run1,[x1,y1])
                    pygame.display.update()
                    
                    print(" ")
                    
                    constant = -0.0075
                    constant2 = math.sqrt(40000)

                    x2 = (constant2 * - 1)
                    y2 = 0

                    constant3 = (constant2 * 2) / 100
                    count = 0
                    num = 0

                    while x1 != 120:
                        if num != 9:
                            num += 1
                        else:
                            num = 0

                        x1 += 7.5
                        self.running(image, num, x1, y1)
                        
                    while x2 <= round(constant2):
                        square = x2 * x2
                        y2 =  float((constant * square) + 300)
                        
                        x1 = x2 + constant2 + 120
                        y1 = 600 - y2
                        print("X = {}          Y = {}" .format(int(x1), int(y1)))
                        self.screen.blit(self.image_back,(0,0))
                        self.screen.blit(jump,(x1,y1))
                        pygame.display.update()
                        x2 += constant3
                        pygame.time.delay(5)

                    while x1 < 640:
                        if num != 9:
                            num += 1
                        else:
                            num = 0

                        x1 += 7.5
                        self.running(image, num, x1, y1)
                    
                    
                    self.screen.blit(self.image_back,(0,0))
                    self.screen.blit(run1,(x1,y1))
                    pygame.display.update()
                    
                    print("")
                    print("Нажмите на экран, чтоб продолжить или повторить; Enter, чтобы завершить")

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def running(self, image, num, x1, y1):
        self.screen.blit(self.image_back,(0,0))
        self.screen.blit(image[num],(x1,y1))
        pygame.display.update()
        print("X = {}          Y = {}" .format(int(x1), int(y1)))
        pygame.time.delay(40)


if __name__ == '__main__':
    ex = Game()

