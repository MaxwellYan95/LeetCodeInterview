class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        cond = [-1] * (amount+1);
        if amount == 0:
            return 0;
        for index in range(amount+1):
            for c in coins:
                if (c == index):
                    cond[index] = 1;
                elif (index >= c):
                    if (cond[index-c] > -1):
                        if (cond[index] == -1):
                            cond[index] = cond[index-c]+1;
                        else:
                            cond[index] = min(cond[index], cond[index-c]+1);
        return cond[len(cond)-1];

sol = Solution();
print(sol.coinChange([1,2,5], 11));
print(sol.coinChange([1,2,5], 11));
print();