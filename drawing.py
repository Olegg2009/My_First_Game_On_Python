from Settings import *
import pygame
from ray_casting import ray_casting

class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
    def background(self):
        pygame.draw.rect(self.sc, SKY, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_angle, player_pos):
        ray_casting(self.sc, player_angle, player_pos)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, False, WHITE)
        self.sc.blit(render, FPS_POSE)

