n_rows = input().split(", ")

collect_data = []

for _ in range(int(n_rows[0])):
    numbers = [int(x) for x in input().split()]
    collect_data.append(numbers)

    unpack_data = zip(*collect_data)

    sum_of_matrix = [sum(unpack_data) for unpack_data in unpack_data]

for el in sum_of_matrix:
    print(el)


