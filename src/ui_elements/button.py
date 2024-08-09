import pygame
from .text import Text


class Button(Text):
	def __init__(self, 
			x: int, 
			y: int, 
			text: str, 
			callback: callable, 
			width: int=-1, 
			height: int=-1,
			text_color: tuple[int,int,int]|list[int,int,int]|str="white", 
			text_alpha: int=0,
			font_size: int=16, 
			font_path: str="freesansbold.ttf", 
			antialias: bool=False,
			background_color: tuple[int,int,int]|list[int,int,int]|str="gray", 
			background_alpha: int=255
			) -> None:
		super().__init__(x, y, text, text_color,  text_alpha, font_size,  font_path,  antialias)

		self.__callback = callback
		self.__width = width if width != -1 else self.get_width() + 20
		self.__height = height if height != -1 else self.get_height()

		self.__background_color = background_color
		self.__background_alpha = background_alpha
		self.__background_surface = pygame.Surface((self.__width, self.__height), pygame.SRCALPHA).convert_alpha()
		self.update_background()

	def press(self) -> None:
		self.__callback()

	def draw(self, surface:pygame.surface.Surface) -> None:
		surface.blit(self.__background_surface, self.get_pos())
		surface.blit(self.get_render(), self.get_pos())

	def update_background(self):
		self.__background_surface.set_alpha(self.__background_alpha)
		self.__background_surface.fill(self.__background_color)

	def set_callback(self, callback:callable) -> None:
		self.__callback = callback

	def get_callback(self) -> callable:
		return self.__callback