from src.entities.entity import GroundCharacterEntity, ProjectileEntity
import src.entities.spawner as spawner


class PlayerEntity(GroundCharacterEntity):

    ac1cd = 0
    ac2cd = 0

    def work(self):
        self.ac1cd = self.ac1cd - 1 if self.ac1cd else 0
        self.ac2cd = self.ac2cd - 1 if self.ac2cd else 0

    def action_1(self):
        if not self.ac1cd:
            self.ac1cd = 10
            spd_x = -15 if self.sprite_handler.should_flip else +15
            spawner.spawn_projectile(ProjectileEntity(init_x=self.x, init_y=self.y, spd_x=spd_x, spd_y=-1, size=10))

    def action_2(self):
        if not self.ac2cd:
            self.ac2cd = 30
            spd_x = -15 if self.sprite_handler.should_flip else +15
            spawner.spawn_projectile(ProjectileEntity(init_x=self.x, init_y=self.y, spd_x=spd_x, spd_y=0))
            spawner.spawn_projectile(ProjectileEntity(init_x=self.x, init_y=self.y, spd_x=spd_x, spd_y=-3))
            spawner.spawn_projectile(ProjectileEntity(init_x=self.x, init_y=self.y, spd_x=spd_x, spd_y=-6))




