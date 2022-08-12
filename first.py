from turtle import back
import pygame
from random import randint
WHITE = (255,255,255)
BLUE = (0,0,255)
pygame.init()
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Hello")
running = True
BLACK = (0,0,0)
RED = (255,0,0)
clock = pygame.time.Clock()
rect_x = 50
rect_y = 50
background = WHITE
movement = [0,0]
font = pygame.font.SysFont('sans',30)
text = font.render("Random",True, BLACK)
text_box =text.get_rect()
random_pos = (50,50)
circle_color = RED
def draw_underline(pos,text_box):
    pygame.draw.line(screen,BLUE,(pos[0],pos[1]+text_box[3]+1),(pos[0]+text_box[2],pos[1]+text_box[3]+1),2)

while running  :
        clock.tick(60)
        screen.fill(background)
        pygame.draw.rect(screen,WHITE,(random_pos[0],random_pos[1],text_box[2], text_box[3]))
        screen.blit(text,random_pos)
        rect_x += movement[0]
        rect_y += movement[1]
        mouse = pygame.mouse.get_pos()
        mouse_x = mouse[0]
        mouse_y = mouse[1]

        #draw a circle
        pygame.draw.circle(screen,circle_color,(50,400),20)
        #change color when click that circle 
        if(mouse_x < random_pos[0]+text_box[2] and mouse_x > random_pos[0] and mouse_y < random_pos[1] + text_box[3] and mouse_y > random_pos[1]):
                        text = font.render("Random",True, BLUE)
                        #pygame.draw.line(screen,BLUE,(random_pos[0],random_pos[1]+text_box[3]+1),(random_pos[0]+text_box[2],random_pos[1]+text_box[3]+1),3)
                        draw_underline(random_pos,text_box)
        else:
            text = font.render("Random",True, BLACK)
        for event in pygame.event.get():
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1):
                    if(mouse_x < random_pos[0]+text_box[2] and mouse_x > random_pos[0] and mouse_y < random_pos[1] + text_box[3] and mouse_y > random_pos[1]):
                        circle_color = (randint(0,255),randint(0,255),randint(2,255))
                        print("This is Rectangle.")

            if(event.type == pygame.QUIT):
                running = False
        
        pygame.display.flip()

pygame.quit()