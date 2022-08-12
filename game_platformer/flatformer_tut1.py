
import pygame
import time

pygame.init()
WIDTH = 1000
HEIGHT = 1000
BLACK = (0,0,0)
WHITE = (255,255,255)

#Set image 
sun_bg = pygame.image.load('assest/sun.png')
sky_bg = pygame.image.load('assest/sky.png')
restart_img = pygame.image.load('assest/restart_btn.png')
start_img = pygame.image.load('assest/start_btn.png')
exit_img = pygame.image.load('assest/exit_btn.png')
exit_door_img = pygame.image.load("assest/exit.png")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game funny")

clock = pygame.time.Clock()
run = True

tile_size = 50
dirt_size = 40
game_over = 0

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
                
                self.click = True
                self.reset = True
            #When you dont click 
            if( pygame.mouse.get_pressed()[0] == 0):
                self.click = False
                self.reset = False

        screen.blit(self.img,self.rect)
        return self.reset

restart_btn = Button(WIDTH //2 - 50 ,HEIGHT //2, restart_img)
start_btn = Button(WIDTH // 2 - 350, HEIGHT // 2,start_img)
exit_btn = Button(WIDTH // 2 + 150, HEIGHT // 2,exit_img)

class Enermy(pygame.sprite.Sprite): #This is the already class for game include draw and update,....
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assest/blob.png")
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.move_direction = 1
        self.direction = 1

    def update(self):
        self.direction+=1
        self.rect.x += self.move_direction
        #The enermies're too fast
        if abs(self.direction) > 50:
            self.direction = -50
            self.move_direction *= -1

blob_group = pygame.sprite.Group()

class Lava(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("assest/lava.png")
        self.image = pygame.transform.scale(image,(tile_size,tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 

lava_group = pygame.sprite.Group()

class Exit(pygame.sprite.Sprite):
    def __init__ (self,x,y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("assest/exit.png")
        self.image = pygame.transform.scale(image,(tile_size,tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
exit_group = pygame.sprite.Group()

class World():
    def __init__(self,data):
        self.tile_list = []
        dirt_img = pygame.image.load("assest/dirt.png")
        grass_img = pygame.image.load("assest/grass.png")
        lava_img = pygame.image.load("assest/lava.png")
        img = [dirt_img,grass_img]
        row_count = 0
        for row in data:
            col_count = 0 
            for tile in row:
                if tile ==1:
                    self.tile_list.append(draw_element(col_count,row_count,tile,img))
                if tile ==2:
                    self.tile_list.append(draw_element(col_count,row_count,tile,img))
                if tile ==3:
                    lava = Lava(col_count * tile_size, row_count * tile_size)
                    lava_group.add(lava)
                    #    self.tile_list.append(draw_element(col_count,row_count,tile,img))
                if tile == 4:
                    blob = Enermy(col_count * tile_size, row_count * tile_size +15)
                    blob_group.add(blob)
                if tile == 5:
                    exit_door = Exit(col_count * tile_size , row_count * tile_size )
                    exit_group.add(exit_door)
                col_count+=1

            row_count+=1

    def draw(self):
        for i in range(len(self.tile_list)):
            screen.blit(self.tile_list[i][0],self.tile_list[i][1])


# world_data = [

level = 3
world_data = []
for i in range(20):
    world_data.append([])

with open(f'level_{level}.txt','r') as file:
    for row in range (len(world_data)):
        world_data[row] = file.readline().split(" ")
        world_data[row].remove("\n")

for i in range(20):
    for k in range(20):
        world_data[i][k] = int(world_data[i][k])
world = World(world_data)
animation_i=0
counter =0




def animation():
    global animation_i,counter
    counter +=4
    if counter > 20:
        counter = 0
        animation_i += 1
        if animation_i > 3:
            animation_i = 0
    #if you do that it'll not delay like time.sleep and more smooth
    return animation_i
class Player():
    def __init__(self,x,y):
        img1 = pygame.image.load('assest/guy1.png')
        img2 = pygame.image.load('assest/guy2.png')
        img3 = pygame.image.load('assest/guy3.png')
        img4 = pygame.image.load('assest/guy4.png')

        dead = pygame.image.load('assest/ghost.png')

        img_right = [img1,img2, img3, img4]
        for i in range(len(img_right)):
            img_right[i] = pygame.transform.scale(img_right[i],(40,80))


        img_left = [img1,img2, img3, img4]
        for i in range(len(img_left)):
            img_left[i] = pygame.transform.scale(img_left[i],(40,80))
            img_left[i] = pygame.transform.flip(img_left[i],True,False)


        self.defalt_animation = 0 
        self.dead_img = dead
        self.img = [img_right,img_left]
        self.rect = self.img[self.defalt_animation][0].get_rect()
        self.width = self.img[0][0].get_width()
        self.height = self.img[0][0].get_height()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0 
        self.jumped = False
        
    def update(self):
        global game_over,level,world
        dx = 0
        dy = 0
        if game_over == 0:
            #move player
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] :
                i = animation()
                screen.blit(self.img[1][i],(self.rect.x,self.rect.y))
                self.defalt_animation = 1
                dx -= 5

            elif key[pygame.K_RIGHT]:
                i = animation()
                screen.blit(self.img[0][i],(self.rect.x,self.rect.y))
                self.defalt_animation = 0 
                dx += 5
        
            elif key[pygame.K_SPACE] and self.jumped == False:
                self.vel_y = -15
                self.jumped = True
            
            else:
                screen.blit(self.img[self.defalt_animation][0],(self.rect))
            
            self.vel_y += 1
            if self.vel_y > 10 :
                self.vel_y = 10
            
            dy += self.vel_y
            
            #update player coordinates
                
            #Check collition
            pygame.draw.rect(screen,(255,255,255),self.rect,2)
            for i in range (0,len(world.tile_list)):
                try :
                    if (world.tile_list[i][1].colliderect(self.rect.x +dx ,self.rect.y,self.width,self.height)):
                        dx = 0
                        # print(len(world.tile_list))
                        # print(i)
                except:
                    print(len(world.tile_list))
                    print(i)


                if( world.tile_list[i][1].colliderect(self.rect.x,self.rect.y + dy,self.width,self.height)):
                    #When the character is jumping (vel_y >0 )
                    if (self.vel_y < 0):
                        #dy equal to distance between bottom of dirt MINUS left-top of charactor
                        dy = world.tile_list[i][1].bottom - self.rect.top
                        #print(dy)
                        self.vel_y = 0
                        
                    elif(self.vel_y >= 0):
                        #Opposite with that condition 
                        dy = world.tile_list[i][1].top - self.rect.bottom
                        #print(dy) # 0
                        self.vel_y = 0
                        self.jumped = False 
                
                if pygame.sprite.spritecollide(self,blob_group,False):
                        enermies = pygame.sprite.spritecollide(self,blob_group,False)
                        for enermy in enermies:
                            if (enermy.rect.top -25 <= self.rect.bottom <= enermy.rect.top +25):
                                enermy.kill()
                                
                            else:
                                game_over = -1
                            

                    
                if pygame.sprite.spritecollide(self,lava_group,False):
                    game_over = -1
                    
                if pygame.sprite.spritecollide(self,exit_group,False):
                    #Reset the level
                    if level <4:
                        level+=1
                    else:
                        level =1
                    blob_group.empty()
                    lava_group.empty()
                    exit_group.empty()
                    world_data = []
                    self.rect.x = 100
                    self.rect.y = HEIGHT -300
                    self.defalt_animation = 0
                    world = []
                    for i in range(20):
                        world_data.append([])

                    with open(f'level_{level}.txt','r') as file:
                        for row in range (len(world_data)):
                            world_data[row] = file.readline().split(" ")
                            world_data[row].remove("\n")

                        for i in range(20):
                            for k in range(20):
                                world_data[i][k] = int(world_data[i][k])
                    world = World(world_data)
                    

        else:
                screen.blit(self.dead_img,(self.rect))
                if self.rect.y >200:
                    dy -= 5
                else:   
                    if (restart_btn.draw()): 
                        
                        self.rect.x = 100
                        self.rect.y = HEIGHT -300
                        self.defalt_animation = 0
                        restart_btn.reset = False
                        game_over = 0

                
        
        self.rect.x += dx
        self.rect.y += dy


                    
                    
        

player = Player(100,HEIGHT - 300)

main_menu = True
while run:

    clock.tick(60) #60fps
    screen.blit(sky_bg,(0,0))
    screen.blit(sun_bg,(100,100))
    if main_menu == True:
      
        if exit_btn.draw():
            run = False
        if start_btn.draw():
            main_menu = False
    else:       
        
        world.draw()
        draw_gid()
        exit_group.draw(screen)
        
        blob_group.draw(screen)
        blob_group.update()
        lava_group.draw(screen)
        player.update()
        

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False
            

    pygame.display.update()
pygame.quit()