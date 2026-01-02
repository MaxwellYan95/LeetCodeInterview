from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        horizon = self.horizontal(board);
        vert = self.vertical(board);
        return horizon and vert \
               and self.cube(board, [0, 3], [0, 3]) \
               and self.cube(board, [0, 3], [3, 6]) \
               and self.cube(board, [0, 3], [6, 9]) \
               and self.cube(board, [3, 6], [0, 3]) \
               and self.cube(board, [3, 6], [3, 6]) \
               and self.cube(board, [3, 6], [6, 9]) \
               and self.cube(board, [6, 9], [0, 3]) \
               and self.cube(board, [6, 9], [3, 6]) \
               and self.cube(board, [6, 9], [6, 9]);

    def horizontal(self, board: list[list[str]]) -> bool:
        for col in range(len(board)):
            row = board[col]
            if self.hasDuplicate(row) == False:
                return False;
        return True;

    def vertical(self, board: list[list[str]]) -> bool:
        for row in range(len(board[0])):
            results = []
            for col in range(len(board)):
                results.append(board[col][row]);
            if self.hasDuplicate(results) == False:
                return False;
        return True;

    def cube(self, board: list[list[str]], rowBounds: list[int], colBounds: list[int]):
        cubeLst = [];
        for r in range(rowBounds[0], rowBounds[1]):
            cubeLst.extend(board[r][colBounds[0]:colBounds[1]]);
        return self.hasDuplicate(cubeLst);

    def hasDuplicate(self, lst: list[str]):
        dict = defaultdict(int)
        for r in set(lst):
            dict[r] = lst.count(r);
        for num in "123456789":
            if dict[num] > 1:
                return False;
        return True;