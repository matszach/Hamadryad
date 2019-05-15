from PIL import Image
import os

# sizes of individual sprites
sprite_size = 16

# width of the border separating sprites in the sprite set
border_width = 1


# parent class to character and particle sprite handlers
class SpriteHandler:

    # returns sprite at location (x,y) from sprite set
    def get_sprite_at(self, x, y):
        x = x*(sprite_size+border_width)
        y = y*(sprite_size+border_width)
        crop_area = (x, y, x+sprite_size, y+sprite_size)
        return self.sprite_set.crop(crop_area)

    # constructor
    def __init__(self, sprite_set_path):

        # single image containing all of the entity's sprites
        abs_path = os.path.normpath(os.getcwd() + os.sep + os.pardir) + '\\' + sprite_set_path
        self.sprite_set = Image.open(abs_path)


# Sprite handler for characters
class CharacterSpriteHandler(SpriteHandler):

    # animation timer limit
    a_lim = 23

    # static sprite dictionary
    sprite_paths = {
        # speed x, speed y, timer : sprite x,y
        (False, 0, 0): (0, 0),  # idle
        (False, 0, 1): (0, 1),
        (False, 0, 2): (0, 2),
        (False, 0, 3): (0, 3),
        (True, 0, 0): (1, 0),   # run / move hor
        (True, 0, 1): (1, 1),
        (True, 0, 2): (1, 2),
        (True, 0, 3): (1, 3),
        (False, 1, 0): (2, 0),  # fall / move down
        (False, 1, 1): (2, 1),
        (True, 1, 0): (2, 0),
        (True, 1, 1): (2, 1),
        (False, 1, 2): (2, 0),
        (False, 1, 3): (2, 1),
        (True, 1, 2): (2, 0),
        (True, 1, 3): (2, 1),
        (False, -1, 0): (2, 2),  # jump / move up
        (False, -1, 1): (2, 3),
        (True, -1, 0): (2, 2),
        (True, -1, 1): (2, 2),
        (False, -1, 2): (2, 2),
        (False, -1, 3): (2, 3),
        (True, -1, 2): (2, 2),
        (True, -1, 3): (2, 3),
        #todo other
    }

    # increments / resets animation timer
    def animation_tick(self):
        self.animation_timer += 1 if self.animation_timer < self.a_lim else -self.a_lim

    # sets current sprite based on character's current speed values
    def pick_sprite(self, spd_x, spd_y):

        is_hor_mov = not spd_x == 0
        ver_mov = 0 if spd_y == 0 else int(spd_y/abs(spd_y))
        sprite_loc = self.sprite_paths[(is_hor_mov, ver_mov, int(self.animation_timer/6))]

        sprite = self.get_sprite_at(sprite_loc[1], sprite_loc[0])

        if spd_x > 0:
            self.should_flip = False
        elif spd_x < 0:
            self.should_flip = True

        if self.should_flip:
            sprite = sprite.transpose(Image.FLIP_LEFT_RIGHT)

        self.animation_tick()

        return sprite

    # constructor
    def __init__(self, sprite_set_path):
        SpriteHandler.__init__(self, sprite_set_path)
        self.animation_timer = 0
        self.should_flip = False


# Sprite handler for tile types
class TileSpriteHandler(SpriteHandler):

    # static subtype indicator dictionary
    sub_loc = {
        'l': (0, 0),
        'u': (0, 1),
        'r': (0, 2),
        'b': (0, 3),
        'lu': (1, 0),
        'ru': (1, 1),
        'rb': (1, 2),
        'lb': (1, 3),
        'lt': (2, 0),
        'ut': (2, 1),
        'rt': (2, 2),
        'bt': (2, 3),
        'vo': (3, 0),
        'ho': (3, 1),
        'c': (3, 2),
        's': (3, 3)
    }

    # returns sprite subtype
    def get_subtype_sprite(self, subtype_indicator):
        loc = self.sub_loc[subtype_indicator]
        return self.get_sprite_at(loc[1], loc[0])

    # constructor
    def __init__(self, sprite_set_path):
        SpriteHandler.__init__(self, sprite_set_path)


# Sprite handler for projectile entities
class ProjectileSpriteHandler(SpriteHandler):
    pass
