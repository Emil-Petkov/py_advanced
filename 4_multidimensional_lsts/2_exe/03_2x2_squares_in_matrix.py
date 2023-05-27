n_rows, n_columns = map(int, input().split())

matrix = [[el for el in input().split()] for _ in range(n_rows)]

counter = 0

for row in range(len(matrix) - 1):
    for column in range(len(matrix[0]) - 1):
        el = matrix[row][column]
        next_el = matrix[row][column + 1]
        down_el = matrix[row + 1][column]
        diagonal_el = matrix[row + 1][column + 1]

        if el == next_el == down_el == diagonal_el:
            counter += 1

print(counter)
