class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        # dp[0][i] means not holding stock
        dp = [[0 for i in range(len(prices))] for j in range(2)]
        if len(set(prices)) == 1:
            return 0
        def recur(hold: int, index: int) -> int:
            if index > len(prices)-1:
                return 0
            if dp[hold][index] != 0:
                return dp[hold][index]
            maxPrice = 0;
            if hold == 0:
                temp = recur(1, index+1) - prices[index] - fee
                maxPrice = max(maxPrice, temp);
            else:
                temp = recur(0, index+1) + prices[index]
                maxPrice = max(maxPrice, temp)
            maxPrice = max(maxPrice, recur(hold, index+1))
            dp[hold][index] = maxPrice;
            return dp[hold][index];
        result = recur(0, 0)
        return result
sol = Solution()
print(sol.maxProfit([1,3,2,8,4,9], 2))
