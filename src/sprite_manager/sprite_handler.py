from PIL import Image
import os

# sizes of individual sprites
sprite_size = 16

# width of the border separating sprites in the sprite set
border_width = 1


# parent class to character and particle sprite handlers
class SpriteHandler:

    # current to-be-displayed sprite
    current_sprite = None

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

    # constructor
    def __init__(self, sprite_set_path):
        SpriteHandler.__init__(self, sprite_set_path)



