class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        dp = [[-float('inf') for i in range(len(matrix))] for j in range(len(matrix))]
        for index in range(len(matrix)):
            dp[len(matrix)-1][index] = matrix[len(matrix)-1][index]
        for row in range(len(matrix)-2, -1, -1):
            for index in range(len(matrix)):
                left = dp[row+1][max(0, index-1)]
                right = dp[row+1][min(len(matrix)-1, index+1)]
                dp[row][index] = matrix[row][index] + min(dp[row+1][index], left, right);
        return min(dp[0]);

sol = Solution()
print(sol.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
