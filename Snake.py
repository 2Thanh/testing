import pygame
import time
from random import randint
WIDTH = 600
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
MAROON = (128, 0, 0)
BROWN = (165, 42, 42)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
running = True

snake = [[0, 1], [1, 1], [2, 1], [3, 1], [4,1] , [5,1]]
tmp = [0, 0]
direction = "None"
apple = [0,0]
eat = False
score = 0

def move(x,y):
    block_new = [snake[-1][0] + x, snake[-1][1] +y]
    if block_new not in snake:
        time.sleep(0.07)
        snake.append(block_new)
        snake.pop(0)
    else:
        if (block_new == snake[-2]):
            block_new = [snake[-1][0] - x, snake[-1][1] +y]
            time.sleep(0.07)
            snake.append(block_new)
            snake.pop(0)
        
while running:
    clock.tick(60)  # fps 60
    screen.fill(BLACK)
    # Draw grid
    for i in range(20):
        pygame.draw.line(screen, RED, (30*i, 0), (30*i, 600))
        pygame.draw.line(screen, RED, (0, 30*i), (600, 30*i))

    for k in range(1,len(snake)):
        pygame.draw.rect(screen, YELLOW, (snake[k][0]*30, snake[k][1]*30, 30, 30))
    pygame.draw.rect(screen, BLUE, (snake[-1][0]*30, snake[-1][1]*30, 30, 30))

    #apple random pos
    if not eat:
        apple = [30*randint(0,15),30*randint(0,15)]
        eat = True
    pygame.draw.rect(screen,RED,(apple[0],apple[1],30,30))

    
    if (direction == "right"):
        if (0<snake[-1][0]*30<600 and 0<snake[-1][1]*30<=600):
            move(1,0)
        
    if (direction == "left"):
        if (0<snake[-1][0]*30<600 and 0<snake[-1][1]*30<=600):
            move(-1,0)

    if (direction == "up"):
        if (0<snake[-1][0]*30<600 and 0<snake[-1][1]*30<=600):
            move(0,-1)
   
    if (direction == "down"):
        if (0<snake[-1][0]*30<600 and 0<snake[-1][1]*30<=600):
            move(0,1)

    if (apple[0] == snake[-1][0]*30 and apple[1] == snake[-1][1]*30):
        score+=1
        eat = False
        if not eat:
            print("XX")
            snake.insert(0,[snake[0][0] , snake[0][1] ])
            print(len(snake))
       

    #Score
    font = pygame.font.SysFont('sans' ,40)
    text = font.render("Score: "+ str(score) , True , GREEN)
    screen.blit(text,(450,10))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_RIGHT):
                direction = "right"
                
            if(event.key == pygame.K_LEFT):
              
                direction = "left"
                
            if(event.key == pygame.K_DOWN):
                direction = "down"
                
                
            if(event.key == pygame.K_UP):
                direction = "up"

    pygame.display.flip()
pygame.quit()
