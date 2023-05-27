n_rows, n_columns = [int(n) for n in input().split(", ")]
matrix = [[int(data) for data in input().split()] for _ in range(n_rows)]

# for col in range(n_columns):
#     columns_sum = 0
#
#     for row in range(n_rows):
#         columns_sum += matrix[row][col]
#
#     print(columns_sum)

print(*[sum(matrix[row][col] for row in range(n_rows)) for col in range(n_columns)], sep="\n")
