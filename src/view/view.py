import pygame
import src.util.game_constants as vc

main_game_screen = pygame.display.set_mode(vc.game_window_size)


def clear_screen():
    main_game_screen.fill(vc.default_background_color)
