class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for i in range(m)];
        for r in range(1, len(m)):
            for c in range(1, len(n)):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]

