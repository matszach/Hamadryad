import pygame
import src.util.game_constants as vc
import src.view.view as view
from src.event_handler.event_handler import handle
from src.entities.entity import GroundCharacterEntity
from src.maps.map_handler import draw_level
from src.entities.entity_handler import run_monsters, run_projectiles


c = GroundCharacterEntity(sprite_set_path='resources/sprites/template16.png', hspeed=5, init_y=200)
c.jump()

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
    draw_level(0, 0)

    # monsters and projectiles act
    run_monsters()
    run_projectiles()

    # todo temp
    c.move_right()
    c.act()

    # draws on display
    pygame.display.update()
