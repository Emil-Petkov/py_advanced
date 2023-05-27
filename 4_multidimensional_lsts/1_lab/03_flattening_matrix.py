data = [[int(numbers) for numbers in input().split(", ")] for _ in range(int(input()))]

print([num for row in data for num in row])
