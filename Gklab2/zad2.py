import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")


def Figura():
    pygame.draw.circle(win, (0, 0, 0), (300, 300), 180)
    pygame.draw.polygon(win, (255, 255, 0), [(200, 200), (400, 200), (400, 400), (200,400)])

   




run = True
while run:
    win.fill((255, 255, 255))
    Figura()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
         
        
    
    pygame.display.update()

pygame.quit()