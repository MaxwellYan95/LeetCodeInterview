class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2))] for j in range(len(text1))]
        dp[0][0] = 1 if text1[0] == text2[0] else 0;
        for i in range(1, len(text2)):
            dp[0][i] = 1 if text1[0] == text2[0] else dp[0][i-1];
            dp[0][i] = 1 if text1[0] == text2[i] else dp[0][i-1];
        for j in range(1, len(text1)):
            dp[j][0] = 1 if text1[0] == text2[0] else dp[j-1][0];
            dp[j][0] = 1 if text1[j] == text2[0] else dp[j-1][0];
        for i in range(1, len(text2)):
            for j in range(1, len(text1)):
                increment = 1 if text1[j] == text2[i] else 0
                dp[j][i] = max(dp[j][i-1], dp[j-1][i], increment + dp[j-1][i-1]);
        return dp[len(text1)-1][len(text2)-1]



sol = Solution()
print(sol.longestCommonSubsequence("bl", "yby"))
