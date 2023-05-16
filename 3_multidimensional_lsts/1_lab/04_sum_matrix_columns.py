<<<<<<< HEAD
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

=======
row, column = map(int, input().split(", "))

data = [list(map(int, input().split(" "))) for _ in range(row)]

column_sum = [sum(row[i] for row in data) for i in range(column)]

print(*column_sum, sep="\n")
>>>>>>> c7f36aa9b915e2a861f6166038e8da5cbe2f90bf

