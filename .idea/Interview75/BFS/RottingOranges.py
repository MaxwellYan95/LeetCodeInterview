class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        stack = []
        maxX = len(grid);
        maxY = len(grid[0]);
        noOranges = True
        for row in range(maxX):
            for col in range(maxY):
                if grid[row][col] == 2:
                    stack.append([row,col]);
                    noOranges = False;
                if grid[row][col] == 1:
                    noOranges = False;
        if len(stack) == 0 and noOranges:
            return 0;
        result = 0;
        while stack:
            n = len(stack);
            for _ in range(n):
                x, y = stack.pop(0);
                grid[x][y] = 2;
                for dx, dy in dir:
                    newX = x-dx;
                    newY = y-dy;
                    outBounds = newX < 0 \
                                or newX > maxX-1 \
                                or newY < 0 \
                                or newY > maxY-1
                    if not outBounds and [newX,newY] not in stack:
                        if grid[newX][newY] == 1:
                            stack.append([newX, newY]);
            result += 1;
        for row in range(maxX):
            for col in range(maxY):
                if grid[row][col] == 1:
                    return -1;
        return result-1;

sol = Solution()
print(sol.orangesRotting([[2,2],[1,1],[0,0],[2,0]]))

