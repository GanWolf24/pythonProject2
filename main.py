import pygame
from parametors import *
from sprite import Persona

pygame.init()
pygame.mixer.init()
scrin = pygame.display.set_mode((WIOTH ,WEIGHT))
pygame.display.set_caption("Первая игра")
clock = pygame.time.Clock

running = True
while running:
    #renders
    scrin.fill(GREEN)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Persona_sprite = pygame.sprite.Group()
    persone = Persona()
    Persona_sprite.add(persone)
pygame.quit()
