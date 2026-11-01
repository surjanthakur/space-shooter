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

spaceship_img_surface = pygame.image.load(
    "./assets/images/spaceship.png"
).convert_alpha()

meteor_01_surface = pygame.image.load("./assets/images/meteor_01.png").convert_alpha()
meteor_02_surface = pygame.image.load("./assets/images/meteor_02.png").convert_alpha()
meteor_03_surface = pygame.image.load("./assets/images/asteroid_03.png").convert_alpha()
meteor_04_surface = pygame.image.load("./assets/images/asteroid_04.png").convert_alpha()

# rects
spaceship_rect = spaceship_img_surface.get_rect(midbottom=(350, 800))


while game_run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_run = False
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            spaceship_rect.x -= 20

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            spaceship_rect.x += 20

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            spaceship_rect.y -= 20

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            spaceship_rect.y += 20

    screen.blit(space_img_surface, (0, 0))

    screen.blit(spaceship_img_surface, spaceship_rect)

    screen.blit(meteor_01_surface, (0, 0))
    screen.blit(meteor_02_surface, (180, 0))
    screen.blit(meteor_03_surface, (200, 500))
    screen.blit(meteor_04_surface, (450, 400))
    pygame.display.update()
    clock.tick(60)


pygame.quit()
