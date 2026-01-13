class Solution:
    def numTrees(self, n: int) -> int:
        dp = [[-1 for i in range(n+1)] for i in range(n)];
        for low in range(n):
            dp[low][low+1] = 1;
        for low in range(n-1):
            dp[low][low+2] = 2;
        for high in range(3, n+1):
            low = 0
            high2 = high
            while high2 <= n:
                dp[low][high2] = dp[low+1][high2] + dp[low][high2-1] + dp[low+1][high2-1];
                low += 1;
                high2 += 1;
        return dp[0][n];


sol = Solution();
print(sol.numTrees(4))


