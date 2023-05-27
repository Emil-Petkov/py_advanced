n_rows, n_columns = map(int, input().split(", "))

matrix = [[int(el) for el in input().split(", ")] for _ in range(n_rows)]

max_sum = 0
current_indexes = []

for rows in range(n_rows - 1):
    for column in range(n_columns - 1):
        el = matrix[rows][column]
        next_el = matrix[rows][column + 1]
        down_el = matrix[rows + 1][column]
        diagonal_el = matrix[rows + 1][column + 1]

        square_sum = el + next_el + down_el + diagonal_el

        if square_sum > max_sum:
            current_indexes.append([el, next_el, down_el, diagonal_el])
            max_sum = square_sum

max_indexes = current_indexes[-1]

print(max_indexes[0], max_indexes[1])
print(max_indexes[2], max_indexes[3])
print(max_sum)
