class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        m = len(matrix[0])
        n = len(matrix)
        maxSide = 0;
        for n2 in range(n):
            for m2 in range(m):
                if matrix[n2][m2] == "1":
                    if n2 == 0 or m2 == 0:
                        dp[n2][m2] = 1;
                    else:
                        dp[n2][m2] = min(dp[n2-1][m2], dp[n2][m2-1], dp[n2-1][m2-1]) + 1;
                    maxSide = max(maxSide, dp[n2][m2])
        return maxSide*maxSide;



sol = Solution()
print(sol.maximalSquare([["1","1","1","0","0"],
                         ["1","1","1","1","1"],
                         ["1","1","1","1","1"],
                         ["1","0","0","1","0"]]))