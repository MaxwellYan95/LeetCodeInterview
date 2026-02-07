class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        width = len(mat[0])
        height = len(mat)
        dp = [[float('inf') for i in range(width)] for j in range(height)]
        visited = [[False for i in range(width)] for j in range(height)]
        for r in range(height):
            for c in range(width):
                if mat[r][c] == 0:
                    dp[r][c] = 0
        def recur(row: int, col: int):
            if row > height-1 or col > width-1 or row < 0 or col < 0:
                return float('inf');
            if dp[row][col] < float('inf'):
                return dp[row][col];
            if visited[row][col] == True:
                return dp[row][col];
            visited[row][col] = True;
            result = dp[row][col]
            if row > 0:
                result = min(result, recur(row-1, col)+1)
            if row < height-1:
                result = min(result, recur(row+1, col)+1)
            if col > 0:
                result = min(result, recur(row, col-1)+1)
            if col < width-1:
                result = min(result, recur(row, col+1)+1)
            dp[row][col] = result
            return dp[row][col]
        for r in range(height):
            for c in range(width):
                if visited[r][c] == False:
                    recur(r,c)
        return dp

sol = Solution()
print(sol.updateMatrix([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]))