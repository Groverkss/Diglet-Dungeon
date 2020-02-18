import pygame
import utility
import turtleconfig
import finishlineconfig
import fixedobstacleconfig
import movingobstacleconfig
from fixedobstacleconfig import fixed_obstacle_locations
from movingobstacleconfig import moving_obstacle_locations

pygame.init()

# Color definations
back = (0, 0, 0)
river = (255, 247, 0)
black = (0, 0, 0)

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
pygame.display.set_caption("Diglet Dungeon")


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

# Moving obstacle sprite group
moving_obstacles = []

# Obstacle numbers based on level
obstacles_on_level = [(6, 9), (9, 8), (9, 11)]

# Current round
current_level = 0


# Initialise moving obstacle sprite group
def moving_object_init():
    global current_level
    global moving_obstacle_locations, moving_obstacles

    movingobstacleconfig.init(obstacles_on_level[current_level][0],
                              obstacles_on_level[current_level][1])
    moving_obstacles.clear()
    for object_location in moving_obstacle_locations:
        new_object = movingobstacleconfig.MovingObstacle(object_location[0],
                                                         object_location[1],
                                                         object_location[2])

        # Increase speed on level 1
        if (current_level == 0):
            if (new_object.movement_direction == 1):
                new_object.speed = 2
            else:
                new_object.speed = -2

        moving_obstacles.append(new_object)


moving_object_init()


# Exit condition checker
game_exit = False

# Initial player
player = player1

# Start text sprite
start_sprite = finishlineconfig.Start(finishlineconfig.start_bottom_x,
                                      finishlineconfig.start_bottom_y)
# End text sprite
end_sprite = finishlineconfig.End(finishlineconfig.start_top_x,
                                  finishlineconfig.start_top_y)

# Spacebar not pressed currently
press_start = False

# Load intro image
intro_image = pygame.image.load("intro.jpeg")
intro_image_rect = intro_image.get_rect()

game_display.blit(intro_image, intro_image_rect)
pygame.display.update()

# Display intro screen while start is not pressed
while not press_start:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            quit()

        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                quit()
            if (event.key == pygame.K_SPACE):
                press_start = True

# Recording time start
prev_time = pygame.time.get_ticks()


# Changes the player on call
def change_player():
    global player, player1, player2, start_sprite, end_sprite, moving_obstacles
    global current_level, prev_time, temp_time, game_exit

    player.time += player.temp_time
    player.temp_time = 0

    player.reset()
    end_sprite.update()
    start_sprite.update()
    if player == player1:
        player = player2
    else:
        player = player1
        if (current_level < 2):
            current_level += 1
        else:
            game_exit = True

    prev_time = pygame.time.get_ticks()

    # Reset the game
    moving_object_init()


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
    player.temp_time = round(((pygame.time.get_ticks() - prev_time) / 1000), 2)

    # Draw fixed_obstacles
    for obstacle in fixed_obstacles:
        game_display.blit(obstacle.image, obstacle.rect)

    # Draw moving obstacles
    for obstacle in moving_obstacles:
        obstacle.move()
        game_display.blit(obstacle.image, obstacle.rect)

    # Collision check between fixed obstacles and player
    for obstacle in fixed_obstacles:
        if (pygame.sprite.collide_rect(player, obstacle)):
            change_player()

    # Collision check between moving obstacles and player
    for obstacle in moving_obstacles:
        if (pygame.sprite.collide_rect(player, obstacle)):
            change_player()

    if (pygame.sprite.collide_rect(player, end_sprite)):
        change_player()

    # Start and End text
    game_display.blit(start_sprite.image, start_sprite.rect)
    game_display.blit(end_sprite.image, end_sprite.rect)

    # Update player
    game_display.blit(player.image, player.rect)

    font = pygame.font.Font(None, 36)
    text = font.render("Time Player1: " + str(round(player1.time +
                       player1.temp_time, 2)), 1, river)
    textpos = text.get_rect(centerx=window_width * 0.1, centery=50)
    game_display.blit(text, textpos)

    font = pygame.font.Font(None, 36)
    text = font.render("Time Player2: " + str(round(player2.time +
                       player2.temp_time, 2)), 1, river)
    textpos = text.get_rect(centerx=window_width * 0.25, centery=50)
    game_display.blit(text, textpos)

    font = pygame.font.Font(None, 36)
    text = font.render("Round: " + str(current_level + 1), 1, river)
    textpos = text.get_rect(centerx=window_width * 0.40, centery=50)
    game_display.blit(text, textpos)

    font = pygame.font.Font(None, 36)
    text = font.render("Player1 Score: " + str(player1.score), 1, river)
    textpos = text.get_rect(centerx=window_width * 0.7, centery=50)
    game_display.blit(text, textpos)

    font = pygame.font.Font(None, 36)
    text = font.render("Player2 Score: " + str(player2.score), 1, river)
    textpos = text.get_rect(centerx=window_width * 0.85, centery=50)
    game_display.blit(text, textpos)

    pygame.display.update()
    clock.tick(frames_per_sec)

if (player1.score > player2.score):
    winner = 1
elif (player1.score < player2.score):
    winner = 2
elif (player1.time < player2.time):
    winner = 1
else:
    winner = 2

ending_image = pygame.image.load("gameover.jpeg")
ending_image_rect = ending_image.get_rect()
game_display.blit(ending_image, ending_image_rect)

font = pygame.font.Font(None, 80)
if (winner == 1):
    text = font.render("Player 1 wins with score: " + str(player1.score) +
                       " and time: " + str(round(player1.time, 2)), 1, black)
else:
    text = font.render("Player 2 wins with score: " + str(player2.score) +
                       " and time: " + str(round(player2.time, 2)), 1, black)
textpos = text.get_rect(centerx=window_width * 0.5, centery=window_height *
                        0.55)
game_display.blit(text, textpos)

pygame.display.update()

# Game over exit condition
press_exit = False

# Game over screen
while not press_exit:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            quit()
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                quit()