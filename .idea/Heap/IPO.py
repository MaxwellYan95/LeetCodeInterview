class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        if k == 0:
            return w;
        if len(profits) == 0 or len(capital) == 0:
            return w;
        canBuy = (capital[0] <= w);
        buy = -1;
        notBuy = -1;
        if canBuy:
            curProfit = profits[0]
            buy = self.findMaximizedCapital(k-1, w+curProfit, profits[1:], capital[1:]);
        notBuy = self.findMaximizedCapital(k, w, profits[1:], capital[1:]);
        return max(notBuy, buy);

sol = Solution();
print(sol.findMaximizedCapital(1, 2, [1, 2, 3], [1, 1, 2]));
print();