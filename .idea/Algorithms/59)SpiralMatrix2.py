class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        if n == 1:
            return [[1]]
        num = 1;
        x = 0;
        y = 0;
        visited = [];
        matrix = [[0 for i in range(n)] for j in range(n)]
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        dirInd = 0;
        while True:
            if (x,y) in visited:
                break;
            matrix[y][x] = num;
            num += 1;
            visited.append((x,y))
            newX = x + dir[dirInd][0];
            newY = y + dir[dirInd][1];
            bounds = newX >= 0 and newX < n and newY >= 0 and newY < n;
            if (newX, newY) in visited or not bounds:
                dirInd = (dirInd+1) % 4;
                newX = x + dir[dirInd][0];
                newY = y + dir[dirInd][1];
            x = newX;
            y = newY;
        return matrix

sol = Solution();
print(sol.generateMatrix(2))
