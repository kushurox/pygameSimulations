"""
Conway's game of life
"""

from copy import deepcopy

import pygame
import pygame as pg
from pygame.time import Clock

k = pg.init()

game_matrix = [[False for _ in range(50)] for __ in range(50)]

mwidth, mheight = len(game_matrix[0]), len(game_matrix)

display = pg.display.set_mode((500, 500))
clock = Clock()

cell_size = 10


def render_matrix(m):
    global display
    r = 0
    t = pg.Surface((cell_size, cell_size))
    t.fill((255, 255, 255))
    for row in m:
        c = 0
        for column in row:
            if column:
                display.blit(t, (c*cell_size, r*cell_size))
            c += 1
        r += 1


def setOn(x, y):
    global game_matrix
    game_matrix[y][x] = True


def setOff(x, y):
    global game_matrix
    game_matrix[y][x] = False


def logic_matrix():
    global game_matrix
    tgm = deepcopy(game_matrix)
    for i in range(0, mheight):
        for j in range(0, mwidth):
            neigh = 0
            left = j-1
            right = j+1
            up = i-1
            down = i+1
            error = False
            if up in (mheight, -1) or down in (mheight, -1):
                error = True
            else:
                neigh += game_matrix[up][j]
                neigh += game_matrix[down][j]
            if left in (mwidth, -1) or right in (mwidth, -1):
                error = True
            else:
                neigh += game_matrix[i][left]
                neigh += game_matrix[i][right]

            if not error:
                neigh += game_matrix[up][left]
                neigh += game_matrix[up][right]
                neigh += game_matrix[down][left]
                neigh += game_matrix[down][right]

            if neigh == 3:
                tgm[i][j] = True
            elif neigh == 2:
                tgm[i][j] = game_matrix[i][j]
            else:
                tgm[i][j] = False
    game_matrix = deepcopy(tgm)


gameOver = True

setOn(11, 10)
setOn(10, 10)
setOn(9, 10)
setOn(8, 10)
setOn(7, 10)

while gameOver:
    dt = clock.tick(5)
    display.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameOver = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x //= cell_size
            y //= cell_size
            setOn(x, y)

    render_matrix(game_matrix)
    logic_matrix()
    pg.display.update()

pg.quit()