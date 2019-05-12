import pygame
import src.util.game_constants as vc
import src.view.view as view
from src.event_handler.event_handler import handle
from src.Entities.entity import Entity

# =========================== GAME INIT ===========================
c = Entity(50, 50)

# displayed application name
pygame.display.set_caption('Hamadryad')

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
    c.move(0.2, 0.3)
    c.act()

    # draws on display
    pygame.display.update()
