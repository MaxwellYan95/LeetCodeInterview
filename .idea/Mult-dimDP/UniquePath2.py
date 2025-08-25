class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        dp = [[-1 for j in obstacleGrid[0]] for i in obstacleGrid];
        maxCol = len(obstacleGrid[0])-1;
        maxRow = len(obstacleGrid)-1;
        for i in range(len(obstacleGrid)):
            element = dp[i][maxCol];
            spot = obstacleGrid[i][maxCol];
            if spot == 1:
                dp[i][maxCol] = 0;
            else:
                dp[i][maxCol] = 1;
        for j in range(len(obstacleGrid[0])):
            element = dp[maxRow][j];
            spot = obstacleGrid[maxRow][j];
            if spot == 1:
                dp[maxRow][j] = 0;
            else:
                dp[maxRow][j] = 1;
        for i in range(len(obstacleGrid)-2, -1, -1):
            for j in range(len(obstacleGrid[0])-2, -1, -1):
                element = dp[i][j];
                spot = obstacleGrid[i][j];
                if spot == 1:
                    dp[i][j] = 0;
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1];
        return dp[0][0];
sol = Solution();
print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]));

