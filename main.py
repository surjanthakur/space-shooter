import pygame

# pygame setup
pygame.init()

pygame.display.set_caption(
    title="space shooter game", icontitle="./assets/images/spaceship.png"
)

screen = pygame.display.set_mode((800, 1000))
clock = pygame.time.Clock()
game_run = True
game_started = False
menu_font = pygame.font.SysFont(None, 56)
menu_labels = ("Start New Game ", "Exit")

# sounds
laser_sound = pygame.mixer.Sound("./assets/audio/shot.wav")
background_sound = pygame.mixer.Sound("./assets/audio/music2.mp3")


# surfaces
space_img_surface = pygame.image.load(
    "./assets/images/space_background.png"
).convert_alpha()

spaceship_img_surface = pygame.image.load(
    "./assets/images/spaceship.png"
).convert_alpha()

fire_laser_surface = pygame.image.load("./assets/images/bullet.png").convert_alpha()

fire_laser_surface = pygame.transform.flip(fire_laser_surface, False, True)

meteor_01_surface = pygame.image.load("./assets/images/meteor_01.png").convert_alpha()
meteor_02_surface = pygame.image.load("./assets/images/meteor_02.png").convert_alpha()
meteor_03_surface = pygame.image.load("./assets/images/asteroid_03.png").convert_alpha()
meteor_04_surface = pygame.image.load("./assets/images/asteroid_04.png").convert_alpha()

# rects
spaceship_rect = spaceship_img_surface.get_rect(midbottom=(350, 800))
meteor_1_rect = meteor_01_surface.get_rect(topleft=(0, 10))
laser_rects = []
menu_rects = [
    menu_font.render(label, True, "white").get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + offset)
    )
    for label, offset in zip(menu_labels, (-40, 40))
]

# run game base on game_run condition
while game_run:
    # get pygame events
    for event in pygame.event.get():

        # if quit game close the game engine
        if event.type == pygame.QUIT:
            game_run = False
        elif (
            not game_started
            and event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
        ):
            # if press on [start new game] start the game
            if menu_rects[0].collidepoint(event.pos):
                game_started = True
                background_sound.play(loops=-1)

            # if press quit then close the game
            elif menu_rects[1].collidepoint(event.pos):
                game_run = False
                # check if game started and keyboard key pressed.
        elif game_started and event.type == pygame.KEYDOWN:

            # if left key
            if event.key == pygame.K_LEFT:
                # move space ship to left side
                spaceship_rect.x -= 60

                # if right key
            elif event.key == pygame.K_RIGHT:
                # move space ship to right side
                spaceship_rect.x += 60

                # if up key
            elif event.key == pygame.K_UP:
                # move space ship to top
                spaceship_rect.y -= 60

                # if down key
            elif event.key == pygame.K_DOWN:
                # move space ship  to down
                spaceship_rect.y += 60

                # if press F key
            elif event.key == pygame.K_f:
                # get wings positions
                wing_positions = (
                    # left side
                    spaceship_rect.left + spaceship_rect.width // 8,
                    # right side
                    spaceship_rect.right - spaceship_rect.width // 8,
                )
                for wing_x in wing_positions:
                    # set laser positions
                    laser_rects.append(
                        fire_laser_surface.get_rect(
                            midbottom=(wing_x, spaceship_rect.top)
                        )
                    )
                    # play sound after positions set
                laser_sound.play()

    if not game_run:
        break

    screen.blit(space_img_surface, (0, 0))

    if game_started:
        spaceship_rect.clamp_ip(screen.get_rect())

        # spaceship surface image
        screen.blit(spaceship_img_surface, spaceship_rect)

        # meteor 1 surface image
        meteor_1_rect.y += 5
        if meteor_1_rect.y >= screen.get_height():
            meteor_1_rect.y = 0
        screen.blit(meteor_01_surface, meteor_1_rect)

        for laser_rect in laser_rects:
            laser_rect.y -= 10
            screen.blit(fire_laser_surface, laser_rect)
        laser_rects = [
            laser_rect for laser_rect in laser_rects if laser_rect.bottom > 0
        ]
    else:
        mouse_position = pygame.mouse.get_pos()
        for label, menu_rect in zip(menu_labels, menu_rects):
            color = "yellow" if menu_rect.collidepoint(mouse_position) else "white"
            text_surface = menu_font.render(label, True, color)
            screen.blit(text_surface, menu_rect)

    # al last update all changes and display screen
    pygame.display.update()
    clock.tick(60)


pygame.quit()
