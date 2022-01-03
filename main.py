import math
import pygame

import ray_casting
from Settings import *
from Player import Player
from map import world_map
from ray_casting import ray_crasting

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    ray_casting.ray_crasting(sc, player.pos, player.angle)

    pygame.draw.circle(sc, GREEN, player.pos, 12)
    pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),
                                             player.y + WIDTH * math.sin(player.angle)))
    for x, y in world_map:
        pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(FPS)
