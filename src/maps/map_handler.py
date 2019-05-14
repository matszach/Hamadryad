from src.view.view import main_game_screen as screen
from src.maps.level_parser import load_level
from src.util import game_constants as gc
import pygame

# loaded level's map
current_level = load_level('level1')


def draw_level(root_x, root_y):
    for y in range(int(gc.game_window_size[1]/gc.unit)):
        for x in range(int(gc.game_window_size[0]/gc.unit)):
            if current_level[root_y+y][root_x+x][0] == 1:
                pygame.draw.rect(screen, (0, 100, 0), (x*gc.unit, y*gc.unit, gc.unit, gc.unit))
                pygame.draw.rect(screen, (0, 60, 0), (x * gc.unit+3, y * gc.unit+3, gc.unit-6, gc.unit-6))


