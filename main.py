import sys

import pygame

# pygame setup
pygame.init()


pygame.display.set_caption(
    title="space shooter game", icontitle="./assets/images/spaceship.png"
)
screen = pygame.display.set_mode((800, 1000))
clock = pygame.time.Clock()
game_run = True

# surfaces
space_img_surface = pygame.image.load(
    "./assets/images/space_background.png"
).convert_alpha()

spaceship_img_surface = pygame.image.load("./assets/images/spaceship.png")


while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
            sys.exit()

    screen.blit(space_img_surface, (0, 0))
    screen.blit(spaceship_img_surface, (200, 700))
    pygame.display.update()
    clock.tick(60)


pygame.quit()
