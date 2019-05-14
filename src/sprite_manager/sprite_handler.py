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

        # current to-be-displayed sprite
        self.current_sprite = self.get_sprite_at(0, 0)


# Sprite handler for characters
class CharacterSpriteHandler(SpriteHandler):

    # constructor
    def __init__(self, sprite_set_path):
        SpriteHandler.__init__(self, sprite_set_path)


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

