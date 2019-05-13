from src.sprite_manager.sprite_handler import SpriteHandler

sh = SpriteHandler('resources/template16.png')

sprite = sh.get_sprite_at(2,2)

sprite.save('resources/sprite.png')
