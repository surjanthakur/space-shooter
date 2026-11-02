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

fire_lasers = pygame.image.load("./assets/images/Rocket_Effect_01.png").convert_alpha()

meteor_01_surface = pygame.image.load("./assets/images/meteor_01.png").convert_alpha()
meteor_02_surface = pygame.image.load("./assets/images/meteor_02.png").convert_alpha()
meteor_03_surface = pygame.image.load("./assets/images/asteroid_03.png").convert_alpha()
meteor_04_surface = pygame.image.load("./assets/images/asteroid_04.png").convert_alpha()

# rects
spaceship_rect = spaceship_img_surface.get_rect(midbottom=(350, 800))

meteor_1_rect = meteor_01_surface.get_rect(topleft=(0, 10))


while game_run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_run = False
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            spaceship_rect.x -= 60

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            spaceship_rect.x += 60

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            spaceship_rect.y -= 60

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            spaceship_rect.y += 60

        # when press F key on keyboard fire_laser effect from the space ship

    spaceship_rect.clamp_ip(screen.get_rect())

    screen.blit(space_img_surface, (0, 0))

    # spaceship surface image
    screen.blit(spaceship_img_surface, spaceship_rect)

    # meteor 1 surface image
    meteor_1_rect.y += 5
    if meteor_1_rect.y >= screen.get_height():
        meteor_1_rect.y = 0
    screen.blit(meteor_01_surface, meteor_1_rect)

    # al last update all changes and display screen
    pygame.display.update()
    clock.tick(60)


pygame.quit()
