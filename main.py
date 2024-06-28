import pygame
from settings import *
import random
import time

random.seed(0)

def draw_background():
    screen.fill(BACKGROUND_COLOR)

def gen_buttons():
    x,y,w,h=20,20,60,60
    buttons1=[]
    for i in range(5):
        buttons1.append({'name': names[i], 'coordinates': (x,y,w,h)})
        y=y+h+10
    x,y,w,h=530,20,60,60
    buttons2=[]
    for i in range(5):
        buttons2.append({'name': names[i], 'coordinates': (x,y,w,h)})
        y=y+h+10
    return(buttons1, buttons2)

def draw_buttons():
    
    for b in buttons1:
        pygame.draw.rect(screen, GRAY, b['coordinates'])
        pygame.draw.rect(screen, BLACK, b['coordinates'], 3)
        text=font.render(b['name'], True, BLACK)
        screen.blit(text, (b['coordinates'][0]+10,b['coordinates'][1]+3))
    for b in buttons2:
        pygame.draw.rect(screen, GRAY, b['coordinates'])
        pygame.draw.rect(screen, BLACK, b['coordinates'], 3)
        text=font.render(b['name'], True, BLACK)
        screen.blit(text, (b['coordinates'][0]+10,b['coordinates'][1]+3))
    
    
    # if selected!=-1:
    #     pygame.draw.rect(screen, PINK, buttons[selected]['coordinates'])
    #     pygame.draw.rect(screen, BLACK, buttons[selected]['coordinates'], 3)
    #     text=font.render(buttons[selected]['name'], True, BLACK)
    #     screen.blit(text, (buttons[selected]['coordinates'][0]+10,buttons[selected]['coordinates'][1]+3))

def number_player():
    draw_background()
    font = pygame.font.SysFont('arial', 40)
    text=font.render('How many player?', True, BLUE)
    screen.blit(text, (100,100))
    

if __name__=='__main__':

    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption('Rock, paper, scissor, spock lizzard♥')
    font = pygame.font.SysFont('arial', 20)

    #28, 40, 56, 80
    #20, 14, 10, 7


    draw_background()
    buttons1,buttons2=gen_buttons()
    draw_buttons()
    # number_player()
    selected1=-1
    selected2=-1


    run  = True

    number=0

    while run:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN or pygame.mouse.get_pressed()[0]:
                x,y=pygame.mouse.get_pos()
                for i in range(len(buttons1)):
                    if x>=buttons1[i]['coordinates'][0] and x<=buttons1[i]['coordinates'][0]+buttons1[i]['coordinates'][2] and y>=buttons1[i]['coordinates'][1] and y<=buttons1[i]['coordinates'][1]+buttons1[i]['coordinates'][3]:
                        print("playr1 "+str(i))
                for i in range(len(buttons2)):
                    if x>=buttons2[i]['coordinates'][0] and x<=buttons2[i]['coordinates'][0]+buttons2[i]['coordinates'][2] and y>=buttons2[i]['coordinates'][1] and y<=buttons2[i]['coordinates'][1]+buttons2[i]['coordinates'][3]:
                        print("playr2 "+str(i))


        pygame.display.flip()
        clock.tick(30)
        

    pygame.quit()