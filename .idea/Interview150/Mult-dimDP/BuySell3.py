from collections import defaultdict;
class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        size = len(prices);
        n = len(prices);
        # i3 --> transactions left (i3 == 2 means 2 transactions left)
        # i2 --> you are allowed to buy or not (you cannot hold 2 stocks simultaneously)
        # i1 --> sublist of prices
        dp = [[[None for i3 in range(3)] for i2 in range(2)] for i1 in range(n)]
        def dfs(i, can_buy, transactions_left):

            if i == len(prices) or transactions_left == 0:
                return 0

            if dp[i][can_buy][transactions_left] is not None:
                return dp[i][can_buy][transactions_left]

            if can_buy:
                ##here you can either buy or not buy
                #if you buy, you subtract current price(cuz you paid) and recursively call sell
                ##why not doing trancsation-1 in case of buy
                ##Because a transaction is only completed when you SELL, not when you buy.
                result =  max(
                    -prices[i] + dfs(i+1, False, transactions_left),  # buy
                    dfs(i+1, True, transactions_left)                 # not buy
                )
            else:
                result =  max(
                    prices[i]+dfs(i+1, True, transactions_left-1),
                    dfs(i+1, False, transactions_left)
                )

            dp[i][can_buy][transactions_left] = result
            return result

        return dfs(0, True, 2)

sol = Solution();
grid = sol.createChart([3,3,5,0,0,3,1,4]);
print(sol.maxProfit([3,3,5,0,0,3,1,4]));
print(sol.maxProfit([1,2,3,4,5]));
print(sol.maxProfit([1, 2]));