class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False;
        n = len(matrix[0])
        if m == 0 or n == 0:
            return False;
        if len(matrix) == 1:
            return self.binarySearch(matrix[0], target);
        elif len(matrix[0]) == 1:
            return self.binarySearch([matrix[n][0] for n in range(len(matrix))], target);
        topLeft = matrix[0][0];
        topRight = matrix[0][n-1];
        bottomLeft = matrix[m-1][0];
        bottomRight = matrix[m-1][n-1];
        if topLeft == target or topRight == target or bottomLeft == target or bottomRight == target:
            return TypeError
        rowBound = [0, m]
        colBound = [0, n]
        if topLeft < target and topRight < target:
            rowBound[0] += 1;
        if topLeft < target and bottomLeft < target:
            colBound[0] += 1;
        if bottomLeft > target and bottomRight > target:
            rowBound[1] -= 1;
        if bottomRight > target and topRight > target:
            colBound[1] -= 1;
        subMatrix = [row[colBound[0]:colBound[1]] for row in matrix[rowBound[0]:rowBound[1]]]
        return self.searchMatrix(subMatrix, target)

    def binarySearch(self, row: list[int], target: int):
        if row[0] == target or row[len(row)-1] == target:
            return True
        middleInd = len(row) // 2;
        if row[middleInd] == target:
            return True;
        if row[0] < target and target < row[middleInd]:
            return self.binarySearch(row[:middleInd], target);
        if row[middleInd] < target and target < row[len(row)-1]:
            return self.binarySearch(row[middleInd:], target);
        return False;

sol = Solution()
print(sol.searchMatrix([[5,6,9],[9,10,11],[11,14,18]], 9))
