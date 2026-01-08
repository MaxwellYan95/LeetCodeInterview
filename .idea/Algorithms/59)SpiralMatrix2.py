class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        row, col = 0, 0;
        matrix = [[0]*n for i in range(n)]
        def checkBounds(row: int, col: int, n: int) -> bool:
            return row >= 0 and row < n and col >= 0 and col < n;
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dirIndex = 0;
        for num in range(1, n*n+1):
            matrix[row][col] = num;
            dRow = direction[dirIndex][0];
            dCol = direction[dirIndex][1];
            changeDir = not checkBounds(row+dRow, col+dCol, n) \
                        or matrix[row+dRow][col+dCol] != 0
            if changeDir:
                dirIndex = (dirIndex + 1) % 4
            dRow = direction[dirIndex][0];
            dCol = direction[dirIndex][1];
            row += dRow;
            col += dCol;
        return matrix;

sol = Solution();
print(sol.generateMatrix(4))
