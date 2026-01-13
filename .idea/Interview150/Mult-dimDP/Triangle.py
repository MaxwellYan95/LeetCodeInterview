class Solution:

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [[-1 for i in range(len(triangle))] for j in range(len(triangle))]
        col = 0;
        for n in triangle[len(triangle)-1]:
            dp[len(triangle)-1][col] = n;
            col += 1;
        col = 0;
        for row in range(len(triangle)-2, -1, -1):
            for c in range(0, len(triangle[row])):
                dp[row][c] = triangle[row][c] + min(dp[row+1][c], dp[row+1][c+1]);
        return dp[0][0]





