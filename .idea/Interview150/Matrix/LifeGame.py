class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        newBoard = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]
        def modify(row: int, col: int):
            adjList = [(0, 1), (0,-1),
                   (1, 0), (-1, 0),
                   (1, 1), (1, -1),
                   (-1, 1), (-1, -1)]
            neigh = 0;
            for dRow, dCol in adjList:
                r = row + dRow;
                c = col + dCol;
                notBound = r < 0 \
                           or r > len(board)-1 \
                           or c < 0 \
                           or c > len(board[0])-1
                if notBound:
                    continue
                if newBoard[r][c] == 1:
                    neigh += 1;
            if neigh < 2 or neigh > 3:
                board[row][col] = 0;
            if neigh == 3:
                board[row][col] = 1;
        for x in range(len(board)):
            for y in range(len(board[0])):
                modify(x, y)


sol = Solution()
b = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(sol.gameOfLife(b))

