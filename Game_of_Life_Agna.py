from pprint import pprint
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse

def kurti_matrica(dim: int) -> list[list[int]]:
    grid = []
    for _ in range(dim):
        line = []
        for _ in range(dim):
            state = random.choice([0, 1])
            #state = 0
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
    new_grid = kurti_matrica(dim)

    for y, row in enumerate(grid):
        for x, is_alive in enumerate(row):
            neib = skaiciuoti_kaimynus(grid, x=x, y=y, dim=dim)
            if is_alive:
                new_state = neib in (2, 3)
            else:
                new_state = neib == 3
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

def main(dim, generations):
    grid = kurti_matrica(dim)

    #kryzius idedamas i matrica
    if dim >= 3:
        mid = dim // 2
        grid[mid][mid-1] = 1
        grid[mid][mid] = 1
        grid[mid][mid+1] = 1
        grid[mid-1][mid] = 1
        grid[mid+1][mid] = 1

    fig, ax = plt.subplots()
    img = ax.imshow(grid, cmap='binary')

    def animuoti(frame):
        nonlocal grid
        grid = pritaikyti_4_taisykles(grid, dim)
        img.set_data(grid)
        return img,

    ani = animation.FuncAnimation(fig, animuoti, frames=generations, interval=50, blit=True)
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Game Of Life')
    parser.add_argument('--dim', type=int, required=False, default=30, help='Matricos dimensija vienetais')
    parser.add_argument('--gen', type=int, required=False, default=12, help='Generacijos skaicius')
    args = parser.parse_args()

    main(args.dim, args.gen)