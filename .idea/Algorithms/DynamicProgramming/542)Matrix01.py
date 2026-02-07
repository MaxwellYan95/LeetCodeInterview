class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        width = len(mat[0])
        height = len(mat)
        # mat, by itself, partially acts like the dp

        # compare top and left adjacent
        """
        CAN'T use ranges such range(1, height) or range(1, width). 
        Some values get excluded.
        For example, what if you go to the edges of "mat"
        """

        for row in range(height):
            for col in range(width):
                if mat[row][col] != 0:
                    top = mat[row-1][col] if row > 0 else float('inf');
                    left = mat[row][col-1] if col > 0 else float('inf');
                    # cannot compare mat[row][col] with itself in the 1st iteration
                    # this is because the value will remain as 1
                    mat[row][col] = min(top+1, left+1);

        # compare bottom and right adjacent
        # the iteration has to start at the bottom right
        for row in range(height-1, -1, -1):
            for col in range(width-1, -1, -1):
                if mat[row][col] != 0:
                    bottom = mat[row+1][col] if row < height-1 else float('inf');
                    right = mat[row][col+1] if col < width-1 else float('inf');
                    mat[row][col] = min(mat[row][col], bottom+1, right+1);

        """
        You learned about using if and else in initializing a variable
        """

        return mat

sol = Solution()
print(sol.updateMatrix([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]))