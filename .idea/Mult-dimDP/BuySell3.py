class Solution:
    # minimum value for each subarray
    def minimumIndex(self, price: list[int]) -> list[int]:
        minimums = [price[0]];
        for index in range(1, len(price)):
            minimums.append(min(minimums[index-1], price[index]));
        return minimums;


    # Max profit for one transactions
    def createChart(self, prices: list[int]) -> int:
        minimums = self.minimumIndex(prices);
        dp = [[0 for j in range(len(prices))] for i in range(len(prices))];
        for begin in range(len(prices)-1):
            for end in range(begin+1, len(prices)):
                prevDP = dp[begin][end-1];
                curMinimum = minimums[begin];
                dp[begin][end] = max(prices[end]-curMinimum, dp[begin][end-1]);
        return dp




    #def maxProfit(self, prices: list[int]) -> int:

sol = Solution();
grid = sol.createChart([3,3,5,0,0,3,1,4]);
print();