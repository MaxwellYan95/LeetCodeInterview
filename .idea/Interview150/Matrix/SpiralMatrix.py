class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        visited = set();
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        result = []
        d = 0;
        y = 0;
        x = 0;
        while len(result) != len(matrix)*len(matrix[0]):
            newY = y+dir[d][0];
            newX = x+dir[d][1];
            outOfBounds = newY > len(matrix)-1 \
                          or newX > len(matrix[0])-1 \
                          or newY < 0 or newX < 0;
            if (newX, newY) in visited or outOfBounds:
                d = (d+1) % 4;
                newY = y+dir[d][0];
                newX = x+dir[d][1];
            result.append(matrix[y][x])
            visited.add((x, y))
            y = newY
            x = newX
        return result

sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
