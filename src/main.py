import pygame
import asyncio
from batt import Batt
from ball import Ball
from brick import create_bricks
from config import WIDTH, HEIGHT, FPS, SCREEN
from helper import *


class Game:
    def __init__(self):
        pygame.init()
        self.batt = Batt(WIDTH // 2, HEIGHT * 0.95)
        self.ball = Ball(WIDTH // 2, HEIGHT * 0.8)
        self.game_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA) 
        self.game_background = scale_sprite(load_sprite("../res/img/background.jpg"), WIDTH, HEIGHT)
        self.pause = False

        self.clock = pygame.time.Clock()
        self.previous_time = pygame.time.get_ticks()
        self.delta_time = 0.01

        self.holding_ball = False

        self.brick_map = [
                            ["-", "-",  "-",  "-",  "-",  "-",  "-",  "-",  "-", "-"],
                            ["-",  5,    5,    5,    5,    5,    5,    5,    5,  "-"],
                            ["-",  4,    4,    4,    4,    4,    4,    4,    4,  "-"],
                            ["-",  3,    3,    3,    3,    3,    3,    3,    3,  "-"],
                            ["-",  2,    2,    2,    2,    2,    2,    2,    2,  "-"],
                            ["-",  1,    1,    1,    1,    1,    1,    1,    1,  "-"],
                            ["-",  0,    0,    0,    0,    0,    0,    0,    0,  "-"],
                        ]
        self.bricks = pygame.sprite.Group()
        create_bricks(self.brick_map, self.bricks)

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                self.handle_event(event)
                
            self.update_game()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            exit()

        # pause the game when pressing SPACE
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.pause = not self.pause
        # launching the ball when pressing RETURN
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and not self.ball.is_launched():
            self.ball.launch()

        # if clicking on the ball
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.ball.get_rect().collidepoint(event.pos):
            self.holding_ball = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.holding_ball = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.batt.change_direction(-1) # move left
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.batt.change_direction(1) # move right
        else:
            self.batt.change_direction(0) # don't move

    def update_game(self):
        self.calculate_time()
        self.draw_game()
        if not self.pause:
            self.process_objects()

    def draw_game(self):
        self.game_surface.blit(self.game_background, (0,0))

        self.bricks.draw(self.game_surface)
        self.batt.draw(self.game_surface)
        self.ball.draw(self.game_surface)
        if self.holding_ball:
            self.ball.draw_debug(self.game_surface)

        if not self.ball.is_launched():
            draw_text(self.game_surface, "PRESS ENTER TO START", (WIDTH // 10, HEIGHT // 6), 45)

        SCREEN.blit(self.game_surface, (0,0))
        pygame.display.update()

    def process_objects(self):
        if self.holding_ball:
            self.ball.set_position(pygame.mouse.get_pos())
        elif not self.ball.is_launched():
            batt_x, batt_y = self.batt.get_position()
            self.ball.set_position((batt_x, batt_y * 0.9))
        else:
            self.ball.brick_colision(self.bricks)
            self.ball.batt_colision(self.batt)
            self.ball.move(self.delta_time)

            if self.ball.is_dead():
                self.game_over()

        self.batt.calculate_state()
        self.batt.move(self.delta_time)

    def calculate_time(self):
        current_time = pygame.time.get_ticks()
        self.delta_time = (current_time - self.previous_time) / 1000
        self.previous_time = current_time
        self.clock.tick(FPS)

    def game_over(self):
        pass


if __name__ == "__main__":
    game = Game()
    game.mainloop()
