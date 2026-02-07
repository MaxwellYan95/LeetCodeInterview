def rotate(matrix: list[list[int]]) -> None:
    tempMatrix = [[matrix[row][col] for col in range(len(matrix[0]))] for row in range(len(matrix))];
    reverseMatrix = [row for row in tempMatrix[::-1]];
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            matrix[col][row] = reverseMatrix[row][col]

m = [[1,2,3],[4,5,6],[7,8,9]]
rotate(m)
print()