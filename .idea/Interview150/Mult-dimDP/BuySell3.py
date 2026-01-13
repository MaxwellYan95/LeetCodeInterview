from collections import defaultdict;
class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        dp = [[[-1 for i1 in range(0, 2)] for i2 in range(0, 3)] for i3 in range(len(prices))]
        length = len(prices);
        for transactions in range(0, 3):
            dp[length-1][transactions][0] = 0;
        for transactions in range(0, 3):
            dp[length-1][transactions][1] = prices[length-1];
        for day in range(length):
            dp[day][2][0] = 0;
        def recur(day: int, transNum: int, hasStock: int):
            if dp[day][transNum][hasStock] != -1:
                return dp[day][transNum][hasStock];
            result = 0;
            if hasStock == 0:
                result = max(recur(day+1, transNum+1, 1) - prices[day],
                             recur(day+1, transNum, hasStock));
            else:
                result = max(recur(day+1, transNum, 0) + prices[day],
                             recur(day+1, transNum, hasStock));
            dp[day][transNum][hasStock] = result
            return result;

        return recur(0, 0, 0);

sol = Solution()
print(sol.maxProfit([3,3,5,0,0,3,1,4]))
