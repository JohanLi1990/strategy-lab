matrix = [
    [1, 0, 0, 9, 8, 0, 4, 3, 0],
    [4, 9, 0, 2, 0, 0, 1, 6, 0],
    [0, 0, 3, 4, 0, 6, 7, 0, 9],
    [6, 0, 0, 1, 0, 0, 8, 9, 0],
    [9, 0, 0, 8, 2, 0, 6, 0, 3],
    [3, 2, 8, 0, 7, 9, 0, 4, 1],
    [7, 3, 0, 5, 0, 0, 2, 8, 6],
    [2, 0, 0, 7, 6, 0, 3, 0, 4],
    [0, 0, 6, 3, 0, 2, 9, 5, 0],
]
# Topological sort approach


# replace -1 with [1...9], such that 

def check_avail(i, j, matrix: list[list]):
    avail = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for k in range(9):
        if matrix[i][k] in avail:
            avail.remove(matrix[i][k])
        if matrix[k][j] in avail:
            avail.remove(matrix[k][j])
    # which box to check?
    box_i = (i // 3) * 3
    box_j = (j // 3) * 3
    for i in range(box_i, box_i + 3):
        for j in range(box_j, box_j + 3):
            if matrix[i][j] in avail:
                avail.remove(matrix[i][j])
    return avail

def sudoku_solver(matrix: list[list]):

    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                # check available options
                options = check_avail(i, j, matrix)
                if len(options) == 0:
                    return False
                for opt in options:
                    matrix[i][j] = opt
                    if sudoku_solver(matrix) == True:
                        return True
                    matrix[i][j] = 0
                return False
    return True


# print(check_avail(5, 1, matrix))
if sudoku_solver(matrix):
    for row in matrix:
        print(row)
