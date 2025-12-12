# Day 4: Printing Department
# Part 1: 1437
# Part 2: 8765

import lib

def run():
    grid = process_input()

    tot = 0
    while True:
        n_map = get_map(grid)
        
        rolls = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '@' and n_map[i][j] < 4:
                    rolls += 1
                    grid[i] = grid[i][:j] + '.' + grid[i][j+1:]
        tot += rolls
        print(rolls)

        if rolls == 0:
            print(tot)
            break



def inc_cell(n_map, row, col):
    try:
        if row < 0 or col < 0:
            return
        n_map[row][col] += 1
    except:
        pass



def get_map(grid):
    n_map = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                inc_cell(n_map, i-1, j-1)
                inc_cell(n_map, i-1, j)
                inc_cell(n_map, i-1, j+1)
                inc_cell(n_map, i, j-1)
                inc_cell(n_map, i, j+1)
                inc_cell(n_map, i+1, j-1)
                inc_cell(n_map, i+1, j)
                inc_cell(n_map, i+1, j+1)
    return n_map



def process_input():
    input = lib.read_input('input4.txt')
    return input



if __name__ == '__main__':
    run()