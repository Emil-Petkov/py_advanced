matrix = [[int(el) for el in input().split()] for rows in range(int(input()))]

# diagonal_sum = 0
#
# for r in range(len(matrix)):
#     diagonal_sum += matrix[r][r]
#
# print(diagonal_sum)

print(*[sum(matrix[row][row] for row in range(len(matrix)))])
