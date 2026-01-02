class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if target < matrix[0][0]:
            return False;
        elif target == matrix[0][0]:
            return True;
        elif target > matrix[len(matrix)-1][len(matrix[0])-1]:
            return False;
        elif target == matrix[len(matrix)-1][len(matrix[0])-1]:
            return True;
        halfLen = int((len(matrix)-1)/2);
        if len(matrix) == 1:
            return self.searchMatrix1d(matrix[0], target);
        elif (target > matrix[0][0] and target <= matrix[halfLen][len(matrix[0])-1]):
            return self.searchMatrix(matrix[:halfLen+1], target);
        else:
            return self.searchMatrix(matrix[halfLen+1:], target);

    def searchMatrix1d(self, row: list[int], target: int) -> bool:
        if target < row[0]:
            return False;
        elif target == row[0]:
            return True;
        elif target > row[len(row)-1]:
            return False;
        elif target == row[len(row)-1]:
            return True;
        halfLen = int((len(row)-1)/2);
        halfLenPlus = halfLen + 1;
        first = row[halfLen];
        second = row[halfLenPlus];
        if target == first:
            return True;
        elif target == second:
            return True;
        elif target > second:
            return self.searchMatrix1d(row[halfLenPlus+1:], target);
        elif target < first:
            return self.searchMatrix1d(row[:halfLen], target);
        else:
            return False;

sol = Solution();
print(sol.searchMatrix([[1],[3],[5]], 3));