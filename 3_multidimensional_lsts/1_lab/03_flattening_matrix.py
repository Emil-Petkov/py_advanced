data = [[int(num) for num in input().split(", ")] for _ in range(int(input()))]

print([el for row in data for el in row])
