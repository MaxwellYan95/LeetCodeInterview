class Solution:

    def mostPoints(self, questions: list[list[int]]) -> int:
        dp = [0 for i in questions];
        for index in range(len(questions)):
            temp = questions[index][0]
            dp[index] = max(dp[index], temp)
            prevIndex = index
            nextIndex = index + questions[index][1] + 1;
            while nextIndex < len(questions):
                points = questions[nextIndex][0]
                dp[nextIndex] = max(dp[nextIndex], points + dp[prevIndex]);
                prevIndex = nextIndex
                nextIndex = prevIndex + questions[prevIndex][1] + 1;
        return max(dp);

sol = Solution()
print(sol.mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]))