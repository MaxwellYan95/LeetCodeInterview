import numpy as np

def numIslands(grid: list[list[str]]) -> int:
    markGrid = np.empty((len(grid), len(grid[0])))
    for x in len(grid):
        for y in len(grid[0]):
            markGrid[x][y] = False

    def identify(grid: list[list[str]], x: int, y: int):
        if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
            return
        elif (grid[x][y] == 0):
            return
        elif (markGrid[x][y] == True):
            return
        else:
            marked[x][y] = True
            identify(x+1, y)
            identify(x-1, y)
            identify(x, y+1)
            identify(x, y-1)

    result = 0

    for x in len(grid):
        for y in len(grid[0]):
            if (markGrid[x][y] == False and grid[x][y] == 1):
                identify(grid, x, y)
                result = result + 1

    return result

print(numIslands([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]))