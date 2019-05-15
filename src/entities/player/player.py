from src.entities.entity import GroundCharacterEntity, ProjectileEntity
import src.entities.spawner as spawner


class PlayerEntity(GroundCharacterEntity):

    def action_1(self):
        spd_x = -15 if self.sprite_handler.should_flip else +15
        spawner.spawn_projectile(ProjectileEntity(init_x=self.x, init_y=self.y, spd_x=spd_x, spd_y=-1, size=10))

    def action_2(self):
        spd_x = -15 if self.sprite_handler.should_flip else +15
        spawner.spawn_projectile(ProjectileEntity(init_x=self.x, init_y=self.y, spd_x=spd_x, spd_y=0))
        spawner.spawn_projectile(ProjectileEntity(init_x=self.x, init_y=self.y, spd_x=spd_x, spd_y=-2))
        spawner.spawn_projectile(ProjectileEntity(init_x=self.x, init_y=self.y, spd_x=spd_x, spd_y=-4))

