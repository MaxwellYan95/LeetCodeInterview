from collections import defaultdict

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0 for i in range(high+1)];
        first = min(zero, one);
        dp[zero] += 1;
        dp[one] += 1;
        for i in range(first+1, high+1):
            dp[i] += dp[i-zero] + dp[i-one];
        result = 0;
        for i in range(low, high+1):
            result += dp[i]
        return result % (10**9 + 7)

sol = Solution()
print(sol.countGoodStrings(2, 3, 1, 2))


