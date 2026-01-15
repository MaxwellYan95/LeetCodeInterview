class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-1 for i in range(n+1)];
        dp[1] = 1;
        dp[2] = 1;
        for i in range(3, n+1):
            maxRes = 0;
            for j in range(2, i):
                maxRes = max(j * dp[i-j], j*(i-j), maxRes);
            dp[i] = maxRes;
        return dp[n]

print()
