import pygame
import src.util.game_constants as vc
import src.view.view as view
from src.event_handler.event_handler import handle
from src.entities.entity import GroundCharacterEntity


c = GroundCharacterEntity(sprite_set_path='resources/template16.png', speed=5)

# displayed application name
pygame.display.set_caption(vc.game_name)

# main game loop
while True:

    # game speed / 'frame-rate'
    pygame.time.delay(vc.game_frame_delay)

    # list of events (keyboard / mouse presses)
    for event in pygame.event.get():
        handle(event)

    # "clears" the screen by filling it with background color
    view.clear_screen()

    # todo temp
    c.move_right()
    c.act()

    # draws on display
    pygame.display.update()
