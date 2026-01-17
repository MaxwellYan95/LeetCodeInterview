class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 0:
            return 0;
        dp = [[-1 for high in range(len(s)+1)] for low in range(len(s))]
        for index in range(len(s)):
            dp[index][index+1] = 1;
            dp[index][index] = 0;
        def recur(low: int, high: int):
            if dp[low][high] != -1:
                return dp[low][high]
            midSub = recur(low+1, high-1);
            result = 0;
            if s[low] == s[high-1] and midSub:
                result = len(s[low:high])
            else:
                for lo in range(0, low):
                    for hi in range(0, high):
                        result = max(result, recur(lo, hi))
            dp[low][high] = result;
            return result;
