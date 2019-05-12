import pygame
from src.view.view import main_game_screen as screen


# parent class to all in-game entities
class Entity:

    # current x and y speed
    spd_x = 0
    spd_y = 0

    # describes total of everything that the entity does during one frame
    def act(self):
        self.work()
        self.adjust_speed()
        self.travel()
        self.select_sprite()
        self.display()

    # selects correct sprite from file to be drawn
    def select_sprite(self):
        pass

    # displays the entity on game screen
    def display(self):
        # todo
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 30, 30))

    # describes workings of the entity
    # (attacking, jumping, walking, other actions)
    def work(self):
        pass

    # describes changes to character speed caused by outside forces
    # (friction, gravity, obstacles)
    def adjust_speed(self):
        pass

    # applies current speed as movement
    def travel(self):
        self.move(self.spd_x, self.spd_y)

    # entity travels a distance equal to the passed values
    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    # constructor
    def __init__(self, init_x=0, init_y=0):

        # current location
        self.x = init_x
        self.y = init_y
