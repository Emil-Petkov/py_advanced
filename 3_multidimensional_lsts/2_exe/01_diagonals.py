matrix = [[int(el) for el in input().split(", ")] for _ in range(int(input()))]

primary_diagonal = []
secondary_diagonal = []

for row in range(len(matrix)):
    primary_diagonal.append(matrix[row][row])
for row in range(len(matrix)):
    secondary_diagonal.append(matrix[row][len(matrix) - row - 1])

print(f"Primary diagonal: {', '.join((str(el) for el in primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join((str(el) for el in secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")
