import pygame
from scripts import settings

pygame.init()
screen = pygame.display.set_mode((settings.VW, settings.VH))


def loadScene(currScene):
    if currScene == 0:
        img = pygame.image.load('scenes/menu/back.png')
        screen.blit(img, (0, 0))
    if currScene == 1:
        img = pygame.image.load('scenes/mainScenes/bus.jpg')
        screen.blit(img, (0, 0))
    if currScene == 2:
        img = pygame.image.load('scenes/menu/back.png')
        screen.blit(img, (0, 0))


def nextText(currTextNum, currSceneNum):
    if currSceneNum == 0:
        return [0, 1]
    elif currSceneNum == 1:
        if currTextNum == 7:
            currSceneNum += 1
            currTextNum = 0
        else:
            currTextNum += 1
    elif currSceneNum == 2:
        if currSceneNum == 15:
            currSceneNum += 1
            currTextNum = 0
        else:
            currTextNum += 1
    elif currSceneNum == 3:
        pass
    elif currSceneNum == 4:
        pass
    elif currSceneNum == 5:
        pass
    elif currSceneNum == 6:
        pass
    elif currSceneNum == 7:
        pass
    elif currSceneNum == 8:
        pass
    elif currSceneNum == 9:
        pass
    elif currSceneNum == 10:
        pass
    elif currSceneNum == 11:
        pass


    return currTextNum, currSceneNum





