import pygame
import utility
import turtleconfig
import fixedobstacleconfig
import movingobstacleconfig
from fixedobstacleconfig import fixed_obstacle_locations
from movingobstacleconfig import moving_obstacle_locations

pygame.init()

# Color definations
back = (0, 0, 0)
river = (255, 247, 0)

# Game window dimensions
window_width = 1920
window_height = 1080

# FPS
frames_per_sec = 72

# Player sprites
player1 = turtleconfig.Turtle(1)
player2 = turtleconfig.Turtle(2)

# River locations from top
river_locations = [window_height * 0.15, window_height * 0.3,
                   window_height * 0.45, window_height * 0.6,
                   window_height * 0.75]

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

# Moving obstacle sprtie group
moving_obstacles = []
for object_location in moving_obstacle_locations:
    new_object = movingobstacleconfig.MovingObstacle(object_location[0],
                                                     object_location[1])
    moving_obstacles.append(new_object)

# Exit condition checker
game_exit = False

# Temp arrangement
# FIX THIS LATER
player = player1
diglet = movingobstacleconfig.MovingObstacle(0, 0, 1)

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

    # Draw moving obstacles
    for obstacle in moving_obstacles:
        game_display.blit(obstacle.image, obstacle.rect)

    # Collision check between fixed obstacles and player
    for obstacle in fixed_obstacles:
        if (pygame.sprite.collide_rect(player, obstacle)):
            quit()  # ADD CRASH CONDITION LATER

    # Collision check between moving obstacles and player
    for obstacle in moving_obstacles:
        if (pygame.sprite.collide_rect(player, obstacle)):
            quit()  # ADD CRASH CONDITION LATER

    pygame.display.update()
    clock.tick(frames_per_sec)
