import pygame
from src.view.view import main_game_screen as screen
from src.sprite_manager.sprite_handler import CharacterSpriteHandler
import src.entities.entity_constants as ec


# parent class to all in-game entities
class Entity:

    # current x and y speed
    spd_x = 0
    spd_y = 0

    # movement-in-direction-possible checking
    def possible_move_left(self):
        return False  #todo

    def possible_move_right(self):
        return False  #todo

    def possible_move_up(self):
        return False  # todo

    def possible_move_down(self):
        return False  # todo

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
        pass

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


# parent class to all characters (Monsters, Player ...)
class CharacterEntity(Entity):

    # character moves left
    def move_left(self):
        self.spd_x += ec.move_acc_increment
        self.spd_x = self.spd_x if self.spd_x <= self.speed else self.speed

    # character moves right
    def move_right(self):
        self.spd_x -= ec.move_acc_increment
        self.spd_x = self.spd_x if self.spd_x >= -self.speed else -self.speed

    # character's first action
    def action_1(self):
        pass  # todo

    # character's second action
    def action_2(self):
        pass  # todo

    # character dies
    def die(self):
        pass  # todo

    # character is damaged
    def take_damage(self, dmg):
        dmg = dmg - self.defence if dmg > self.defence else 0  # prevents negative damage
        self.curr_hp -= dmg
        if self.curr_hp <= 0:
            self.die()

    # character regenerates taken damage
    def regenerate(self, reg):
        self.curr_hp += reg
        self.curr_hp = self.curr_hp if self.curr_hp <= self.max_hp else self.max_hp

    # displays the entity on game screen
    def display(self):
        sprite = self.sprite_handler.current_sprite
        img_rect = (self.size, self.size)
        screen.blit(sprite, img_rect)

    # constructor
    def __init__(self, sprite_set, hp=10, defence=0, power=10, speed=1, size=16, init_x=0, init_y=0):
        Entity.__init__(self, init_x, init_y)

        # character's health
        # character dies when it's health reaches 0
        self.max_hp = hp
        self.curr_hp = hp

        # reduces damage taken
        self.defence = defence

        # increases effectiveness of character's actions
        self.power = power

        # limits character's movement speed
        self.speed = speed

        # character's size (determines hit-boxes, drawn images size ...)
        self.size = size

        # manages character's sprite set
        self.sprite_handler = CharacterSpriteHandler(sprite_set)


# parent class to all non-flying characters
class GroundCharacterEntity(CharacterEntity):

    # constructor
    def __init__(self, sprite_set, hp=10, defence=0, power=10, speed=1, size=16, init_x=0, init_y=0):
        CharacterEntity.__init__(sprite_set, hp, defence, power, speed, size, init_x, init_y)


# parent class to all non-flying characters
class FlyingCharacterEntity(CharacterEntity):

    # constructor
    def __init__(self, sprite_set, hp=10, defence=0, power=10, speed=1, size=16, init_x=0, init_y=0):
        CharacterEntity.__init__(sprite_set, hp, defence, power, speed, size, init_x, init_y)
