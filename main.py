import string

from scripts import scenes, settings, music, texts
import pygame

working = True
clock = pygame.time.Clock()

lastTiming = -100

isMenu = True

scriptLineScene = 0
currSceneText = 0

textBack = pygame.image.load('textures/TextBack.png')

lastLetter = clock.get_time()

done = False
currIndex = 0
currText = ''

allText = ''

while working:
    if clock.get_time()-lastTiming > 10:
        if isMenu:
            music.play_ambient_song()
            lastTiming = clock.get_time()
        else:
            pygame.mixer.music.stop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False

        if currIndex < settings.letterinterval * len(allText):
            currIndex += 1
        elif currIndex >= settings.letterinterval * len((allText)):
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            isMenu = False

            data = scenes.nextText(currSceneText, scriptLineScene)

            currSceneText = data[0]
            scriptLineScene = data[1]

            scenes.loadScene(scriptLineScene)

            scenes.screen.blit(textBack, (settings.VW / 2 - textBack.get_width() / 2, settings.VH / 2 + textBack.get_height() / 3))

            allText = texts.textToShow[scriptLineScene][currSceneText]

            currIndex = 0

            done = False

    if isMenu:
        scenes.loadScene(0)

    currText = texts.font.render(allText[0:currIndex//settings.letterinterval], False, 'white')

    textArea = scenes.screen.blit(currText, (180,500))

    if done and not isMenu:
        contText = texts.font.render('Продолжить', False, 'white')
        scenes.screen.blit(contText, (710, 625))

    pygame.display.flip()
    clock.tick(settings.FPS)