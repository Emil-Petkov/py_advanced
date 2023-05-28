n_lines = int(input())

even_set = set()
odd_set = set()

for row in range(1, n_lines + 1):
    current_name = input()

    ascii_sum_of_name = sum([ord(el) for el in current_name]) // row

    if ascii_sum_of_name % 2 == 0:
        even_set.add(ascii_sum_of_name)
    else:
        odd_set.add(ascii_sum_of_name)

if sum(even_set) == sum(odd_set):
    print(*even_set.union(odd_set), sep=", ")

elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")

elif sum(even_set) > sum(odd_set):
    print(*odd_set.symmetric_difference(even_set), sep=", ")
