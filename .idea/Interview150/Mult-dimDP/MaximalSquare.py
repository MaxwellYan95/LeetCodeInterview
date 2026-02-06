class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        dp = [[-1 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        m = len(matrix[0])
        n = len(matrix)
        for i in range(n):
            if matrix[i][m-1] == "0":
                dp[i][m-1] = 0;
            else:
                dp[i][m-1] = 1;
        for i in range(m):
            if matrix[n-1][i] == "0":
                dp[n-1][i] = 0;
            else:
                dp[n-1][i] = 1;
        for m2 in range(m-2, -1, -1):
            for n2 in range(n-2, -1, -1):
                if matrix[n2+1][m2] == matrix[n2][m2+1] == matrix[n2+1][m2+1] == "1":
                    dp[n2][m2] = dp[n2+1][m2]+1;
                else:
                    dp[n2][m2] = max(dp[n2+1][m2], dp[n2][m2+1])
        if dp[0][0] == 0:
            return 0;
        if 2**dp[0][0] < 4:
            return 1;
        return 2**dp[0][0]

sol = Solution()
print(sol.maximalSquare([["1","1","1","0","0"],
                         ["1","1","1","1","1"],
                         ["1","1","1","1","1"],
                         ["1","0","0","1","0"]]))