class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid);
        n = len(obstacleGrid[0]);
        if obstacleGrid[m-1][n-1] == 1:
            return 0;
        dp = [[0 for i in range(n)] for j in range(m)];

        for y in range(m-1, -1, -1):
            if obstacleGrid[y][n-1] == 1:
                break;
            dp[y][n-1] = 1;
        start = 1;
        for x in range(n-1, -1, -1):
            if obstacleGrid[m-1][x] == 1:
                break;
            dp[m-1][x] = 1;
        for x in range(n-2, -1, -1):
            for y in range(m-2, -1, -1):
                if obstacleGrid[y][x] != 1:
                    dp[y][x] = dp[y+1][x] + dp[y][x+1];
        return dp[0][0]

sol = Solution();
print(sol.uniquePathsWithObstacles([[0,1,0,0]]))