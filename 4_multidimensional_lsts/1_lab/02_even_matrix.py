matrix = [[int(number) for number in input().split(", ")] for _ in range(int(input()))]
even_numbers = [[num for num in el if num % 2 == 0] for el in matrix]

print(even_numbers)

################################################################

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
