import pygame


# Draws a rectanglular object on screen
def draw_thing(game_display, thing_x, thing_y,
               thing_width, thing_height, color):
    pygame.draw.rect(game_display, color,
                     [thing_x, thing_y, thing_width, thing_height])
