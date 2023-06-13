import pygame, sys

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(' graphics\ship.png').convert_alpha()
        self.rect = self.image.get_rect(center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2))

# basic setup
pygame.init()
DISPLAY_WIDTH, DISPLAY_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

# sprite groups
spaceship_group = pygame.sprite.Group()

# srite creatinon
ship = Ship()
spaceship_group.add(ship)

# game loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # delta time
    dt = clock.tick(120) / 1000
   
    # Graphics
    spaceship_group.draw(display_surface)

    # draw the frame
    pygame.display.update()