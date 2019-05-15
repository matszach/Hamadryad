from src.entities.entity import GroundCharacterEntity
import pygame
from src.view.view import main_game_screen as screen
from src.util.game_constants import unit
from src.maps import map_handler as mh


class PlayerEntity(GroundCharacterEntity):

    def display(self):

        print(self.x, self.y)

        sprite = self.sprite_handler.pick_sprite(self.spd_x, self.spd_y)
        surface = pygame.image.fromstring(sprite.tobytes(), sprite.size, sprite.mode)  # convert to pygame surface
        surface = pygame.transform.scale(surface, (self.size, self.size))

        y_off = 0 if mh.view_root_y < 10 else mh.view_root_y - 10
        x_off = 0 if mh.view_root_x < 16 else mh.view_root_x - 16

        surface_rect = (self.x-x_off*unit, self.y-y_off*unit)
        screen.blit(surface, surface_rect)

