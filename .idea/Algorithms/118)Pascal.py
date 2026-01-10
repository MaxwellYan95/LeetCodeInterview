class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]];
        elif numRows == 2:
            return [[1], [1,1]]
        lst = [[1], [1,1]]
        for i in range(2, len(numRows)):
            n = i+1;
            inner = [1]
            for j in range(1, i):
                inner.append(lst[i-1][j-1] + lst[i-1][j])
            inner.append(1);
            lst.append(inner)
        return lst;