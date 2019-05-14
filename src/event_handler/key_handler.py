from src.entities.entity_handler import player
import pygame


def execute():

    keys = pygame.key.get_pressed()

    # movement
    if keys[pygame.K_a]:
        player.move_left()
    elif keys[pygame.K_d]:
        player.move_right()
    else:
        player.slow_down()

    # jumping
    if keys[pygame.K_SPACE] or keys[pygame.K_w]:
        player.jump()

    # actions
    if keys[pygame.K_o]:
        player.action_1()
    elif keys[pygame.K_p]:
        player.action_2()



