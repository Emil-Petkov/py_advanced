rows = int(input())

result = []

for _ in range(rows):
    matrix = [int(x) for x in input().split(", ")]
    result.append(
        [x for x in matrix if x % 2 == 0]
    )

print(result)

# rows = int(input())
#
# matrix = []
#
# for _ in range(rows):
#     list = []
#     elements = [int(x) for x in input().split(", ")]
#     for el in elements:
#         if el % 2 == 0:
#             list.append(el)
#
#     matrix.append(list)
#
# print(matrix)
