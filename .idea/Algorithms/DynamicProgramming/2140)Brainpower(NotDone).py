class Solution:

    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions);
        dp = [0 for i in range(n)];
        maxRes = 0;
        for index in range(n):
            i = index;
            result = 0;
            while i < n:
                result += questions[i][0]
                dp[i] = max(dp[i], result)
                maxRes = max(maxRes, dp[i])
                i += (questions[i][1]+1);
        return maxRes

sol = Solution()
print(sol.mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]))