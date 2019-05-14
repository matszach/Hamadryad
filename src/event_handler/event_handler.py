import sys
import pygame
from src.event_handler import key_handler


def handle(event):

    # close button
    if event.type == pygame.QUIT:
        sys.exit()
