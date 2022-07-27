

print("  ***** Demonstration Game *****  ")
print(" ")
question = raw_input("Write 'start' to begin the game? ")
print(" ")
cancel = "run"
    
while 1:
        
    if question != "start":
        answer = raw_input("Are you sure you want to quit? ")
        print(" ")
        if answer == "yes":
            pygame.quit()
            
        else:
            question = "start"
            answer = "no"

    print(" ")
    print(" ")
    
    import pygame

    pygame.init()
    width = 700;
    height = 700
    pygame.display.set_caption("Demonstration game")
    screen = pygame.display.set_mode((width, height))
    background = pygame.display.set_mode()

    red_square = pygame.image.load("player.bmp").convert()
    blue_square = pygame.image.load("player2.bmp").convert_alpha(background)

    import random
    x = int(251);
    y = int(26);
    print("The x coordinate of Mr.RedSquare = {} " .format(x))
    print(" ")
    print("The y coordinate of Mr.RedSquare = {}" .format(y))
    print(" ")

    x2 = int(382);
    y2 = int(223);
    print("The x coordinate of Mr.BlueSquare = {} " .format(x2))
    print(" ")
    print("The y coordinate of Mr.BlueSquare = {} " .format(y2))
    print(" ")

    screen.fill((255,255,255))

    screen.blit(red_square,(x,y))
    screen.blit(blue_square,(x2,y2))

    pygame.display.update()

    print(" ")
    print(" ")

    import math

    stage1 = raw_input("          Stage 1 ")
    print(" ")
    if stage1 == "":
        sidex = x2 - x
        if sidex > 0:
            print("Side x is = {}" .format(sidex))
            
        else:
            sidex = x - x2
            print("Side x is = {}" .format(sidex))

    print(" ")

    sidey = y2 - y
    if sidey > 0:
        print("Side y is = {}" .format(sidey))
        
    else:
        sidey = y - y2
        print("Side y is = {}" .format(sidey))

    print(" ")
    print(" ")


    stage2 = raw_input("          Stage 2 ")
    print(" ")
    if stage2 == "":
        hypsqt = (sidex * sidex) + (sidey * sidey )
        hyp = math.sqrt(hypsqt)
        print("The hypoteneus = {}" .format(hyp))

        
    print(" ")
    print(" ")


    stage3 = raw_input("          Stage3 ")
    print(" ")
    if stage3 == "":
        if y2 > y:
            if x2 > x:
                preangle = float(sidey) / float(sidex)
            elif x2 < x:
                preangle = float(sidey) / float(sidex)
        elif y2 < y:
            if x2 > x:
                preangle = float(sidex) / float(sidey)
            elif x2 < x:
                preangle = float(sidex) / float(sidey)


    angle = math.degrees(math.atan(preangle))
    print("The angle = {}" .format(angle))
    print(" ")
    print(" ")
    
    stage4 = raw_input("          Stage 4 ")
    print(" ")
    if stage4 == "":
        if y2 > y:
            if x2 > x:
                bearing = angle

            if x2 < x:
                bearing = 360 - angle

        if y2 < y:
            if x2 > x:
                bearing = 180 - angle

            if x2 < x:
                bearing = 180 + angle
        

    print("The bearing = {}" .format(bearing))

    print(" ")
    print(" ")
            

    stage5 = raw_input("          Stage 5 ")
    print(" ")

    gradient = float(sidey) / float(sidex)
    print("The gradient = {}" .format(gradient))
    print(" ")
    
    if stage5 == "":
        while x != x2 and y != y2 :
            if x2 > x:
                if y2 > y:
                    x2 -= 1
                    y2 -= gradient
                elif y2 < y:
                    x2 -= 1
                    y2 += gradient
            elif x2 < x:
                if y2 > y:
                    x2 += 1
                    y2 -= gradient
                elif y2 < y:
                    x2 += 1
                    y2 += gradient

            screen.fill((255,255,255))
            screen.blit(red_square, (x,y))
            screen.blit(blue_square, (x2,y2))
            pygame.display.update()
            print("X = {}          Y = {}" .format(x2,int(y2)))
        
            

    print(" ")
    print(" ")
    
    print("You Won!!!")
    print(" ")

    finalQ = raw_input("Would you like to start again? ")

    print(" ")
    print(" ")
    print(" ")

    if finalQ != "yes":
        pygame.quit()
        sys.exit()


pygame.quit()
