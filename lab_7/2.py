import pygame 
import os

pygame.init()

window = pygame.display.set_mode((500, 500)) 
pygame.display.set_caption("Music Player")

music = r'C:\merey\pp2\lab_7\music'
musicfiles = [os.path.join(music, f) for f in os.listdir(music) if f.endswith('.mp3')]

i = 0
pygame.mixer.music.load(musicfiles[i]) 
pygame.mixer.music.play()

prev_button = pygame.draw.polygon(window, (0, 255, 0), ((30, 425), (80, 400),(80, 450))) #green triangle
play_button = pygame.draw.rect(window, (255, 255, 0), (130, 400, 50, 50)) #yellow rectangle
pause_button = pygame.draw.circle(window, (0, 255, 255), (255, 425), 25) #blue circle
stop_button = pygame.draw.rect(window, (255, 0, 255), (330, 400, 50, 50)) #purple rectangle
next_button = pygame.draw.polygon(window, (0, 255, 0), ((480, 425), (430, 400),(430, 450)))  #green triangle


songs = len(os.listdir(r'C:\merey\pp2\lab_7\music'))

while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            if pause_button.collidepoint(event.pos): 
                pygame.mixer.music.pause() 
            elif play_button.collidepoint(event.pos): 
                pygame.mixer.music.unpause()
            elif stop_button.collidepoint(event.pos): 
                pygame.mixer.music.stop()
            elif next_button.collidepoint(event.pos):
                while i < songs:
                    pygame.mixer.music.load(musicfiles[i+1]) 
                    pygame.mixer.music.play()
                    i += 1
                    break
            elif prev_button.collidepoint(event.pos):
                while i > 0:
                    pygame.mixer.music.load(musicfiles[i-1]) 
                    pygame.mixer.music.play()
                    i -= 1
                    break
                   
                
    pygame.display.update()