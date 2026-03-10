from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        stack = deque([entrance]);
        maze[entrance[0]][entrance[1]] = '+'
        result = 0;
        while stack:
            n = len(stack);
            result += 1;
            for i in range(n):
                x, y = stack.popleft();
                for dx, dy in dir:
                    newX = x - dx;
                    newY = y - dy;
                    bounds = newX >= 0 and newX < len(maze) and newY >= 0 and newY < len(maze[0])
                    if not bounds:
                        continue;
                    if maze[newX][newY] == '+':
                        continue;
                    if newX == 0 or newY == 0 or newX == len(maze)-1 or newY == len(maze[0])-1:
                        return result;
                    stack.append([newX, newY]);
                    maze[newX][newY] = '+'
        return -1

sol = Solution()
print(sol.nearestExit([["+",".","+","+","+","+","+"],
                       ["+",".","+",".",".",".","+"],
                       ["+",".","+",".","+",".","+"],
                       ["+",".",".",".",".",".","+"],
                       ["+","+","+","+",".","+","."]],
                    [0,1]))





