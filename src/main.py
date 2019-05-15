import pygame
import src.util.game_constants as vc
import src.view.view as view
from src.event_handler.event_handler import handle
from src.maps.map_handler import draw_level
from src.entities.entity_handler import run_monsters, run_projectiles, run_player, adjust_view_root
from src.event_handler import key_handler

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

    # todo make this dependant on player position
    draw_level()

    # monsters and projectiles act
    run_monsters()
    run_projectiles()

    # player acts
    run_player()
    key_handler.execute()

    # view root is adjusted ("follows player")
    adjust_view_root()

    # draws on display
    pygame.display.update()
