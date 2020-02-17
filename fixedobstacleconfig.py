import pygame
import turtleconfig

# Window parameters
window_width = 1920
window_height = 1080

# Obstacle parameters
obstacle_width = 70
obstacle_height = 60

# Offset for fixing distance from top
obstacle_offset = 0.02
bottom_obstacle_offset = 0.03
bank_obstacle_offset = 0.01

# Boundary gate obstacles
# Obstacle positions in order ->
# Topleft top
# Topright top
# Bottomleft bottom
# Bottomright bottom
# Topleft middle
# Topright middle
# Bottomleft middle
# Bottomright middle
# Topleft bottom
# Topright bottom
# Bottomleft top
# Bottomright top
fixed_obstacle_locations = [(turtleconfig.location_x[0] -
                            (2 * turtleconfig.turtle_width), 0 -
                            window_height * obstacle_offset),
           
                            (turtleconfig.location_x[1], 0 -
                            window_height * obstacle_offset),

                            (turtleconfig.location_x[0] -
                            (2 * turtleconfig.turtle_width),
                            window_height - turtleconfig.turtle_height * 2 +
                            window_height * bottom_obstacle_offset),

                            (turtleconfig.location_x[1], window_height -
                            (turtleconfig.turtle_height * 2) +
                            window_height * bottom_obstacle_offset),

                            (turtleconfig.location_x[0] -
                            (2 * turtleconfig.turtle_width),
                            turtleconfig.turtle_height - window_height *
                            obstacle_offset),

                            (turtleconfig.location_x[1],
                            turtleconfig.turtle_height - window_height *
                            obstacle_offset),

                            (turtleconfig.location_x[0] -
                            (2 * turtleconfig.turtle_width),
                            window_height - (turtleconfig.turtle_height * 3) +
                            window_height * bottom_obstacle_offset),

                            (turtleconfig.location_x[1], window_height -
                            (turtleconfig.turtle_height * 3) +
                            window_height * bottom_obstacle_offset),

                            (turtleconfig.location_x[0] -
                            (2 * turtleconfig.turtle_width),
                            (turtleconfig.turtle_height * 2) -
                            window_height * obstacle_offset),

                            (turtleconfig.location_x[1],
                            (turtleconfig.turtle_height * 2) -
                            window_height * obstacle_offset),

                            (turtleconfig.location_x[0] -
                            (2 * turtleconfig.turtle_width),
                            window_height - (turtleconfig.turtle_height * 4) +
                            window_height * bottom_obstacle_offset),

                            (turtleconfig.location_x[1], window_height -
                            (turtleconfig.turtle_height * 4) +
                            window_height * bottom_obstacle_offset),
                            ]

fixed_obstacles_on_first_bank = 8
fixed_obstacles_on_second_bank = 12

# Initialising fixed obstacle count for first banks and offset from left
fixed_obstacle_count = fixed_obstacles_on_first_bank
first_bank_offset = window_width / (fixed_obstacle_count + 1)
# Adding obstacle locations on first banks from both sides
for obstacle_num in range(fixed_obstacle_count):
    fixed_obstacle_locations.append((first_bank_offset + window_width *
                                    (obstacle_num / fixed_obstacle_count),
                                    (window_height * 0.22) +
                                    window_height * bank_obstacle_offset))
    fixed_obstacle_locations.append((first_bank_offset + window_width *
                                    (obstacle_num / fixed_obstacle_count),
                                    (window_height * 0.67) +
                                    window_height * bank_obstacle_offset))

# Initialising fixed obstacle count for second bank and offset from left
fixed_obstacle_count = fixed_obstacles_on_second_bank
second_bank_offset = window_width / (fixed_obstacle_count + 1)
# Adding obstacle locations on second banks from both sides
for obstacle_num in range(fixed_obstacle_count):
    fixed_obstacle_locations.append((second_bank_offset + window_width *
                                    (obstacle_num / fixed_obstacle_count),
                                    (window_height * 0.37) +
                                    window_height * bank_obstacle_offset))
    fixed_obstacle_locations.append((second_bank_offset + window_width *
                                    (obstacle_num / fixed_obstacle_count),
                                    (window_height * 0.52) +
                                    window_height * bank_obstacle_offset))

# Boundary parameters
boundary_count = 14
boundary_offset = window_width

# Boundary obstacles
# Obstacle positions in order ->
# Topeft
# Bottomleft
# Topright
# Bottomright
for obstacle in range(boundary_count):
    fixed_obstacle_locations.append((obstacle * (obstacle_width * 0.9),
                                    (turtleconfig.turtle_height * 2) -
                                    window_height * obstacle_offset))

    fixed_obstacle_locations.append((obstacle * (obstacle_width * 0.9),
                                    window_height -
                                    (turtleconfig.turtle_height * 4) +
                                    window_height * bottom_obstacle_offset))

    fixed_obstacle_locations.append((boundary_offset - (obstacle *
                                    (obstacle_width)),
                                    (turtleconfig.turtle_height * 2) -
                                    window_height * obstacle_offset))

    fixed_obstacle_locations.append((boundary_offset - (obstacle *
                                    (obstacle_width)),
                                    window_height -
                                    (turtleconfig.turtle_height * 4) +
                                    window_height * bottom_obstacle_offset))


# Fixed obstacle sprite definations
class FixedObstacle(pygame.sprite.Sprite):

    def __init__(self, location_x, locationy):

        super().__init__()

        self.image = pygame.image.load("fixed_obstacle.png")
        self.image = pygame.transform.scale(self.image, (obstacle_width,
                                            obstacle_height))
        self.rect = self.image.get_rect()

        self.rect.top, self.rect.bottom = (locationy, locationy +
                                           obstacle_height)
        self.rect.left, self.rect.right = (location_x, location_x +
                                           obstacle_width)
