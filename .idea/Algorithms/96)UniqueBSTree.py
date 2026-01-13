class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for i in range(n+1)];
        dp[0] = dp[1] = 1;
        for i in range(2, len(dp)):
            for j in range(i):
                dp[i] += (dp[j]*dp[i-1-j]);
        return dp[n];

sol = Solution();
print(sol.numTrees(4))


