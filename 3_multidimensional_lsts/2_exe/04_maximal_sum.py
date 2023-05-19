n_rows, n_columns = map(int, input().split())

matrix = [[int(el) for el in input().split()] for _ in range(n_rows)]

max_sum = float("-inf")
current_numbers = []

for rows in range(len(matrix) - 2):
    for columns in range(len(matrix[0]) - 2):
        first_line = matrix[rows][columns], matrix[rows][columns + 1], matrix[rows][columns + 2]
        second_line = matrix[rows + 1][columns], matrix[rows + 1][columns + 1], matrix[rows + 1][columns + 2]
        third_line = matrix[rows + 2][columns], matrix[rows + 2][columns + 1], matrix[rows + 2][columns + 2]

        square_sum = sum(first_line) + sum(second_line) + sum(third_line)

        if square_sum > max_sum:
            current_numbers.append([first_line, second_line, third_line])
            max_sum = square_sum

print(f"Sum = {max_sum}")
[print(*el) for el in current_numbers[-1]]
