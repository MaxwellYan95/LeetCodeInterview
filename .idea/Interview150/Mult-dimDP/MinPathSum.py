class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
        height = len(grid)-1
        width = len(grid[0])-1
        dp[height][width] = grid[height][width]
        for col in range(width-1, -1, -1):
            dp[height][col] = grid[height][col] + dp[height][col+1]
        for row in range(height-1, -1, -1):
            dp[row][width] = grid[row][width] + dp[row+1][width]
        for row in range(height-1, -1, -1):
            for col in range(width-1, -1, -1):
                dp[row][col] = grid[row][col] + min(dp[row+1][col], dp[row][col+1])
        return dp[0][0]






sol = Solution();
print(sol.minPathSum([[1,2,3],[4,5,6]]))