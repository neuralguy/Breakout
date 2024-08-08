import pygame


# general setup
WIDTH = 700
HEIGHT = 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
GAME_TITLE = "Breakout"
pygame.display.set_caption(GAME_TITLE)

# framerate
FPS = 60

# batt settings
BATT_WIDTH = 100
BATT_HEIGHT = 20
BATT_SPEED = 400

# ball settings 
BALL_SIZE = 15
BALL_SPEED = 500

# brick settings
BRICK_WIDTH = 70
BRICK_HEIGHT = 35