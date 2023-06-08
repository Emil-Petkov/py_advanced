rows, columns = [int(x) for x in input().split(", ")]

matrix = [[int(c) for c in input().split(", ")] for r in range(rows)]

max_sum = 0
sum_of_max_digits = []

for row in range(rows - 1):
    for col in range(columns - 1):

        current_num = matrix[row][col]
        right_num = matrix[row][col + 1]
        down_num = matrix[row + 1][col]
        diagonal_num = matrix[row + 1][col + 1]

        current_sum = current_num + right_num + down_num + diagonal_num

        if current_sum > max_sum:
            digits = current_num, right_num, down_num, diagonal_num
            sum_of_max_digits.append(digits)
            max_sum = current_sum

dig = sum_of_max_digits[-1]
print(dig[0], dig[1])
print(dig[2], dig[3])
print(max_sum)

