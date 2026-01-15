class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-1 for i in range(n+1)];
        dp[1] = 1;
        dp[2] = 1;
        for i in range(3, n+1):
            maxRes = 0;
            twoNum = j*(i-j)
            for j in range(2, i):
                maxRes = max(j * dp[i-j], twoNum, maxRes);
            dp[i] = maxRes;
        return dp[n]

print()
