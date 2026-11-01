import pygame

# pygame setup
pygame.init()


pygame.display.set_caption(
    title="space shooter game", icontitle="./assets/images/spaceship.png"
)
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

game_run = True


while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

    screen.fill("red")

    clock.tick(60)
    pygame.display.update()


pygame.quit()
