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

# current view root (based on player's location)
view_root_x = 0
view_root_y = 0


# draws level from current root position
def draw_level():

    xm = (view_root_x % 1)
    ym = (view_root_y % 1)
    
    x_start = int((view_root_x - xm) - 16)
    y_start = int((view_root_y - ym) - 10)
    
    for y in range(20+1):
        for x in range(32+1):

            field_id = current_level[y_start+y][x_start+x][0]

            if not field_id == 0:
                sub_ind = current_level[y_start+y][x_start+x][1]
                handler = sprite_handlers[field_id]
                sprite = handler.get_subtype_sprite(sub_ind)

                # convert to pygame surface
                surface = pygame.image.fromstring(sprite.tobytes(), sprite.size, sprite.mode)
                surface = pygame.transform.scale(surface, (gc.unit, gc.unit))
                surface_rect = ((x-xm) * gc.unit, (y-ym)*gc.unit)
                screen.blit(surface, surface_rect)


