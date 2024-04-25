import pygame
from scripts import settings

pygame.init()
screen = pygame.display.set_mode((settings.VW, settings.VH))

def loadScene(path):

    img = pygame.image.load(path)

    screen.blit(img, (0, 0))



