class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        coins.sort()
        self.minCoin = coins[0];
        self.dp = {}
        self.dp[self.minCoin] = 1;
        def recur(money: int):
            result = 0
            if money < self.minCoin:
                return result
            if money in self.dp:
                return self.dp[money];
            if money in coins:
                result += 1;
            for c in coins:
                result += recur(money - c);
            self.dp[money] = result;
            return self.dp[money]
        return recur(amount)

sol = Solution()
print(sol.change(5, [1,2,5]))

        