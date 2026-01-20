class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        prevTriangle = self.generate(numRows-1);
        lastRow = prevTriangle[len(prevTriangle)-1];
        nextRow = [1];
        for index in range(len(lastRow)-1):
            nextRow.append(lastRow[index]+lastRow[index+1]);
        nextRow.append(1)
        prevTriangle.append(nextRow);
        return prevTriangle