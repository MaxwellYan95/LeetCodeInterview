class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        result = 0
        for row in range(n):
            for col in range(n):
                equal = True
                for i in range(n):
                    if grid[row][i] != grid[i][col]:
                        equal = False;
                        break;
                if equal:
                    result += 1;
        return result

sol = Solution()
print(sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))

