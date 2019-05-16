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
    if keys[pygame.K_7]:
        player.action_1()
    elif keys[pygame.K_8]:
        player.action_2()
    elif keys[pygame.K_9]:
        player.action_3()
    elif keys[pygame.K_0]:
        player.action_4()




