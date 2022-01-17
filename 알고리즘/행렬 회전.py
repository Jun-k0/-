# 행렬 회전하는 법을 자꾸 까먹어서,,,,, 기록기록 

def rotate_a_matrix_by_90_degree(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    result=[[0] * row for _ in range(column)]
    for i in range(row):
        for j in range(column):
            result[j][row - i - 1] = matrix[i][j]
    return result
