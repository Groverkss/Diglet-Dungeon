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

score_location1 = [(0.75, 10), (0.67, 5), (0.6, 10), (0.52, 5), (0.45, 10),
                   (0.37, 5), (0.3, 10), (0.22, 5), (0.15, 10), (-1, 0)]

score_location2 = [(0.22, 10), (0.3, 5), (0.37, 10), (0.45, 5), (0.52, 10),
                   (0.6, 5), (0.67, 10), (0.75, 5), (0.82, 10), (1, 0)]


# Turtle sprtie definations
class Turtle(pygame.sprite.Sprite):

    def __init__(self, player_number):

        super().__init__()

        # Load image and resize it
        self.image = pygame.image.load("turtle.png")
        self.image = pygame.transform.scale(self.image, (turtle_width,
                                            turtle_height))

        self.player_number = player_number

        # Flip the image if it is player 2
        if (self.player_number == 2):
            self.image = pygame.transform.rotate(self.image, 180)

        # Initial coordinates
        self.locationx = (location_x[0] - 12, location_x[1] - 12)

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

        self.score = 0

        self.current_locate = 0

        self.time = 0
        self.temp_time = 0

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

        if (self.player_number == 1):
            if (self.rect.top <= score_location1[self.current_locate][0] * window_height):
                self.score += score_location1[self.current_locate][1]
                self.current_locate += 1
        else:
            if (self.rect.top >= score_location2[self.current_locate][0] * window_height):
                self.score += score_location2[self.current_locate][1]
                self.current_locate += 1

    # Resets coordinates and speed
    def reset(self):

        # Initial image placement
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.right = self.locationx[0], self.locationx[1]
        self.rect.top, self.rect.bottom = self.locationy[0], self.locationy[1]

        # Initial speed
        self.speed = [0, 0]

        # Initialise score locater
        self.current_locate = 0
