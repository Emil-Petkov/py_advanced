def matrix_traversal(matrix, searched_symbol):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == searched_symbol:
                return f"({row}, {col})"

    return f"{searched_symbol} does not occur in the matrix"


matrix = [[el for el in input()] for _ in range(int(input()))]

print(matrix_traversal(matrix, searched_symbol=input()))
