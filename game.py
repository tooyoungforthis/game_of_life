"""
Game of Life
Правила: 
если клетка в состоянии "1" и сумма соседей = 2 или 3, то клетка остается в состоянии "1"
иначе переходит в состояние "0"
если клетка в состоянии "0" и сумма соседей = 3, то клетка переходит в состояние "1"
иначе переходит остоется в состоянии "0"
"""

import numpy as np 
import random 

def neighbors_counting(grid): 
    """
    Объяснение алгоритма для клетки с позицией (i, j):
    для i - той строки находим сумму i - 1, i, i + 1 строк
    для верхней строки - сумма i, i + 1  
    для нижней строки - сумма i, i - 1  
    затем находим сумму соседей(i, j) клетки, как сумму: (i, j - 1),  (i, j + 1)  
    для левого столбца - сумма  j + 1
    для правого столбца - сумма j - 1, j + 1
    """

    summ_of_rows = np.zeros(grid.shape)

    for i in range(grid.shape[0]):
        if i == 0:
            summ_of_rows[i, :] = grid[i, :] + grid[i + 1, :]
        elif i == grid.shape[0] - 1:
            summ_of_rows[i, :] = grid[i - 1, :] + grid[i, :] 
        else:
            summ_of_rows[i, :] = grid[i - 1, :] + grid[i, :] + grid[i + 1, :]
    

    summ_of_columns = np.zeros(grid.shape)
    for j in range(grid.shape[1]):
        if j == 0:
            summ_of_columns[:, j] = summ_of_rows[:, j] + summ_of_rows[:, j + 1] 
        elif j == grid.shape[1] - 1:
            summ_of_columns[:, j] = summ_of_rows[:, j - 1] + summ_of_rows[:, j]
        else:
            summ_of_columns[:, j] = summ_of_rows[:, j - 1] + summ_of_rows[:, j] + summ_of_rows[:, j + 1]

    return summ_of_columns

def next_step(grid):
    next_grid = np.zeros(grid.shape)
    neighbor_grid = neighbors_counting(grid)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 0:
                if neighbor_grid[i, j]  == 3:
                    next_grid[i, j] = 1
                else:
                    next_grid[i, j] = 0
            if grid[i, j] == 1:
                neighbor_grid[i, j] -= 1
                if neighbor_grid[i, j] in [2, 3]:
                    next_grid[i, j] = 1
                else: 
                    next_grid[i, j] = 0

    return next_grid        

def main():
    start_grid = np.zeros((10,10))
    figure = ((1, 1), (2, 2), (3, 0), (3, 1), (3, 2))

    for dot in figure:
        start_grid[dot] = 1

    
    for i in range(4):
        start_grid = next_step(start_grid)
    print(start_grid)



if __name__ == "__main__":
    main()