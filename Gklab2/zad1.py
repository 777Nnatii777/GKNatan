import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie 2 grafika komputerowa")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
NIEBIESKI = (0, 0, 255)
BIALI = (255, 255, 255)

def Nar13Kat(color, x=300, y=300, radius=150, scale_x=1, scale_y=1, kat=0, skoss_x=0):
    wieszcholki = []
    for i in range(13):
        angle = 2 * math.pi * i / 13  

        local_x = radius * math.cos(angle) * scale_x
        local_y = radius * math.sin(angle) * scale_y

        rotated_x = local_x * math.cos(kat) - local_y * math.sin(kat)
        rotated_y = local_x * math.sin(kat) + local_y * math.cos(kat)

        rotated_x += skoss_x * rotated_y

        vx = x + rotated_x
        vy = y + rotated_y

        wieszcholki.append((vx, vy))
    
    pygame.draw.polygon(win, color, wieszcholki)
 

    size = radius // 3


    kat_arrow = kat - math.pi / 2
    arrow_vertices = [
        (x + size * math.cos(kat_arrow), y + size * math.sin(kat_arrow)),
        (x - size // 2 * math.cos(kat_arrow + math.pi / 6), y - size // 2 * math.sin(kat_arrow + math.pi / 6)),
        (x - size // 2 * math.cos(kat_arrow - math.pi / 6), y - size // 2 * math.sin(kat_arrow - math.pi / 6))
    ]
    pygame.draw.polygon(win, BIALI, arrow_vertices)


    left_x = x + size * 1.5 * math.cos(kat_arrow + math.pi / 2)
    left_y = y + size * 1.5 * math.sin(kat_arrow + math.pi / 2)
    right_x = x + size * 1.5 * math.cos(kat_arrow - math.pi / 2)
    right_y = y + size * 1.5 * math.sin(kat_arrow - math.pi / 2)


    if scale_x == -1:  
        left_x, right_x = right_x, left_x
        left_y, right_y = right_y, left_y


    left_arrow_vertices = [
        (left_x + size * 0.6 * math.cos(kat_arrow), left_y + size * 0.6 * math.sin(kat_arrow)),
        (left_x - size * 0.3 * math.cos(kat_arrow + math.pi / 6), left_y - size * 0.3 * math.sin(kat_arrow + math.pi / 6)),
        (left_x - size * 0.3 * math.cos(kat_arrow - math.pi / 6), left_y - size * 0.3 * math.sin(kat_arrow - math.pi / 6))
    ]
    pygame.draw.polygon(win, CZERWONY, left_arrow_vertices)


    right_arrow_vertices = [
        (right_x + size * 0.6 * math.cos(kat_arrow), right_y + size * 0.6 * math.sin(kat_arrow)),
        (right_x - size * 0.3 * math.cos(kat_arrow + math.pi / 6), right_y - size * 0.3 * math.sin(kat_arrow + math.pi / 6)),
        (right_x - size * 0.3 * math.cos(kat_arrow - math.pi / 6), right_y - size * 0.3 * math.sin(kat_arrow - math.pi / 6))
    ]
    pygame.draw.polygon(win, ZIELONY, right_arrow_vertices)




def reset():
    win.fill((255, 255, 255))

options = {
    '1': lambda: Nar13Kat(NIEBIESKI, x=300, y=300, radius=50, scale_x=1, scale_y=1),
    '2': lambda: Nar13Kat(NIEBIESKI, x=300, y=300, radius=150, scale_x=1, scale_y=1, kat=math.radians(45)),
    '3': lambda: Nar13Kat(NIEBIESKI, x=300, y=300, radius=100, kat=math.radians(180)),
    '4': lambda: Nar13Kat(NIEBIESKI, x=300, y=300, radius=150, scale_x=1, scale_y=1, skoss_x=0.5),  
    '5': lambda: Nar13Kat(NIEBIESKI, x=300, y=100, radius=150, scale_x=1, scale_y=0.5),
    '6': lambda: Nar13Kat(NIEBIESKI, x=300, y=300, radius=150, scale_x=1, scale_y=1, skoss_x=(-0.5), kat=math.radians(90)),
    '7': lambda: Nar13Kat(NIEBIESKI, x=300, y=300, radius=100, scale_x=-1, scale_y=1, skoss_x=0, kat=math.radians(180)),
    '8': lambda: Nar13Kat(NIEBIESKI, x=300, y=400, radius=150, scale_x=1, scale_y=0.5, kat=math.radians(45)),
    '9': lambda: Nar13Kat(NIEBIESKI, x=400, y=300, radius=150, scale_x=1, scale_y=1, skoss_x=0.5, kat=math.radians(180)),
    '0': lambda: reset()
}


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    user_input = input("Wybierz jedna z 9 opcji klikajac 1/2/3/4/5/6/7/8/9 lub 0 by powrocilo do stanu poczatkowego: ")
    if user_input in options:
        reset()
        options[user_input]()
    
    pygame.display.update()

pygame.quit()