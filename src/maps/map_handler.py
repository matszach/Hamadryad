from src.view.view import main_game_screen as screen
from src.maps.level_parser import load_level
from src.util import game_constants as gc
from src.sprite_manager.sprite_handler import TileSpriteHandler
import pygame

# loaded level's map
current_level = load_level('level1')

# tile sprite handlers
sprite_handlers = {
    1: TileSpriteHandler('resources/sprites/tile_stone.png')
}


# draws level from current root position
def draw_level(root_x, root_y):
    xm = (root_x % gc.unit)*gc.unit
    ym = (root_x % gc.unit)*gc.unit
    for y in range(int(gc.game_window_size[1]/gc.unit)):
        for x in range(int(gc.game_window_size[0]/gc.unit)):
            field_id = current_level[round(root_y)+y][round(root_x)+x][0]
            if not field_id == 0:
                sub_ind = current_level[round(root_y)+y][round(root_x)+x][1]
                handler = sprite_handlers[field_id]
                sprite = handler.get_subtype_sprite(sub_ind)
                # convert to pygame surface
                surface = pygame.image.fromstring(sprite.tobytes(), sprite.size, sprite.mode)
                surface = pygame.transform.scale(surface, (gc.unit, gc.unit))
                surface_rect = (x * gc.unit - xm, y*gc.unit - ym)
                screen.blit(surface, surface_rect)


