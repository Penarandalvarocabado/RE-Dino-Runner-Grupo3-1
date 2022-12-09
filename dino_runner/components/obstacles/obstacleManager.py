import pygame
import random

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacle_type_list = [Bird(), Cactus()]
            self.obstacles.append(random.choice(self.obstacle_type_list))
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                # pygame.time.delay(380)
                # game.playing = False
                # break
                if not game.player.shield:
                    pygame.time.delay(100)
                    self.obstacles = []

                    game.player_heart_manager.reduce_heart()
                    if game.player_heart_manager.heart_count > 0:
                        #self.coll_sound.play(2)
                        game.player.shield = True
                        game.player.show_text = False
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time + 1000
                        #pygame.mixer.Sound.play(self.death_sound)
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
                        break
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self, self_1):
        self.obstacles = []
