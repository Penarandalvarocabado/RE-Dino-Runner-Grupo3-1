import pygame

from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

import random

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_app = random.randint(1, 3)
            if obstacle_app == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif obstacle_app == 2:
                self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                # pygame.time.delay(380)
                # game.playing = False
                # break
                pygame.time.delay(100)
                self.obstacles = []

                game.player_heart_manager.reduce_heart()
                if game.player_heart_manager.heart_count > 0:
                    game.playershield = True
                    game.player.show_text = False
                    start_time = pygame.time.get_ticks()
                    game.player.shield_time_up = start_time + 1000
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self, self_1):
        self.obstacles = []
