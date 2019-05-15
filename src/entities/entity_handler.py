from src.entities.player.player import PlayerEntity
from src.entities.monsters.basic_monsters import SimpleFollower
import src.maps.map_handler as mh
from src.util.game_constants import view_width, view_height

player = PlayerEntity(sprite_set_path='resources/sprites/character.png', hspeed=7)
monsters = []
projectiles = []

monsters.append(SimpleFollower(sprite_set_path='resources/sprites/template16.png', hspeed=2))
monsters.append(SimpleFollower(sprite_set_path='resources/sprites/template16.png', hspeed=3, init_x=330))


def run_monsters():
    for m in monsters:
        m.act()


def run_projectiles():
    for p in projectiles:
        p.act()


def run_player():
    player.act()


def adjust_view_root():
    mh.view_root_x = player.get_x_unit() if player.get_x_unit() >= view_width/2 else view_width/2
    mh.view_root_y = player.get_y_unit() if player.get_y_unit() >= view_height/2 else view_height/2
    mh.player_x = player.get_x_unit()
    mh.player_y = player.get_y_unit()
