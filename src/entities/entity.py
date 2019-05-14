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
        return True  # todo

    def possible_move_right(self):
        return True  # todo

    def possible_move_up(self):
        return True  # todo

    def possible_move_down(self):
        return True # todo

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
    # (obstacles)
    def adjust_speed(self):
        if self.spd_x < 0 and not self.possible_move_left():
            self.spd_x = 0
        elif self.spd_x > 0 and not self.possible_move_right():
            self.spd_x = 0
        if self.spd_y < 0 and not self.possible_move_up():
            self.spd_y = 0
        elif self.spd_y > 0 and not self.possible_move_down():
            self.spd_y = 0

    # applies current speed as movement
    def travel(self):
        self.move(self.spd_x, self.spd_y)

    # entity travels a distance equal to the passed values
    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    # constructor
    def __init__(self, init_x, init_y):

        # current location
        self.x = init_x
        self.y = init_y


# parent class to all characters (Monsters, Player ...)
class CharacterEntity(Entity):

    # character moves left
    def move_left(self):
        self.spd_x -= ec.move_acc_increment*self.hspeed
        self.spd_x = self.spd_x if self.spd_x >= -self.hspeed else -self.hspeed

    # character moves right
    def move_right(self):
        self.spd_x += ec.move_acc_increment*self.hspeed
        self.spd_x = self.spd_x if self.spd_x <= self.hspeed else self.hspeed

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
        surface = pygame.image.fromstring(sprite.tobytes(), sprite.size, sprite.mode)  # convert to pygame surface
        surface = pygame.transform.scale(surface, (self.size, self.size))
        surface_rect = (self.x, self.y)
        screen.blit(surface, surface_rect)

    # constructor
    def __init__(self, sprite_set_path, hp, defence, power, hspeed, size, init_x, init_y):
        Entity.__init__(self, init_x, init_y)

        # character's health
        # character dies when it's health reaches 0
        self.max_hp = hp
        self.curr_hp = hp

        # reduces damage taken
        self.defence = defence

        # increases effectiveness of character's actions
        self.power = power

        # limits character's horizontal movement speed
        self.hspeed = hspeed

        # character's size (determines hit-boxes, drawn images size ...)
        self.size = size

        # manages character's sprite set
        self.sprite_handler = CharacterSpriteHandler(sprite_set_path)


# parent class to all non-flying characters
class GroundCharacterEntity(CharacterEntity):

    # describes changes to character speed caused by outside forces
    # (obstacles, friction, gravity)
    def adjust_speed(self):
        self.fall()
        CharacterEntity.adjust_speed(self)

    # character falling (called every frame)
    def fall(self):
        self.spd_y += ec.move_acc_increment*ec.max_fall_spd
        self.spd_y = self.spd_y if self.spd_y <= ec.max_fall_spd else ec.max_fall_spd

    # jump
    def jump(self):
        if not self.possible_move_down():  # prevents "mid-air-jumps"
            self.spd_y = -self.jump_speed

    # constructor
    def __init__(self, sprite_set_path, hp=10, defence=0, power=10, hspeed=1, size=32, init_x=0, init_y=0, jump_speed=20):
        CharacterEntity.__init__(self, sprite_set_path, hp, defence, power, hspeed, size, init_x, init_y)

        # vertical speed applied when character jumps
        self.jump_speed = jump_speed


# parent class to all non-flying characters
class FlyingCharacterEntity(CharacterEntity):

    # character moves left
    def move_up(self):
        self.spd_y -= ec.move_acc_increment * self.vspeed
        self.spd_y = self.spd_y if self.spd_y >= -self.vspeed else -self.vspeed

    # character moves right
    def move_down(self):
        self.spd_y += ec.move_acc_increment * self.vspeed
        self.spd_y = self.spd_y if self.spd_y <= self.vspeed else self.vspeed

    # constructor
    def __init__(self, sprite_set_path, hp=10, defence=0, power=10, hspeed=1, size=32, init_x=0, init_y=0, vspeed=1):
        CharacterEntity.__init__(self, sprite_set_path, hp, defence, power, hspeed, size, init_x, init_y)

        # limits character's vertical movement speed
        self.vspeed = vspeed
