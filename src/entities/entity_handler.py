from src.entities.entity import GroundCharacterEntity

player = GroundCharacterEntity(sprite_set_path='resources/sprites/character.png', hspeed=7,)
monsters = []
projectiles = []


def run_monsters():
    for m in monsters:
        m.act()


def run_projectiles():
    for p in projectiles:
        p.act()

