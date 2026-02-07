class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        width = len(mat[0])
        height = len(mat)
        self.dp = mat.copy()
        self.dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        self.visited = [[False for i in range(width)] for j in range(height)]

        def recur(row: int, col: int):
            if self.dp[row][col] == 0:
                return self.dp[row][col];
            if self.visited[row][col] == True:
                return self.dp[row][col];
            self.visited[row][col] = True
            result = float('inf')
            for x, y in self.dir:
                newRow = row + x;
                newCol = col + y;
                if newCol >= 0 and newRow >= 0 \
                        and newCol < width and newRow < height:
                    result = min(result, recur(newRow, newCol)+1);
            self.dp[row][col] = result
            return self.dp[row][col]

        for row in range(height):
            for col in range(width):
                if self.visited[row][col] == False:
                    recur(row,col)
        return self.dp

sol = Solution()
print(sol.updateMatrix([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]))