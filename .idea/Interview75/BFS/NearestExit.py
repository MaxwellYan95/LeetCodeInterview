class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:

    def neighborhood(self, maze: list[list[str]]):
        dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for x in range(len(maze)):
            for y in range(len(maze[0])):
                if maze[x][y] == '.':
                    for dx, dy in dir:
                        newX = x + dx;
                        newY = y + dy;



