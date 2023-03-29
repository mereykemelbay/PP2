import pygame
import time

sagat=pygame.time.Clock()

pygame.init()

width=400
height=400
screen=pygame.display.set_mode((width, height))
done=False
white=[255,255,255]
screen.fill(white)
x=50
y=50
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y>20: y -= 20
    if pressed[pygame.K_DOWN] and y<height-20: y += 20
    if pressed[pygame.K_LEFT]and x>20: x -= 20
    if pressed[pygame.K_RIGHT] and x<width-20 : x += 20
    
    pygame.draw.circle(screen, (225, 0, 0), (x, y), 25)
    pygame.display.flip()
    sagat.tick(60)