class Solution:
    # minimum value for each subarray (arr[begin:])
    # 2d minimum array
    def minimumIndex(self, price: list[int]) -> list[int]:
        minimums = [[float('inf') for i in range(len(price))] for j in range(len(price))];
        for index in range(0, len(price)):
            minimums[index][index] = price[index];
        for begin in range(len(price)-1):
            for end in range(begin+1, len(price)):
                prevMin = minimums[begin][end-1];
                minimums[begin][end] = min(prevMin, price[end]);
        return minimums;


    # Max profit for one transactions
    def createChart(self, prices: list[int]) -> int:
        minimums = self.minimumIndex(prices);
        dp = [[0 for j in range(len(prices))] for i in range(len(prices))];
        for begin in range(len(prices)-1):
            for end in range(begin+1, len(prices)):
                prevDP = dp[begin][end-1];
                curMinimum = minimums[begin][end];
                dp[begin][end] = max(prices[end]-curMinimum, dp[begin][end-1]);
        return dp;


    def maxProfit(self, prices: list[int]) -> int:
        maximum = 0;
        dp = self.createChart(prices);
        for end1 in range(1, len(dp[0])):
            trans1 = dp[0][end1];
            beg2 = end1+1;
            if end1 == len(dp[0])-1:
                maximum = max(trans1, maximum);
            else:
                for end2 in range(beg2+1, len(dp[0])):
                    trans2 = dp[beg2][end2];
                    maximum = max(trans2+trans1, maximum);
        return maximum;

sol = Solution();
grid = sol.createChart([3,3,5,0,0,3,1,4]);
print(sol.maxProfit([3,3,5,0,0,3,1,4]));
print(sol.maxProfit([1,2,3,4,5]));