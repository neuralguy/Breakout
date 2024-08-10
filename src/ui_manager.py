import pygame
from ui_elements import *

from config import WIDTH, HEIGHT


class UI:
	def __init__(self) -> None:
		self._states = ["menu", "options", "game"]
		self._current_state = "menu"

		self._ui_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA).convert_alpha()

		self.widgets = {
			"texts": [],
			"buttons": []
		}

	def draw_ui(self, surface:pygame.surface.Surface) -> None:
		for text in self.widgets["texts"]:
			text.draw(self._ui_surface)

		for button in self.widgets["buttons"]:
			text.draw(self._ui_surface)

		surface.blit(self._ui_surface, (0,0))

	def set_state(self, state:str) -> None:
		if state in self._states:
			self._current_state = state
			self.apply_state()
		else:
			raise ValueError(f"Unknown {state}! Use get_states function to see available ones")

	def get_states(self) -> tuple[str]:
		return self._states

	def apply_state(self) -> None:
		match self._current_state:
			case "menu":
				self.create_menu()
			case "options":
				self.create_options()
			case "game"

	def create_menu(self) -> None:
		btn = Button(400, 400, "hui", 1, font_size=32, antialias=True)
		btn.draw(self._ui_surface)



