rows = int(input())

matrix = [list(map(int, input().split(", "))) for _ in range(rows)]

result = [el for row in matrix for el in row]

print(matrix)
