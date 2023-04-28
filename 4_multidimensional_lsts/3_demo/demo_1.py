n_lists = int(input("n_lists: "))
n_elements = int(input("n_elements: "))

matrix = []

for i in range(n_lists):
    list = []

    for j in range(1, n_elements + 1):
        list.append(j)

    matrix.append(list)

print(matrix)
