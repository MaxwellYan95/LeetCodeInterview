class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        visited = [];
        matrix = [[] for i in range(n)];
        number = 1;
        row = 0;
        col = 0;
        rowBounds = [0, n];
        colBounds = [0, n];
        end = rowBounds[0] != rowBounds[1] and colBounds[0] != colBounds[1];
        while end:
            for c in range(colBounds[0], colBounds[1]):
                matrix[row][c] = number;
                number += 1;
            col = colBounds[1]-1;
            for r in range(rowBounds[0], rowBounds[1]):
                matrix[r][col] = number;
                number += 1;
            rowBounds[0] += 1;
            row = rowBounds[1]-1
            if end:
                break;
            for c in range(colBounds[1]-1, colBounds[0]-1, -1):
                matrix[r][col] = number;
                number += 1;
            col = colBounds[0]
            for r in range(rowBounds[1]-1, rowBounds[0]-1, -1):
                matrix[row][c] = number;
                number += 1;
            colBounds[1] -= 1;
            row = rowBounds[0];
            if end:
                break;
        return matrix;

sol = Solution();
print(sol.generateMatrix(4))
