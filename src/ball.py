import pygame
from pygame.math import Vector2
from helper import *
from config import BALL_SIZE, BALL_SPEED, WIDTH, HEIGHT
from math import atan2, sin, cos, radians, floor
from random import randint


class Ball:
    def __init__(self, x:int, y:int) -> None:

        self._image = scale_sprite(
                            crop_sprite(
                                load_sprite("../res/img/asset.png"), 
                            384, 432, 16, 16), 
                        BALL_SIZE, BALL_SIZE)

        self._pos = Vector2(x, y)
        self._vel = Vector2()

        self._size = BALL_SIZE
        self._speed = BALL_SPEED

        self.rect = pygame.Rect((x, y, self._size, self._size))

        self._dead = False

        self._batt_hit_sound = pygame.mixer.Sound("../res/sound/batt_hit.wav")
        self._brick_hit_sound = pygame.mixer.Sound("../res/sound/Shoot_1.wav")

    def move(self, delta_time:float=1) -> None:
        self.wall_colision()

        if abs(self._vel.x) > self._speed:
            self._vel.x *= 0.99

        if abs(self._vel.y) > self._speed:
            self._vel.y *= 0.99

        self._pos += self._vel * delta_time

        self.rect.topleft = self._pos.xy

    def wall_colision(self) -> None:
        if self.rect.left < 0:
            self._pos.x = 0
            self._vel.x *= -1

        if self.rect.right > WIDTH:
            self._pos.x = WIDTH - self._size
            self._vel.x *= -1

        if self.rect.top < 0:
            self._pos.y = 0 
            self._vel.y *= -1

        if self.rect.bottom >= HEIGHT:
            self._dead = True

    def batt_colision(self, batt:pygame.Rect) -> None:
        batt_rect = batt.get_rect()
        if self.rect.colliderect(batt_rect):
                self._pos.y = batt_rect.top - self._size - 1

                self._vel.y *= -1.4

                # to control the ball with a bat
                distance = self.rect.centerx - batt_rect.centerx
                self._vel.x += distance * 5 + batt.get_speed()

                self._batt_hit_sound.play()

    def brick_colision(self, bricks:pygame.sprite.Group) -> None:
        for brick in bricks.sprites():
            if self.rect.colliderect(brick.rect):
                if brick.get_lives() > 1:
                    brick.damage()
                else:
                    bricks.remove(brick)

                if self.rect.left > brick.rect.left and self.rect.right > brick.rect.right:
                    self.rect.left = brick.rect.right + 1
                    self._vel.x *= -1 

                elif self.rect.left < brick.rect.left and self.rect.right < brick.rect.right:
                    self.rect.right = brick.rect.left - 1
                    self._vel.x *= -1 

                elif self.rect.top > brick.rect.top and self.rect.bottom > brick.rect.bottom:
                    self.rect.top = brick.rect.bottom + 1
                    self._vel.y *= -1 

                elif self.rect.top < brick.rect.top and self.rect.bottom < brick.rect.bottom:
                    self.rect.bottom = brick.rect.top - 1
                    self._vel.y *= -1 

                self._brick_hit_sound.play()

                break

    def draw(self, surface:pygame.surface.Surface) -> None:        
        surface.blit(self._image, (self._pos.x, self._pos.y))

    def launch(self) -> None:
        angle = radians(randint(200, 330))
        self._vel = Vector2(self._speed * cos(angle), self._speed * sin(angle))

    def is_launched(self) -> bool:
        return self._vel != Vector2()

    def is_dead(self) -> bool:
        return self._dead

    def set_position(self, position:tuple[int,int]|list[int,int]) -> None:
        self._pos.x, self._pos.y = [i - self._size // 2 for i in position]
        self.rect.x = self._pos.x
        self.rect.y = self._pos.y

    def get_rect(self) -> pygame.rect.Rect:
        return self.rect

    def draw_debug(self, surface):
        coeff = 0.1
        pygame.draw.rect(surface, "red", (self.rect.x, self.rect.y, self._size, self._size), 1)
        pygame.draw.line(surface, "red", (self.rect.centerx, self.rect.centery), (self.rect.centerx+self._vel.x*coeff, self.rect.centery+self._vel.y*coeff), 5)
        # draw_text(surface, f"{self._vel.x}\n{self._vel.y}", (self.rect.topleft))

