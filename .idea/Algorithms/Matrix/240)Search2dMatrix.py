class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        mHalf = m//2;
        nHalf = n//2
        midLeft = matrix[mHalf][0]
        middle = matrix[mHalf][nHalf]
        midRight = matrix[mHalf][n-1]
        downLeft = matrix[m-1][0]
        downMid = matrix[m-1][nHalf]
        downRight = matrix[m-1][n-1]
        if midLeft < target < middle:
            return self.searchMatrix(matrix[:])

