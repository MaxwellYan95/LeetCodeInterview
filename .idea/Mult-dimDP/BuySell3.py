from collections import defaultdict;
class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        transaction1, transaction2 = float('inf'), float('inf')
        profit1, profit2 = 0, 0

        for i in prices:
            transaction1 = min(transaction1, i)
            profit1 = max(profit1, i - transaction1)

            transaction2 = min(transaction2, i-profit1)
            profit2 = max(profit2, i - transaction2)
        return profit2

sol = Solution();
grid = sol.createChart([3,3,5,0,0,3,1,4]);
print(sol.maxProfit([3,3,5,0,0,3,1,4]));
print(sol.maxProfit([1,2,3,4,5]));
print(sol.maxProfit([1, 2]));