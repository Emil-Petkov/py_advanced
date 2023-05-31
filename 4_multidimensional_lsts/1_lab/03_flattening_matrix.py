data = [[int(numbers) for numbers in input().split(", ")] for _ in range(int(input()))]

print([num for row in data for num in row])

#############################################################

# row =  int(input())

# result = []

# for _ in range(row):
#     current_row = input().split(", ")
#     for el in current_row:
#         result.append(int(el))

# print(result)
