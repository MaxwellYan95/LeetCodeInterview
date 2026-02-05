class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[-1 for i in range(len(s)+1)] for j in range(len(s))]
        for index in range(len(s)):
            dp[index][index+1] = s[index];
            dp[index][index] = "";
        def recur(low: int, high: int):
            if dp[low][high] != -1:
                return dp[low][high]
            left = recur(low+1, high)
            right = recur(low, high-1)
            result = 0;
            if s[low] == s[high-1] and dp[low+1][high-1] == s[low+1:high-1]:
                result = s[low:high];
            elif len(left) > len(right):
                result = left
            else:
                result = right
            dp[low][high] = result;
            return dp[low][high]
        return recur(0, len(s))




sol = Solution();
print(sol.longestPalindrome("cbbd"));
