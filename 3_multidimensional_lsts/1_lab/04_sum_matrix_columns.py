row, column = map(int, input().split(", "))

data = [list(map(int, input().split(" "))) for _ in range(row)]

column_sum = [sum(row[i] for row in data) for i in range(column)]

print(*column_sum, sep="\n")

