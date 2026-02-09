class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        # you are trying to find the maxSide
        maxSide = 0
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    if row == 0 or col == 0:
                        dp[row][col] = 1;
                    else:
                        # you need to include dp[row-1][col-1] inside min()
                        dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1])+1
                    maxSide = max(maxSide, dp[row][col]);
        return maxSide*maxSide;



sol = Solution()
print(sol.maximalSquare([["1","1","1","0","0"],
                         ["1","1","1","1","1"],
                         ["1","1","1","1","1"],
                         ["1","0","0","1","0"]]))