from src.entities.player.player import PlayerEntity
import src.maps.map_handler as mh

player = PlayerEntity(sprite_set_path='resources/sprites/character.png', hspeed=7)
monsters = []
projectiles = []


def run_monsters():
    for m in monsters:
        m.act()


def run_projectiles():
    for p in projectiles:
        p.act()


def run_player():
    player.act()


def adjust_view_root():
    mh.view_root_x = player.get_x_unit() if player.get_x_unit() >= 16 else 16
    mh.view_root_y = player.get_y_unit() if player.get_y_unit() >= 10 else 10
