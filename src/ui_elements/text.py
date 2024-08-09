# Don't forget pygame.init() before using it

import pygame

class Text:
	def __init__(self, 
			x: int, 
			y: int, 
			text: str, 
			text_color: tuple[int,int,int]|list[int,int,int]|str="white", 
			text_alpha: int=1,
			font_size: int=16, 
			font_path: str="freesansbold.ttf", 
			antialias: bool=False) -> None:
		self.__text = text
		self.__text_color = text_color
		self.__text_alpha = text_alpha

		self.__font = pygame.font.Font(font_path, font_size)
		self.__render = self.__font.render(text, antialias, text_color).convert_alpha()
		# self.__render.set_alpha(self.__text_alpha)

		self.__width = self.__render.get_width()
		self.__height = self.__render.get_height()
		self.__x = x - self.__width // 2
		self.__y = y - self.__height // 2
		self.__rect = self.__render.get_rect()

		self.__antialias = antialias

	def draw(self, surface:pygame.surface.Surface) -> None:
		surface.blit(self.__render, (self.__x, self.__y))
		
	def set_text(self, text:str) -> None:
		self.__text = text
		self.__render = self.__font.render(text, self.__antialias, self.__text_color)

	def set_text_color(self, text_color:tuple[int,int,int]|list[int,int,int]|str) -> None:
		self.__text_color= text_color
		self.__render = self.__font.render(self.__text, self.__antialias, text_color)

	def get_pos(self) -> tuple[int,int]:
		return (self.__x, self.__y)

	def get_text(self) -> str:
		return self.__text

	def get_text_color(self) -> tuple[int,int,int]|list[int,int,int]|str:
		return self.__text_color

	def get_render(self) -> pygame.surface.Surface:
		return self.__render

	def get_width(self) -> int:
		return self.__width

	def get_height(self) -> int:
		return self.__height

	def is_collide(self, x:int, y:int) -> bool:
		return self.__rect.collidepoint(x, y)
