from dino_runner.components.obstacle.obstacle import Obstacle
import random

class Birds(Obstacle):
    def __init__(self, image):
        self.type = random .randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 200
