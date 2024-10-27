def rotateMatrix(mat : List[List[int]]):
    size = len(mat)

    # transpose the matrix
    for i in range(size):
        for j in range(i, size):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # reverse the matrix
    for i in range(size):
        for j in range(size//2):
            mat[i][j], mat[i][size-1-j] = mat[i][size-1-j], mat[i][j]
