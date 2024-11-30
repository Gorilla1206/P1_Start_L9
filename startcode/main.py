import pygame, sys
from pygame.locals import QUIT

pygame.init()
venster = pygame.display.set_mode((2000, 2000))
venster.fill((255,255,255))
color = (0,0,0)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed() == (True,False,False):
            pygame.draw.circle(venster, color, pygame.mouse.get_pos(), 5)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255,0,0)
            if event.key == pygame.K_s:
                pygame.image.save(venster, "tekening" + ".jpg")
            if event.key == pygame.K_g:
                color = (255, 255, 255)

    pygame.display.update()
















