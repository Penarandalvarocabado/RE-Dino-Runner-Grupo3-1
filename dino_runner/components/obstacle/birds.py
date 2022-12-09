import random

from dino_runner.components.obstacle.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Birds(Obstacle):
    def __init__(self):
        self.list_pos = 0
        self.birds = 0
        super().__init__(BIRD, self.list_pos)
        self.rect.y = random.randint(100, 310)


    def update(self, game_speed, obstacles):
        self.objects_to_draw = BIRD[0] if self.birds < 10 else BIRD[1]
        self.birds += 1
        if self.birds >= 20:
            self.birds = 0
        super().update(game_speed, obstacles) 
