rows = int(input())

matrix = []

for _ in range(rows):
    list = []
    elements = [int(x) for x in input().split(", ")]
    for el in elements:
        if el % 2 == 0:
            list.append(el)

    matrix.append(list)

print(matrix)
