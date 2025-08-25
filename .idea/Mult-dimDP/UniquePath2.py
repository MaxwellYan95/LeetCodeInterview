class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        dp = [[-1 for j in obstacleGrid[0]] for i in obstacleGrid];
        def recur(x, y) -> int:
            if (x == len(obstacleGrid[0])-1 and y == len(obstacleGrid)-1):
                return 1;
            if dp[y][x] != -1:
                return dp[y][x];
            if (obstacleGrid[y][x] == 1):
                dp[y][x] = 0;
            down = 0;
            right = 0;
            if y+1 > len(obstacleGrid)-1:
                down = recur(x, y+1);
            if x+1 > len(obstacleGrid[0])-1:
                right = recur(x+1, y);
            dp[y][x] = down + right;
            return down + right;
        return recur(0, 0);
sol = Solution();
print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]));

