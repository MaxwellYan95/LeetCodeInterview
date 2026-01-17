class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 0:
            return 0;
        dp = {}
        dp[""] = 0;
        for index in range(len(s)):
            dp[s[index]] = 1;
        def recur(subStr: str):
            if subStr in dp:
                return dp[subStr];
            result = 0;
            for index in range(len(subStr)):
                result = max(result, recur(subStr[:index] + "" + subStr[index+1:]))
            midStr = subStr[1: len(subStr)-1];
            if dp[midStr] == len(midStr) and subStr[0] == subStr[len(subStr)-1]:
                result = len(subStr);
            dp[subStr] = result;
            return result;