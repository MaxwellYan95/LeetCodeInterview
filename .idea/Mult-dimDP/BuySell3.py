from collections import defaultdict;
class Solution:

    # Max profit for one transactions
    def createChart(self, prices: list[int]) -> dict:
        dp = defaultdict(int);
        for begin in range(len(prices)-1):
            minimum = prices[begin];
            for end in range(begin+1, len(prices)):
                prevDP = dp[(begin, end-1)];
                betterDP = prices[end]-minimum;
                if prevDP > 0 or betterDP > 0:
                    dp[(begin, end)] = max(prevDP, betterDP);
                minimum = min(minimum, prices[end]);
        return dp;


    def maxProfit(self, prices: list[int]) -> int:
        maximum = 0;
        dp = self.createChart(prices);
        for end1 in range(1, len(prices)):
            trans1 = dp[(0, end1)];
            beg2 = end1+1;
            if end1 == len(prices)-1:
                maximum = max(trans1, maximum);
            else:
                for end2 in range(beg2+1, len(prices)):
                    trans2 = dp[(beg2, end2)];
                    maximum = max(trans2+trans1, maximum);
        return maximum;

sol = Solution();
grid = sol.createChart([3,3,5,0,0,3,1,4]);
print(sol.maxProfit([3,3,5,0,0,3,1,4]));
print(sol.maxProfit([1,2,3,4,5]));
print(sol.maxProfit([1, 2]));