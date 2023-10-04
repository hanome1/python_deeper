"""Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]"""


def transpon(matrix: list[list[int]]) -> list[list[int]]:
    new_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        new_matrix.append(new_row)
    return new_matrix
print(transpon([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))