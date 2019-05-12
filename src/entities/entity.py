import pygame
from src.view.view import main_game_screen as screen


# parent class to all in-game entities
class Entity:

    # describes sum everything that the entity does during one frame
    def act(self):
        self.work()
        self.display()

    # displays the entity on game screen
    def display(self):
        # todo
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 30, 30))

    # describes workings of the entity
    def work(self):
        pass

    # entity travels a distance equal to the passed values
    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    # constructor
    def __init__(self, init_x=0, init_y=0):

        # entity's current location
        self.x = init_x
        self.y = init_y
