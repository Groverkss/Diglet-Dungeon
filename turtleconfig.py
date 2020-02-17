import pygame

# Window parameters
window_width = 1920
window_height = 1080

# Turtle parameters
turtle_width = 50
turtle_height = 50
location_x = [(window_width / 2) - (turtle_width / 2),
              (window_width / 2) - (turtle_width / 2) +
              turtle_width]


class Turtle(pygame.sprite.Sprite):

    def __init__(self, player_number):

        super().__init__()

        # Load image and resize it
        self.image = pygame.image.load("turtle.png")
        self.image = pygame.transform.scale(self.image, (turtle_width,
                                            turtle_height))

        # Flip the image if it is player 2
        if (player_number == 2):
            self.image = pygame.transform.rotate(self.image, 180)

        # Initial coordinates
        self.locationx = location_x

        if (player_number == 1):
            self.locationy = [window_height * 0.9, (window_height * 0.9) +
                              turtle_height]
        else:
            self.locationy = [window_height * 0.1 - turtle_height,
                              (window_height * 0.1)]

        # Initial image placement
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.right = self.locationx[0], self.locationx[1]
        self.rect.top, self.rect.bottom = self.locationy[0], self.locationy[1]

        # Initial speed
        self.speed = [0, 0]

        # Increase in speed on movement in the direction
        self.movement_rate = 2

    # Move the sprite according to speed
    def move(self):

        # Move only if not going out of boundary horizontally
        if (self.rect.right + self.speed[0] <= window_width and
                self.rect.left + self.speed[0] >= 0):
            self.rect.left += self.speed[0]
            self.rect.right += self.speed[0]

        # Move only if not going out of boundary vertically
        if (self.rect.bottom + self.speed[1] <= window_height and
                self.rect.top + self.speed[1] >= 0):
            self.rect.top += self.speed[1]
            self.rect.bottom += self.speed[1]
