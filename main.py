import pygame, sys
pygame.init()
DISPLAY_WIDTH, DISPLAY_HEIGHT = 1280,720
pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(120)
    pygame.display.update()