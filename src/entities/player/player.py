from src.entities.entity import GroundCharacterEntity, ProjectileEntity
import src.entities.spawner as spawner
from random import randrange


class PlayerEntity(GroundCharacterEntity):

    ac1cd = 0
    ac2cd = 0
    ac3cd = 0
    ac4cd = 0

    def work(self):
        self.ac1cd = self.ac1cd - 1 if self.ac1cd else 0
        self.ac2cd = self.ac2cd - 1 if self.ac2cd else 0
        self.ac3cd = self.ac3cd - 1 if self.ac3cd else 0
        self.ac4cd = self.ac4cd - 1 if self.ac4cd else 0

    def action_1(self):
        if not self.ac1cd:
            self.ac1cd = 10
            spd_x = -15 if self.sprite_handler.should_flip else +15
            spawner.spawn_projectile(ProjectileEntity(init_x=self.x, init_y=self.y,
                                                      spd_x=spd_x, spd_y=0, size=10, drop=0.01))

    def action_2(self):
        if not self.ac2cd:
            self.ac2cd = 30
            spd_x = -15 if self.sprite_handler.should_flip else +15
            for i in range(5):
                spd_y = -0.8*(i+1)
                spawner.spawn_projectile(ProjectileEntity(init_x=self.x, init_y=self.y,
                                                          spd_x=spd_x, spd_y=spd_y, drop=0.05))

    def action_3(self):
        if not self.ac3cd:
            self.ac3cd = 40
            for i in range(20):
                spd_x = randrange(-5, 5)
                spd_y = randrange(-10, 0)
                spawner.spawn_projectile(ProjectileEntity(init_x=self.x, init_y=self.y,
                                                          spd_x=spd_x, spd_y=spd_y, drop=0.3))

    def action_4(self):
        spd_x = -10 if self.sprite_handler.should_flip else +10
        if not self.ac4cd:
            self.ac1cd = 3
            spd_y = randrange(-20, 10)*0.1
            spawner.spawn_projectile(ProjectileEntity(init_x=self.x, init_y=self.y,
                                                      spd_x=spd_x, spd_y=spd_y, size=3, drop=0.01, duration=40))

