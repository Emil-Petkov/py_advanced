row, column = map(int, input().split(", "))

matrix = [[int(c) for c in input().split(", ")] for r in range(row)]

print(sum(sum(r) for r in matrix))
print(matrix)

################################################################

# row, column = [int(x) for x in input().split(", ")]

# sum_of_matrix = 0
# matrix = []

# for _ in range(row):
#     aaa = matrix.append([int(num) for num in input().split(", ")])

# for el in matrix:
#     sum_of_matrix += sum(el)

# print(sum_of_matrix)
# print(matrix)
