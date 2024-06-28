import pygame
from settings import *
import random
import time


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
    
    
    if selected1!=-1:
        pygame.draw.rect(screen, PINK, buttons1[selected1]['coordinates'])
        pygame.draw.rect(screen, BLACK, buttons1[selected1]['coordinates'], 3)
        text=font.render(buttons1[selected1]['name'], True, BLACK)
        screen.blit(text, (buttons1[selected1]['coordinates'][0]+10,buttons1[selected1]['coordinates'][1]+3))

    if selected2!=-1:
        pygame.draw.rect(screen, PINK, buttons2[selected2]['coordinates'])
        pygame.draw.rect(screen, BLACK, buttons2[selected2]['coordinates'], 3)
        text=font.render(buttons2[selected2]['name'], True, BLACK)
        screen.blit(text, (buttons2[selected2]['coordinates'][0]+10,buttons2[selected2]['coordinates'][1]+3))
    
    pygame.display.flip()
    
def winner(selected1, selected2):
    c1=names[selected1]
    c2=names[selected2]
    for i in range(len(wins)):
        if wins[i][0]==c1 and wins[i][2]==c2:
            return(1, wins[i])
        if wins[i][0]==c2 and wins[i][2]==c1:
            return(2, wins[i])
    return(0, 'Draw')
        
def display_sentence(sentence):
    pygame.draw.rect(screen, BACKGROUND_COLOR, (190,190,250,100))
    if not(isinstance(sentence, str)):
        sentence=' '.join(sentence)
    font = pygame.font.SysFont('arial', 20)
    text=font.render(sentence, True, WHITE)
    screen.blit(text, (200,200))

def display_scores():
    font = pygame.font.SysFont('arial', 50)
    text=font.render(str(score[0]), True, WHITE)
    screen.blit(text, (250,20))
    text=font.render('|', True, WHITE)
    screen.blit(text, (300,15))
    text=font.render(str(score[1]), True, WHITE)
    screen.blit(text, (335,20))




if __name__=='__main__':

    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), flags, vsync=1)
    pygame.display.set_caption('Rock, paper, scissor, spock lizzard♥')
    font = pygame.font.SysFont('arial', 20)

    #28, 40, 56, 80
    #20, 14, 10, 7

    selected1=-1
    selected2=-1
    score=(0,0)
    draw_background()
    buttons1,buttons2=gen_buttons()
    draw_buttons()
    display_scores()
    # number_player()



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
                        selected1=i
                        selected2=random.randint(0,4)
                        draw_buttons()
                        print(selected1,selected2)
                        w, sentence = winner(selected1, selected2)
                        display_sentence(sentence)
                        selected1=-1
                        selected2=-1
                        break

        pygame.display.flip()
        clock.tick(30)
        

    pygame.quit()