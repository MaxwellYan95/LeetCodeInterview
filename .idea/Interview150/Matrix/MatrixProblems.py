def isValidSudoku(board: list[list[str]]) -> bool:
    for row in board:
        num = []
        for element in row:
            if (element != "."):
                num.append(element)
        numSet = set(num)
        if (len(num) != len(numSet)):
            return False
    for firstIndex in range(9):
        num = []
        for index in range(9):
            element = board[index][firstIndex]
            if (element != "."):
                num.append(element)
        numSet = set(num)
        if (len(num) != len(numSet)):
            return False
    cubes = [[(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)],
             [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)],
             [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)],
             [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)],
             [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)],
             [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)],
             [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)],
             [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)],
             [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)],]
    for c in cubes:
        num = []
        for row, col in c:
            element = board[row][col]
            if (element != "."):
                num.append(board[row][col])
        numSet = set(num)
        if (len(num) != len(numSet)):
            return False
    return True

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    nums = []
    lowerCol = 0
    higherCol = len(matrix[0])-1
    lowerRow = 0
    higherRow = len(matrix)-1
    while True:
        for col in range(lowerCol, higherCol+1):
            nums.append(matrix[lowerRow][col])
        for row in range(lowerRow+1, higherRow+1):
            nums.append(matrix[row][higherCol])
        for col in range(higherCol-1, lowerCol-1, -1):
            nums.append(matrix[higherRow][col])
        for row in range(higherRow-1, lowerRow, -1):
            nums.append(matrix[row][lowerCol])
        lowerCol = lowerCol + 1
        higherCol = higherCol - 1
        lowerRow = lowerRow + 1
        higherRow = higherRow - 1
        while len(nums) > len(matrix)*len(matrix[0]):
            nums.pop()
        if (lowerRow > higherRow):
            break
        if (lowerCol > higherCol):
            break
    return nums

def rotate(matrix: list[list[int]]) -> None:
    tempMatrix = []
    for row in range(len(matrix)):
        tempMatrix.append([])
        for col in range(len(matrix[0])):
            tempMatrix[row].append(matrix[row][col])
    for row in range(len(tempMatrix)):
        for col in range(len(tempMatrix[0])):
            matrix[row][col] = tempMatrix[(len(tempMatrix)-1)-col][row]

def setZeroes(matrix: list[list[int]]) -> None:
    coord = []
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if (matrix[x][y] == 0):
                coord.append((x, y))
    for x, y in coord:
        for row in range(len(matrix)):
            matrix[row][y] = 0
        for col in range(len(matrix[0])):
            matrix[x][col] = 0

def gameOfLife(board: list[list[int]]) -> None:
    cond = []
    for row in range(len(board)):
        cond.append([])
    for row in range(len(board)):
        for col in range(len(board[0])):
            adj = [(row-1, col-1), (row-1, col), (row-1, col+1),
                   (row, col-1), (row, col+1),
                   (row+1, col-1), (row+1, col), (row+1, col+1)]
            alive = 0
            for x, y in adj:
                inBounds = (x >= 0) and (y >= 0) and (x < len(board)) and (y < len(board[0]))
                if inBounds:
                    if board[x][y] == 1:
                        alive = alive + 1
            if (alive < 2 and board[row][col] == 1):
                cond[row].append(False)
            elif ((alive == 2 or alive == 3) and board[row][col] == 1):
                cond[row].append(True)
            elif (alive > 2 and board[row][col] == 1):
                cond[row].append(False)
            elif (alive == 3 and board[row][col] == 0):
                cond[row].append(True)
            else:
                cond[row].append(False)
    for row in range(len(cond)):
        for col in range(len(cond[0])):
            if cond[row][col] == False:
                board[row][col] = 0
            else:
                board[row][col] = 1

board1 = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board1))
board2 = [[".",".",".",".","5",".",".","1","."],
          [".","4",".","3",".",".",".",".","."],
          [".",".",".",".",".","3",".",".","1"],
          ["8",".",".",".",".",".",".","2","."],
          [".",".","2",".","7",".",".",".","."],
          [".","1","5",".",".",".",".",".","."],
          [".",".",".",".",".","2",".",".","."],
          [".","2",".","9",".",".",".",".","."],
          [".",".","4",".",".",".",".",".","."]]
print(isValidSudoku(board2))

matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix1))
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix2))

board3 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(gameOfLife(board3))

matrix3 = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate(matrix3))
