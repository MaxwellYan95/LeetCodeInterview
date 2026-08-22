class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set();
        col = set();
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                val = matrix[y][x];
                if val == 0:
                    row.add(y)
                    col.add(x)
        for y in range(len(matrix)):
            for x in col:
                matrix[y][x] = 0;
        for x in range(len(matrix[0])):
            for y in row:
                matrix[y][x] = 0;