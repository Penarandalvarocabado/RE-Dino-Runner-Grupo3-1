import pygame 
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacleManager import ObstacleManager
from dino_runner.components.score_menu.text_utils import *
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.components.powerups.power_up_manager import PowerUpManager
#from dino_runner.utils import text_utils

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        #self.music = 0
        self.running = True
        self.death_count = 0
        self.player_heart_manager = PlayerHeartManager()
        self.power_up_manager = PowerUpManager()

    def run(self):
        self.obstacle_manager.reset_obstacles(self)
        self.player_heart_manager.resert_hearts()
        self.points = 0
        self.game_speed = 20
        self.power_up_manager.resert_power_ups(self.points)
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        # pygame.quit()

    #def excute(self):
        #self.play_music()
        #while self.game_running:
            #if not self.playing:
                #self.show_menu

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((0, 255, 127))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score()
        self.player_heart_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def score(self):
        self.points += 1

        if self.points % 100 == 0:
            self.game_speed += 1

        score, score_rect = get_score_element(self.points)
        self.screen.blit(score, score_rect)
        self.player.check_invincibility(self.screen)

    def show_menu(self):
        self.running = True

        skyblue_color = (135, 206, 235)
        self.screen.fill(skyblue_color)

        self.print_menu_elemnts(self.death_count)
        pygame.display.update()

        self.handle_key_events_on_menu()

    def print_menu_elemnts(self, death_count = 0):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if death_count == 0:
            text, text_rect = get_centered_message('PRESS ANY KEY TO START')
            self.screen.blit(text, text_rect)
        elif death_count > 0:
            text, text_rect = get_centered_message('PRESS ANY KEY TO RESTART')
            score, score_rect = get_centered_message('YOUR SCORE: ' + str(self.points), height = half_screen_height + 50)
            self.screen.blit(score, score_rect)
            self.screen.blit(text, text_rect)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("DINO: GOOD BYE!!")
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    #def play_music(self):
        #if self.music == 0:
            #pygame.mixer.music.load("assets/sounds/OST-23.mp3")
            #pygame.mixer.music.play(-1)
            #pygame.mixer.music.set_volume(0.15)
        #elif self.music == 1:
            #pygame.mixer.music.load("assets/sounds/01-Running-About.mp3")
            #pygame.mixer.music.play(-1)
            #pygame.mixer.music.set_volume(0.5)
            #if self.death_count == 4:
                #pygame.mixer.music.stop()
