import pygame
import utility

pygame.init()

# Color definations
blue = (0, 255, 255)
lime = (0, 255, 0)

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

    # Draw background
    utility.draw_thing(game_display, 0, 0, window_width, 
                        window_height, lime)
    for location in river_locations:
        utility.draw_thing(game_display, 0, location, window_width,
                            window_height * 0.1, blue)

    pygame.display.update()
    clock.tick(frames_per_sec)