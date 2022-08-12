import webbrowser
import pygame

#Load video
class Video:
    def __init__ (self, title, link):
        self.title = title
        self.link = link
        self.seen = False
    def open(self):
        self.seen = True
        print("Open: "+ self.title)
        webbrowser.open(self.link)

class Play_list:
    def __init__ (self, name, description, rating, videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos

def read_videos_from_txt(file):
        videos = []
        total = int(file.readline()) #number of videos
        for i in range(total):
            title = file.readline()
            link = file.readline()
            video = Video(title, link)
            videos.append(video)
        return videos

def read_playlist_from_text(file):
    playlist_name = file.readline()
    playlist_description = file.readline()
    playlist_rating = file.readline()
    playlist_videos = read_videos_from_txt(file)
    playlist = Play_list(playlist_name, playlist_description, playlist_rating, playlist_videos)
    return playlist


def read_playlists_from_text():#open multiple playlist
    playlists = []
    with open("Play_list.txt","r") as file:
        total = int(file.readline()) #number of playlists
        for i in range (total):
            playlist = read_playlist_from_text(file)
            playlists.append(playlist)
    return playlists


WIDTH = 600
HEIGHT = 400
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE =(0,0,255)

class TextButton:
    def __init__ (self , text , position, color):
        self.text = text
        self.position = position

        self.color = color
        self.font = pygame.font.SysFont('sans' ,20)
        self.text_font = self.font.render(self.text , True , self.color)
        self.text_box = self.text_font.get_rect() #text box become a atribute of Class
    def draw_rect(self):
        #Draw text
        #font = pygame.font.SysFont('sans' ,20)
        #text = font.render(self.text , True , self.color)
        #self.text_box = text.get_rect() #text box become a atribute of Class
        #Is mouse on text
        if TextButton.is_mouse_on_text(self):
            pygame.draw.line(screen,BLUE,(self.position[0],self.position[1]+self.text_box[3]+1),(self.position[0]+self.text_box[2],self.position[1]+self.text_box[3]+1),2)
            text = self.font.render(self.text , True , BLUE)
        else:
            text = self.font.render(self.text , True , self.color)
        screen.blit(text,self.position)


    def is_mouse_on_text(self):
        mouse = pygame.mouse.get_pos()

        if(mouse[0] < self.position[0]+self.text_box[2] and mouse[0] > self.position[0] and mouse[1] < self.position[1] + self.text_box[3] and mouse[1] > self.position[1]):   
            return True
        else:
            return False


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Play Music")
running = True
clock = pygame.time.Clock()

#Create Text Button
playlists = read_playlists_from_text()
playlists_btn_list = []

#playlist name
for i in range(len(playlists)):
    playlist_name_bt = TextButton(playlists[i].name.rstrip(), (30,50+50*i), BLACK) #remove new line\
    playlists_btn_list.append(playlist_name_bt)

#Playlist videos
videos_btn_list = []
def draw_playlist(i):
    global videos_btn_list
    playlist =playlists[i]
    for i in range(len(playlist.videos)):
        #videos_btn_list.append(playlist.videos[i])
        video_btn = TextButton(str(i+1)+"."+playlist.videos[i].title.rstrip(),(250,50+50*(i)),BLACK)
        videos_btn_list.append(video_btn)

playlist_choice = None
while running:
    clock.tick(60) #60fps
    screen.fill(WHITE)
    playlist_name_bt.draw_rect()
    for playlist_btn in playlists_btn_list:
        playlist_btn.draw_rect()

    for video_button in videos_btn_list:
        video_button.draw_rect()

    for event in pygame.event.get():
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(event.button ==1 ):
                
                for i in range(len(playlists_btn_list)):
                    if(playlists_btn_list[i].is_mouse_on_text()):
                        playlist_choice = i
                        videos_btn_list = [] # Renew video and redraw ag
                        draw_playlist(i) 

                if (playlist_choice!= None):
                    #print(len(videos_btn_list))
                    for i in range(len(videos_btn_list)):
                        if (videos_btn_list[i].is_mouse_on_text()):         
                            playlists[playlist_choice].videos[i].open()      
                            videos_btn_list[i].color = RED

        if(event.type == pygame.QUIT):
            running = False

    pygame.display.flip()

pygame.quit()
