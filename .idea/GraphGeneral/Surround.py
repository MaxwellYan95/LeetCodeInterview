
def solve(board: list[list[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    visited = []
    newGrid = []
    for x in range(len(board)):
        visitRow = []
        newGridRow = []
        for y in range(len(board[0])):
            visitRow.append(False)
            newGridRow.append(board[x][y])
        visited.append(visitRow)
        newGrid.append(newGridRow)

    def identify(board: list[list[str]], x: int, y: int) -> bool:
        counter = False
        if ((x == 0 or x == len(board)-1 or y == 0 or y == len(board[0])-1) and board[x][y] == "O"):
            counter = True
        elif (board[x][y] == "X"):
            visited[x][y] = True
            return False
        elif (visited[x][y] == True):
            return False
        visited[x][y] = True
        edge = counter or identify(board, x+1, y) or identify(board, x-1, y) or identify(board, x, y+1) or identify(board, x, y-1)
        if (edge == False and board[x][y] == "O"):
            board[x][y] = "X"
        return edge

    for x in range(1, len(board)-1):
        for y in range(1, len(board[0])-1):
            if (visited[x][y] == False):
                identify(board, x, y)
            else:
                visited[x][y] = True

print(solve([["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]))