import pygame
import numpy as np
pygame.init()

RES = WIDTH, HEIGHT = 1200, 800
TILE = 20
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 10

grid = np.zeros((W, H))

surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

def start_figure():
    
    while True:
        
        flag = False
        figure = []
        surface.fill(pygame.Color('Black'))
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                flag = True
                           
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                column = pos[1] // TILE
                row = pos[0] // TILE
                
                if grid[row][column] == 0:
                    grid[row][column] = 1
                else:
                    grid[row][column] = 0
                
                

        # рисуем сетку
        [pygame.draw.line(surface, pygame.Color('dimgray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
        [pygame.draw.line(surface, pygame.Color('dimgray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]


        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i][j] == 1:
                    figure.append((i, j))
                    pygame.draw.rect(surface, pygame.Color('forestgreen'), (i * TILE + 2, j * TILE + 2, TILE - 2, TILE - 2 ))
        


        pygame.display.flip()
        clock.tick(FPS)  

        if flag:
            return figure
      
