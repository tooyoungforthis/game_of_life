import game
import window
import numpy as np
import pygame 
pygame.init()

RES = WIDTH, HEIGHT = 1200, 800
TILE = 20
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 10

surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

start_figure = []



current_grid = np.zeros((W,H))
start_figure = window.start_figure()
for dot in start_figure:         
    current_grid[dot] = 1

while True:

    surface.fill(pygame.Color('Black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # рисуем сетку
    [pygame.draw.line(surface, pygame.Color('dimgray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color('dimgray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]

    for x in range(W):
        for y in range(H):
            if current_grid[x][y] == 1:
                pygame.draw.rect(surface, pygame.Color('forestgreen'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2 ))
                
    
    current_grid = game.next_step(current_grid)


    pygame.display.flip()
    clock.tick(FPS)

