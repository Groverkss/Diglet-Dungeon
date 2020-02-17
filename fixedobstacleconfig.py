import pygame

# Window parameters
window_width = 1920
window_height = 1080

# Obstacle parameters
obstacle_width = window_width * 0.07
obstacle_height = window_height * 0.05


class FixedObstacle(pygame.sprite.Sprite):

    def __init__(self, locationx, locationy):

        super().__init__()

        self.image = pygame.image.load("fixed_obstacle.png")
        self.image = pygame.transform.scale(self.image, (obstacle_width,
                                            obstacle_height))
        self.rect = self.image.get_rect()
