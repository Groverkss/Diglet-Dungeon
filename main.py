import pygame
import utility
import turtleconfig

pygame.init()

# Color definations
back = (0, 0, 0)
river = (255, 247, 0)

# Game variables
window_width = 1920
window_height = 1080
frames_per_sec = 60
game_exit = False

# River locations from top
river_locations = [window_height * 0.15, window_height * 0.3,
                    window_height * 0.45, window_height * 0.6,
                    window_height * 0.75]

# Game window initialisations
game_display = pygame.display.set_mode((window_width, window_height),
                                        pygame.FULLSCREEN)
pygame.display.set_caption("Turtle Crossing")
clock = pygame.time.Clock()

player = turtleconfig.Turtle();

# Game loop
while not game_exit:

    # Event loop
    for event in pygame.event.get():
        
        # Quit condition
        if (event.type == pygame.QUIT):
            quit()
        
        if (event.type == pygame.KEYDOWN):

            # Quit condition
            if (event.key == pygame.K_ESCAPE):
                quit()

            # Player movement
            if (event.key == pygame.K_LEFT):
                player.speed[0] = -5
            elif (event.key == pygame.K_RIGHT):
                player.speed[0] = 5
            elif (event.key == pygame.K_UP):
                player.speed[1] = -5
            elif (event.key == pygame.K_DOWN):
                player.speed[1] = 5
        
        elif (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or
                    event.key == pygame.K_RIGHT):
                player.speed[0] = 0
            elif (event.key == pygame.K_UP or
                    event.key == pygame.K_DOWN):
                player.speed[1] = 0


    # Draw background
    utility.draw_thing(game_display, 0, 0, window_width, 
                        window_height, back)
    for location in river_locations:
        utility.draw_thing(game_display, 0, location, window_width,
                            window_height * 0.07, river)

    player.move()
    game_display.blit(player.image, player.rect)

    pygame.display.update()
    clock.tick(frames_per_sec)