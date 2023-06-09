matrix = [[int(x) for x in input().split(", ")] for _ in range(int(input()))]

primary_diagonal = []
secondary_diagonal = []

for row in range(len(matrix)):
    primary_diagonal.append(matrix[row][row])

for row in range(len(matrix)):
    secondary_diagonal.append(matrix[row][len(matrix) - row - 1])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
