def is_rectangle(matrix):
    ln_str = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != ln_str:
            return False
    return True

def transpose(mat: list[list[float | int]]) -> list[list]:
    if not is_rectangle(mat):
        raise ValueError("Рваная матрица")
    new_mat = [[0 for i in range(len(mat))] for y in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            new_mat[j][i] = mat[i][j]
    return new_mat

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not is_rectangle(mat):
            raise ValueError("Рваная матрица")
    sums = []
    for i in mat:
        sums.append(sum(i))
    return sums

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not is_rectangle(mat):
                raise ValueError("Рваная матрица")
    sums = [0 for i in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
             sums[j] += mat[i][j]
    return sums
