import pygame
import turtleconfig

# Window parameters
window_width = 1920
window_height = 1080

# Obstacle parameters
obstacle_width = int(window_width * 0.06)
obstacle_height = int(window_height * 0.1)

# Offset for fixing distance from top
obstacle_offset = 0.02

# Fixed obstacle locations from top
fixed_obstacle_locations = [(turtleconfig.location_x[0] -
                            (2 * turtleconfig.turtle_width), 0 -
                            window_height * obstacle_offset),

                            (turtleconfig.location_x[1], 0 -
                            window_height * obstacle_offset),

                            (turtleconfig.location_x[0] -
                            (2 * turtleconfig.turtle_width),
                            window_height - turtleconfig.turtle_height * 2),

                            (turtleconfig.location_x[1], window_height -
                            turtleconfig.turtle_height * 2),

                            (turtleconfig.location_x[0] -
                            (2 * turtleconfig.turtle_width),
                            turtleconfig.turtle_height - window_height *
                            obstacle_offset),

                            (turtleconfig.location_x[1],
                            turtleconfig.turtle_height - window_height *
                            obstacle_offset),

                            (turtleconfig.location_x[0] -
                            (2 * turtleconfig.turtle_width),
                            window_height - turtleconfig.turtle_height * 3),

                            (turtleconfig.location_x[1], window_height -
                            turtleconfig.turtle_height * 3),

                            (turtleconfig.location_x[0] -
                            (2 * turtleconfig.turtle_width),
                            (turtleconfig.turtle_height * 2) -
                            window_height * obstacle_offset),

                            (turtleconfig.location_x[1],
                            (turtleconfig.turtle_height * 2) -
                            window_height * obstacle_offset),

                            (turtleconfig.location_x[0] -
                            (2 * turtleconfig.turtle_width),
                            window_height - turtleconfig.turtle_height * 4),

                            (turtleconfig.location_x[1], window_height -
                            turtleconfig.turtle_height * 4),
                            ]

fixed_obstacles_on_first_bank = 8
fixed_obstacles_on_second_bank = 12


class FixedObstacle(pygame.sprite.Sprite):

    def __init__(self, location_x, locationy):

        super().__init__()

        self.image = pygame.image.load("fixed_obstacle.png")
        self.image = pygame.transform.scale(self.image, (obstacle_width,
                                            obstacle_height))
        self.rect = self.image.get_rect()

        self.rect.topleft = (location_x, locationy)
