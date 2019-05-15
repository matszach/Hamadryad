from src.entities.entity import GroundCharacterEntity
import src.maps.map_handler as mh


class SimpleFollower(GroundCharacterEntity):

    def work(self):
        if mh.player_x > self.get_x_unit():
            self.move_right()
        else:
            self.move_left()
        if mh.player_y + 0.5 < self.get_y_unit():
            self.jump()
