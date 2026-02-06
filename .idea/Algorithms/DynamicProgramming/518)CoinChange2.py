class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        coins.sort();
        # first i coin types
        # money amount j
        dp = [[0 for j in range(amount+1)] for i in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1;
        for j in range(1, amount+1):
            for i in range(1, len(coins)+1):
                c = coins[i-1];
                if c <= j:
                    dp[i][j] = dp[i][j-c] + dp[i-1][j];
                else:
                    dp[i][j] = dp[i-1][j];
        return dp[len(coins)][amount]


sol = Solution()
print(sol.change(5, [1,2,5]))

        