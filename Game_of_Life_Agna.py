from pprint import pprint
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

DIM = 30
grid = []

def kurti_matrica(dim:int=DIM) -> list[list[int]]:
    grid = []
    for _ in range(dim):
        line = []
        for _ in range(dim):
            #state = random.choice([0, 1])
            state = 0
            line.append(state)
        grid.append(line)
    return grid

def skaiciuoti_kaimynus(grid, x, y, dim):
    total = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx = x + dx
            ny = y + dy
          
            if 0 <= nx < dim and 0 <= ny < dim:
                total += grid[ny][nx]
    return total

def pritaikyti_4_taisykles(grid, dim):
    new_grid = kurti_matrica()

    for y, row in enumerate(grid):
        for x, is_alive in enumerate(row):
            neib = skaiciuoti_kaimynus(grid, x=x, y=y, dim=dim)
            if is_alive:
                new_state = neib in (2, 3)
            else:
                new_state = neib==3
            new_grid[y][x] = int(new_state)
                
    # for x in range(dim):
    #     for y in range(dim):
    #         live_neighbors = skaiciuoti_kaimynus(grid, x, y, dim)
    #         if grid[x][y] == 1:
    #             if live_neighbors < 2 or live_neighbors > 3:
    #                 new_grid[x][y] = 0
    #             else:
    #                 new_grid[x][y] = 1
    #         else:
    #             if live_neighbors == 3:
    #                 new_grid[x][y] = 1

    return new_grid

def spausdinti(grid, dim):
    for row in grid:
        line = "".join([str(item)for item in row])
        print(line)
    print("\n" + "-" * dim) #atskirti kiekviena generacija bruksnine linija

grid = kurti_matrica()

#kryzius idedamas i matrica
if DIM >= 3:
    mid = DIM // 2
    grid[mid][mid-1] = 1
    grid[mid][mid] = 1
    grid[mid][mid+1] = 1
    grid[mid-1][mid] = 1
    grid[mid+1][mid] = 1

generations = 12 #kiek  generaciju daryti

# debuginimui
# count= skaiciuoti_kaimynus(grid, 4, 4, DIM)
# print(count)

#spausdinti terminale
#for _ in range(generations):
#    spausdinti(grid, DIM)
#    grid = pritaikyti_4_taisykles(grid, DIM)


fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='binary')

def animuoti (frame):
    global grid
    grid = pritaikyti_4_taisykles(grid, DIM)
    img.set_data(grid)
    return img,

ani = animation.FuncAnimation(fig, animuoti, frames=generations, interval=500, blit=True)

plt.show()