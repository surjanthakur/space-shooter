import sys

import pygame

# pygame setup
pygame.init()


pygame.display.set_caption(
    title="space shooter game", icontitle="./assets/images/spaceship.png"
)
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
game_run = True

# surfaces
space_img_surface = pygame.image.load(
    "./assets/images/space_background.png"
).convert_alpha()


while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
            sys.exit()

    screen.fill("red")

    pygame.display.update()
    clock.tick(60)


pygame.quit()
