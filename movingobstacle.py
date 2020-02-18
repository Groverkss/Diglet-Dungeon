import pygame
import turtle
from config import *

# Obstacle parameters
obstacle_width = 70
obstacle_height = 45
obstacle_speed = 1.5
obstacle_offset = 0

# Moving obstacle locations from top
moving_obstacle_locations = []


# Initialise obstacle locations
def init(moving_obstacles_on_odd_rivers, moving_obstacles_on_even_rivers):
    global moving_obstacle_locations

    # Clear the list
    moving_obstacle_locations.clear()
    # Initialising moving obstacle count for first rivers and offset from left
    moving_obstacle_count = moving_obstacles_on_odd_rivers
    # Adding obstacle locations on odd rivers from both sides
    for obstacle_num in range(moving_obstacle_count):
        moving_obstacle_locations.append((window_width *
                                         (obstacle_num /
                                          moving_obstacle_count),
                                         (window_height * 0.15), 1))
        moving_obstacle_locations.append((window_width *
                                         (obstacle_num /
                                          moving_obstacle_count),
                                         (window_height * 0.45), 1))
        moving_obstacle_locations.append((window_width *
                                         (obstacle_num /
                                          moving_obstacle_count),
                                         (window_height * 0.75), 1))

    # Initialising moving obstacle count for second rivers and offset from left
    moving_obstacle_count = moving_obstacles_on_even_rivers
    # Adding obstacle locations on even rivers from both sides
    for obstacle_num in range(moving_obstacle_count):
        moving_obstacle_locations.append((window_width *
                                         (obstacle_num /
                                          moving_obstacle_count),
                                         (window_height * 0.3), 2))
        moving_obstacle_locations.append((window_width *
                                         (obstacle_num /
                                          moving_obstacle_count),
                                         (window_height * 0.6), 2))


# Moving obstacle sprite definations
class MovingObstacle(pygame.sprite.Sprite):

    def __init__(self, location_x, locationy, movement_direction):

        # Initialise class as sprite
        super().__init__()

        # Load sprite image
        self.image = pygame.image.load("data/moving_obstacle.png")
        self.image = pygame.transform.scale(self.image, (obstacle_width,
                                            obstacle_height))
        self.rect = self.image.get_rect()

        # Place sprite according to given coordinates
        self.rect.top, self.rect.bottom = (locationy, locationy +
                                           obstacle_height)
        self.rect.left, self.rect.right = (location_x, location_x +
                                           obstacle_width)

        # Set obstacle speed and direction                                   
        self.speed = obstacle_speed
        self.movement_direction = movement_direction

        # if direction is of type 2, go left while moving
        if (self.movement_direction == 2):
            self.speed = -self.speed

    # Method for movement of obstacle
    def move(self):
        self.rect.left += self.speed
        self.rect.right += self.speed

        # Replacement on going offscreen
        if (self.movement_direction == 1):
            if (self.rect.left >= window_width):
                self.rect.right = 0
                self.rect.left = self.rect.right - obstacle_width
        else:
            if (self.rect.right <= 0):
                self.rect.left = window_width
                self.rect.right = self.rect.left + obstacle_width
