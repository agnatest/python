from pprint import pprint
import random

dim = 10
grid = []

def kurti_matrica(dim):
    grid = []
    for _ in range(dim):
        line = []
        for _ in range(dim):
            #state = random.choice([0, 1])
            state = 0
            line.append(state)
        grid.append(line)

    if dim >= 3:
        mid = dim // 2
        #kryzius idedamas 
        grid[mid][mid-1] = 1
        grid[mid][mid] = 1
        grid[mid][mid+1] = 1
        grid[mid-1][mid] = 1
        grid[mid+1][mid] = 1
    return grid

def skaiciuoti_kaimynus(grid, x, y, dim):
    total = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            ni = x + i
            nj = y + j
          
            if 0 <= ni < dim and 0 <= nj < dim:
                total += grid[ni][nj]
        return total

def pritaikyti_4_taisykles(grid, dim):
    new_grid = []
    for _ in range(dim):
        line = []
        for _ in range(dim):
            state = 0
            line.append(state)
        new_grid.append(line)

    for x in range(dim):
        for y in range(dim):
            live_neighbors = skaiciuoti_kaimynus(grid, x, y, dim)
            if grid[x][y] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[x][y] = 0
                else:
                    new_grid[x][y] = 1
            else:
                if live_neighbors == 3:
                    new_grid[x][y] = 1
    return new_grid

def spausdinti(grid, dim):
    for x in range(dim):
        line = ''
        for y in range(dim):
            line += '1' if grid[x][y] == 1 else '0'
        print(line)
    print("\n" + "-" * dim) #atskirti kiekviena generacija bruksnine linija


grid = kurti_matrica(dim)
generations = 5 #kiek  generaciju daryti

for _ in range(generations):
    spausdinti(grid, dim)
    grid = pritaikyti_4_taisykles(grid, dim)