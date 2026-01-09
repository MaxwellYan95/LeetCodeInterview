from collections import defaultdict

class Solution:

    mapping = defaultdict(int);

    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0;
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1;
        dp[1] = 1;
        for i in range(2, len(s)+1):
            oneDigit = int(s[i-1]);
            twoDigit = int(s[i-2: i]);
            if oneDigit != 0:
                dp[i] += dp[i-1]
            if 10 <= twoDigit <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)];

sol = Solution()
print(sol.numDecodings("226"))
print(sol.numDecodings("06"))