class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[m-1][i] = 1;
        for i in range(m):
            dp[i][n-1] = 1;
        for m2 in range(m-2, -1, -1):
            for n2 in range(n-2, -1, -1):
                dp[m2][n2] = dp[m2][n2+1] + dp[m2+1][n2];
        return dp[0][0]