import pygame
from helper import *
from config import WIDTH, HEIGHT, BRICK_WIDTH, BRICK_HEIGHT


textures = [
    [
        scale_sprite(
            crop_sprite(
                load_sprite("../res/img/asset.png"), 
                448 + j * 64, 0 + i * 32, 64, 32), 
            BRICK_WIDTH, BRICK_HEIGHT) 
        for j in range(3)
    ] for i in range(9)]


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, texture_num):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = textures[texture_num]

        self.lives = 3

        self.image = self.sprites[3-self.lives]
        self.rect = pygame.rect.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)

    def draw(self, surface:pygame.surface.Surface) -> None:
        surface.blit(self.image, self.rect)

    def get_lives(self) -> int:
        return self.lives

    def damage(self) -> None:
        self.lives -= 1
        self.image = self.sprites[3-self.lives]


def create_bricks(brick_map, bricks_group:pygame.sprite.Group) -> None:
    for row, i in enumerate(brick_map):
        for col, j in enumerate(i):
            if j != "-":
                bricks_group.add(Brick(col*BRICK_WIDTH, row*BRICK_HEIGHT, j))
