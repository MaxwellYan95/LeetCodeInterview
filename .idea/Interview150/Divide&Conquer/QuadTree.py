# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        if len(grid) == 0 or len(grid[0]) == 0:
            return None;
        elif len(grid) == 1 and len(grid[0]) == 1:
            return Node(grid[0][0], 1, None, None, None, None);
        else:
            num = self.allOneOrZero(grid);
            n = len(grid);
            halfN = int(n/2);
            if num == 0 or num == 1:
                return Node(num, 1, None, None, None, None);
            else:
                topLeft = self.construct([lst[0:halfN] for lst in grid[0:halfN]]);
                topRight = self.construct([lst[halfN: n] for lst in grid[0:halfN]]);
                bottomLeft = self.construct([lst[0:halfN] for lst in grid[halfN: n]]);
                bottomRight = self.construct([lst[halfN: n] for lst in grid[halfN: n]]);
                if topLeft.val == 1 or topRight.val == 1 or bottomLeft.val == 1 or bottomRight.val == 1:
                    return Node(1, 0, topLeft, topRight, bottomLeft, bottomRight);
                return Node(0, 0, topLeft, topRight, bottomLeft, bottomRight);


    def allOneOrZero(self, grid: List[List[int]]) -> 'Node':
        firstVal = grid[0][0];
        for outer in range(len(grid)):
            for inner in range(len(grid[0])):
                element = grid[outer][inner];
                if element != firstVal:
                    return -1;
        return firstVal;