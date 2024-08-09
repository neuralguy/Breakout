import pygame


def load_sprite(path:str) -> pygame.surface.Surface:
    return pygame.image.load(path).convert_alpha()

def scale_sprite(sprite:pygame.surface.Surface, width:int, height:int) -> pygame.surface.Surface:
    return pygame.transform.scale(sprite, (width, height)).convert_alpha()

def crop_sprite(sprite:pygame.surface.Surface, x:int, y:int, width:int, height:int) -> pygame.surface.Surface:
    return sprite.subsurface((x, y, width, height)).convert_alpha()

def draw_text(surface:pygame.surface.Surface, text:str, position:tuple[int,int]|list[int,int], font_size:int=16):
    font = pygame.font.Font("freesansbold.ttf", font_size)
    text = font.render(text, True, "white")
    surface.blit(text, position)

class TimerManager:
    def __init__(self):
        self.timers = []

    def add_timer(self, name: str, interval: float, callback: callable, *args):
        timer = {
            "name": name,
            "interval": interval, # miliseconds
            "callback": callback,
            "args": args,
            "next_update_time": pygame.time.get_ticks()
        }
        self.timers.append(timer)
    
    def remove_timer(self, name):
        """removing timer with name from the list of timers"""
        for timer in self.timers:
            if timer["name"] == name:
                self.timers.remove(timer)
                break

    async def update_arguments(self, name, *args):
        """updating arguments for the timer"""
        for timer in self.timers:
            if timer["name"] == name:
                timer["args"] = args
                break

    async def update(self):
        """calling all timers"""
        current_time = pygame.time.get_ticks()
        for timer in self.timers:
            if current_time >= timer["next_update_time"]:
                timer["callback"](*timer["args"])
                timer["next_update_time"] = current_time + timer["interval"]