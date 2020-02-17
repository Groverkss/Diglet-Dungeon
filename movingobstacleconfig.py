import pygame
import turtleconfig

# Window parameters
window_width = 1920
window_height = 1080

# Obstacle parameters
obstacle_width = 70
obstacle_height = 45
obstacle_speed = 5

# Moving obstacle locations from top
moving_obstacle_locations = []


# Moving obstacle sprite definations
class MovingObstacle(pygame.sprite.Sprite):

    def __init__(self, location_x, locationy, movement_direction):

        super().__init__()

        self.image = pygame.image.load("moving_obstacle.png")
        self.image = pygame.transform.scale(self.image, (obstacle_width,
                                            obstacle_height))
        self.rect = self.image.get_rect()

        self.rect.top, self.rect.bottom = (locationy, locationy +
                                           obstacle_height)
        self.rect.left, self.rect.right = (location_x, location_x +
                                           obstacle_width)
        self.speed = obstacle_speed

        # if direction is of type 2, go left while moving
        if (movement_direction == 2):
            self.speed = -self.speed

        # Method for movement of obstacle
        def move(self):
            self.left += self.speed
            self.right += self.speed
            if (self.left >= window_width):
                self.right = 0
                self.left = self.right - obstacle_width
