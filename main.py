import pygame
import utility
import turtleconfig
import fixedobstacleconfig
from fixedobstacleconfig import fixed_obstacle_locations

pygame.init()

# Color definations
back = (0, 0, 0)
river = (255, 247, 0)

# Game window dimensions
window_width = 1920
window_height = 1080

# FPS
frames_per_sec = 120

# Player sprites
player1 = turtleconfig.Turtle(1)
player2 = turtleconfig.Turtle(2)

# River locations from top
river_locations = [window_height * 0.15, window_height * 0.3,
                   window_height * 0.45, window_height * 0.6,
                   window_height * 0.75]

# Initialising fixed obstacle count for first banks and offset from left
fixed_obstacle_count = fixedobstacleconfig.fixed_obstacles_on_first_bank
first_bank_offset = window_width / (fixed_obstacle_count + 1)
# Adding obstacle locations on first banks from both sides
for obstacle_num in range(fixed_obstacle_count):
    fixed_obstacle_locations.append((first_bank_offset + window_width *
                                    (obstacle_num / fixed_obstacle_count),
                                    window_height * 0.22))
    fixed_obstacle_locations.append((first_bank_offset + window_width *
                                    (obstacle_num / fixed_obstacle_count),
                                    window_height * 0.67))

# Initialising fixed obstacle count for second bank and offset from left
fixed_obstacle_count = fixedobstacleconfig.fixed_obstacles_on_second_bank
second_bank_offset = window_width / (fixed_obstacle_count + 1)
# Adding obstacle locations on second banks from both sides
for obstacle_num in range(fixed_obstacle_count):
    fixed_obstacle_locations.append((second_bank_offset + window_width *
                                    (obstacle_num / fixed_obstacle_count),
                                    window_height * 0.37))
    fixed_obstacle_locations.append((second_bank_offset + window_width *
                                    (obstacle_num / fixed_obstacle_count),
                                    window_height * 0.52))

# Game window initialisations
game_display = pygame.display.set_mode((window_width, window_height),
                                       pygame.FULLSCREEN)
pygame.display.set_caption("Turtle Crossing")

# Game clock
clock = pygame.time.Clock()

# Hide mouse in game window
pygame.mouse.set_visible(0)

# Fixed obstacle sprite group
fixed_obstacles = []
for object_location in fixed_obstacle_locations:
    new_object = fixedobstacleconfig.FixedObstacle(object_location[0],
                                                   object_location[1])
    fixed_obstacles.append(new_object)

# Exit condition checker
game_exit = False

# Temp arrangement
player = player1

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
                # Move left
                player.speed[0] = -player.movement_rate
            elif (event.key == pygame.K_RIGHT):
                # Move right
                player.speed[0] = player.movement_rate
            elif (event.key == pygame.K_UP):
                # Move up
                player.speed[1] = -player.movement_rate
            elif (event.key == pygame.K_DOWN):
                # Move down
                player.speed[1] = player.movement_rate

        elif (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or
                    event.key == pygame.K_RIGHT):
                # Stop moving horizontally
                player.speed[0] = 0
            elif (event.key == pygame.K_UP or
                    event.key == pygame.K_DOWN):
                # Stop moving vertically
                player.speed[1] = 0

    # Draw background
    utility.draw_thing(game_display, 0, 0,
                       window_width, window_height, back)
    for location in river_locations:
        utility.draw_thing(game_display, 0, location, window_width,
                           window_height * 0.07, river)

    # Move player
    player.move()

    # Update player
    game_display.blit(player.image, player.rect)
    game_display.blit(player2.image, player2.rect)

    # Draw fixed_obstacles
    for obstacle in fixed_obstacles:
        game_display.blit(obstacle.image, obstacle.rect)

    pygame.display.update()
    clock.tick(frames_per_sec)
