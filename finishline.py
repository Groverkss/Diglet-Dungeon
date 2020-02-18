import pygame
from turtle import location_x
from turtle import turtle_height
from turtle import turtle_width
from config import *

# Obstacle parameters
obstacle_width = 50
obstacle_height = 30

# Predifned positions
start_bottom_x = location_x[0] - 12
start_bottom_y = window_height * 0.9
start_top_x = location_x[0] - 12
start_top_y = window_height * 0.1 - turtle_height


# Start sprite definations
class Start(pygame.sprite.Sprite):

    def __init__(self, location_x, locationy):

        # Initialise class as a sprite
        super().__init__()

        # Load image sprite and resize it
        self.image = pygame.image.load("data/start.png")
        self.image = pygame.transform.scale(self.image, (obstacle_width,
                                            obstacle_height))
        self.rect = self.image.get_rect()

        # Place image rectangle at specified coordinates
        self.rect.top, self.rect.bottom = (locationy, locationy +
                                           obstacle_height)
        self.rect.left, self.rect.right = (location_x, location_x +
                                           obstacle_width)

    # Reset the sprite on change of player
    def update(self):
        global start_bottom_y
        global start_top_y

        # Swap start position with end position
        if (self.rect.top == start_bottom_y):
            self.rect.top = start_top_y
            self.rect.bottom = start_top_y + obstacle_height
        else:
            self.rect.top = start_bottom_y
            self.rect.bottom = start_bottom_y + obstacle_height


# End sprite definations
class End(pygame.sprite.Sprite):

    def __init__(self, location_x, locationy):

         # Initialise class as a sprite
        super().__init__()

         # Load image sprite and resize it
        self.image = pygame.image.load("data/end.png")
        self.image = pygame.transform.scale(self.image, (obstacle_width,
                                            obstacle_height))
        self.rect = self.image.get_rect()

        # Place image rectangle at specified coordinates
        self.rect.top, self.rect.bottom = (locationy, locationy +
                                           obstacle_height)
        self.rect.left, self.rect.right = (location_x, location_x +
                                           obstacle_width)
    
    # Reset the sprite on change of player
    def update(self):
        global start_bottom_y
        global start_top_y
        
        # Swap start position with end position
        if (self.rect.top == start_bottom_y):
            self.rect.top = start_top_y
            self.rect.bottom = start_top_y + obstacle_height
        else:
            self.rect.top = start_bottom_y
            self.rect.bottom = start_bottom_y + obstacle_height
