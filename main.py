from scripts import scenes, settings, music
import pygame

working = True
clock = pygame.time.Clock()

lastTiming = -100

isMenu = True


while working:
    if isMenu:
        scenes.loadScene("scenes/menu/back.png")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False

        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     scenes.loadScene('scenes/mainScenes/bus.jpg')
        #     isMenu = False

    if clock.get_time()-lastTiming > 100:
        music.play_ambient_song()
        lastTiming = clock.get_time()

    pygame.display.flip()
    clock.tick(settings.FPS)