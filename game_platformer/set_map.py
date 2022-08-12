import telnetlib
from turtle import title
import pygame

pygame.init()
WIDTH = 1200
HEIGHT = 1000
BLACK = (0,0,0)
WHITE = (255,255,255)
sun_bg = pygame.image.load('assest/sun.png')
sky_bg = pygame.image.load('assest/sky.png')
screen = pygame.display.set_mode((WIDTH,HEIGHT))
save_btn = pygame.image.load('assest/save_btn.png')
pygame.display.set_caption("Game funny")


clock = pygame.time.Clock()
run = True

tile_size = 50
dirt_size = 40

class Button():
    def __init__(self,x,y,img):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.click = False
        self.reset = False

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if(self.rect.collidepoint(mouse_pos)):
            if (pygame.mouse.get_pressed()[0] == 1) and self.click == False:
                print("Clicked")
                self.click = True
                self.reset = True
            #When you dont click 
            if( pygame.mouse.get_pressed()[0] == 0):
                self.click = False
                self.reset = False

        screen.blit(self.img,self.rect)
        return self.reset

dirt_img = pygame.image.load("assest/dirt.png")
dirt = pygame.transform.scale(dirt_img,(tile_size,tile_size))
grass_img = pygame.image.load("assest/grass.png")
grass = pygame.transform.scale(grass_img,(tile_size,tile_size))
lava_img = pygame.image.load("assest/lava.png")
lava = pygame.transform.scale(lava_img,(tile_size,tile_size))
blob_img = pygame.image.load("assest/blob.png")
blob = pygame.transform.scale(blob_img,(tile_size,tile_size))
exit_img = pygame.image.load("assest/exit.png")
exit = pygame.transform.scale(exit_img,(tile_size,tile_size))
imgs = [dirt, grass, lava, blob, exit]
btns = []
for i in range(len(imgs)):
    icon = Button(1000, 200 + 100*i, imgs[i])
    btns.append(icon)


def draw_gid():
    for line in range(0,int(WIDTH/tile_size)):
        pygame.draw.line(screen,WHITE,(0,line*tile_size),(WIDTH,line*tile_size),1)
        pygame.draw.line(screen,WHITE,(line*tile_size,0),(line*tile_size,HEIGHT),1)

def draw_element(col_count,row_count,tile,img):
    img = pygame.transform.scale(img[tile-1],(tile_size,tile_size))
    img_rect = img.get_rect()
    img_rect.x = tile_size * col_count
    img_rect.y = tile_size * row_count 
    #add to a list
    tile_img = (img, img_rect)
    return tile_img

class Button():
    def __init__(self,x,y,img):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.click = False
        self.reset = False

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if(self.rect.collidepoint(mouse_pos)):
            if (pygame.mouse.get_pressed()[0] == 1) and self.click == False:
                print("Clicked")
                self.click = True
                self.reset = True
            #When you dont click 
            if( pygame.mouse.get_pressed()[0] == 0):
                self.click = False
                self.reset = False

        screen.blit(self.img,self.rect)
        return self.reset

save = Button(1100, 200 , save_btn)

class World():
    def __init__(self,data):
        self.tile_list = []
        dirt_img = pygame.image.load("assest/dirt.png")
        grass_img = pygame.image.load("assest/grass.png")
        lava_img = pygame.image.load("assest/lava.png")
        blob_img = pygame.image.load("assest/blob.png")
        exit_img = pygame.image.load("assest/exit.png")
        img = [dirt_img, grass_img, lava_img, blob_img, exit_img]
        row_count = 0
        for row in data:
            col_count = 0 
            for tile in row:
                if tile == 1:
                    self.tile_list.append(draw_element(col_count,row_count,tile,img))
                if tile == 2:
                    self.tile_list.append(draw_element(col_count,row_count,tile,img))
                
                if tile == 3:
                    self.tile_list.append(draw_element(col_count,row_count,tile,img))
                
                if tile == 4:
                    self.tile_list.append(draw_element(col_count,row_count,tile,img))
                
                if tile == 5:
                    self.tile_list.append(draw_element(col_count,row_count,tile,img))
                
                col_count+=1

            row_count+=1

    def draw(self):
        for i in range(len(self.tile_list)):
            screen.blit(self.tile_list[i][0],self.tile_list[i][1])


world_list = []
#create rows and columns
for row in range (20):
    world_list.append([])
    for column in range(20):
        world_list[row].append(0)
        

def create_world(img_i):  
        dirt_img = pygame.image.load("assest/dirt.png")
        dirt = pygame.transform.scale(dirt_img,(tile_size,tile_size))
        grass_img = pygame.image.load("assest/grass.png")
        grass = pygame.transform.scale(grass_img,(tile_size,tile_size))
        lava_img = pygame.image.load("assest/lava.png")
        lava = pygame.transform.scale(lava_img,(tile_size,tile_size))
        blob_img = pygame.image.load("assest/blob.png")
        blob = pygame.transform.scale(blob_img,(tile_size,tile_size))
        exit_img = pygame.image.load("assest/exit.png")
        exit = pygame.transform.scale(exit_img,(tile_size,tile_size))
        


        img = [dirt,grass,lava,lava,blob,exit]
        img_rect = img[img_i].get_rect()

        pos = pygame.mouse.get_pos()
        for row in range(20):
                if( tile_size*row <= pos[1] <= tile_size*(row+1)):
                    for column in range(20):
                        if( tile_size*column <= pos[0] <= tile_size*(column+1)):
                            world_list[row][column] = img_i+1
                        
        # world_data_set = World(world_list)
        # world_data_set.draw()


#only draw dirt

img_i = 0
font = pygame.font.SysFont('sans',40)
k = 2
text_level = font.render(f"Level {k}",False, (255,0,0))
while run:
    
    clock.tick(60) #60fps
    screen.blit(sky_bg,(0,0))
    screen.blit(sun_bg,(100,100))

    world_data_set = World(world_list)
    world_data_set.draw()
    draw_gid()
    screen.blit(text_level,((WIDTH-200)//2 , 200))
    
    for i in range(len(btns)):
        if btns[i].draw():
            img_i = i
        

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
        if(event.type == pygame.MOUSEBUTTONDOWN):
            create_world(img_i)       
        

    if save.draw():
        with open(f'level_{k}.txt',"w") as file:
            for i in range(len(world_list)):
                for k in range(len(world_list[i])):
                    file.writelines(str(world_list[i][k]) + " " )
                file.writelines("\n")
                        
               


    pygame.display.update()
pygame.quit()