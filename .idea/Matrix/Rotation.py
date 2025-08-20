def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    tempMatrix = [[matrix[(len(matrix)-1)-col][row] for col in range(len(matrix))]for row in range(len(matrix))]
    matrix.replace(tempMatrix)
    print(matrix)

m = [[1,2,3],[4,5,6],[7,8,9]]
rotate(m)
print(m)
