def read_matrix():
    row_columns = list(map(int, input().split(", ")))

    total_sum = 0
    matrix = []

    for _ in range(row_columns[0]):
        element = []

        for i in range(row_columns[1]):
            numbers = list(map(int, input().split(", ")))
            for num in numbers:
                element.append(num)
            matrix.append(element)
            break

    for el in matrix:
        total_sum += sum(el)

    print(total_sum)
    print(matrix)


read_matrix()
