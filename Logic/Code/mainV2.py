import pygame, sys
from settingsV2 import*
from levelV2 import Level
from game_data import level_0




pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_0, screen)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('grey')
    level.run()

    pygame.display.update()
    clock.tick(60)

