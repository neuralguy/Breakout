import pygame
from helper import *
from config import WIDTH, BATT_WIDTH, BATT_HEIGHT, BATT_SPEED



class Batt:
	def __init__(self, x:int, y:int):

		self._sprites = [
						scale_sprite(
							crop_sprite(
								load_sprite("../res/img/asset.png"), 
							32*i, 16, 32, 16), 
						BATT_WIDTH, BATT_HEIGHT)
					for i in range(5)] 
		self._state = 0 
		self._x = x - BATT_WIDTH // 2
		self._rect = pygame.rect.Rect(x - BATT_WIDTH // 2, y - BATT_HEIGHT // 2, BATT_WIDTH, BATT_HEIGHT)
		self._speed = BATT_SPEED
		self._direction = 0
		self._last_time = 0

	def move(self, delta_time:float=1) -> None:
		if (0 <= self._x and self._direction == -1) or (self._x + self._rect.width <= WIDTH and self._direction == 1):
			self._x += self._speed * self._direction * delta_time

			self._rect.x = self._x

	def draw(self, surface:pygame.Surface) -> None:
		surface.blit(self._sprites[self._state], (self._rect.x, self._rect.y))

	def get_rect(self) -> pygame.rect.Rect:
		return self._rect

	def change_direction(self, value:int) -> None:
		self._direction = value

	def get_position(self) -> tuple[int,int]:
		return self._rect.center

	def get_speed(self) -> int:
		return self._speed * self._direction

	def calculate_state(self):
		if pygame.time.get_ticks() - self._last_time > 200:
			self._last_time = pygame.time.get_ticks()
			if self._state < 4:
				self._state += 1
			else:
				self._state = 0