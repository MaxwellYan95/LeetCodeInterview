import math


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = [-math.inf for p in prices]
        profit[len(prices)-1] = 0
        for i in range(len(prices)-2, -1, -1):
            maxP = 0;
            for j in range(i+1, len(prices)):
                p = min(prices[i]-prices[j], 0)
                p
            profit[i] = max()
