class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        width = len(mat[0])
        height = len(mat)
        dp = [[float('inf') for i in range(width)] for j in range(height)]
        for row in range(height):
            for col in range(width):
                if mat[row][col] == 0:
                    dp[row][col] = 0
        dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for row in range(height):
            for col in range(width):
                if dp[row][col] == float('inf'):
                    result = dp[row][col]
                    for x, y in dir:
                        newRow = row + x;
                        newCol = col + y;
                        if newCol >= 0 and newRow >= 0 \
                            and newCol < width and newRow < height:

sol = Solution()
print(sol.updateMatrix([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]))