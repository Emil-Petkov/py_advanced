n_names = int(input())

even_numbers = set()
odd_numbers = set()

for i in range(1, n_names + 1):
    current_name = input()

    convert_el_in_ord = [ord(el) for el in current_name]

    sum_of_characters = sum(convert_el_in_ord) // i
    if sum_of_characters % 2 == 0:
        even_numbers.add(sum_of_characters)
    else:
        odd_numbers.add(sum_of_characters)

if sum(even_numbers) > sum(odd_numbers):
    print(*even_numbers.symmetric_difference(odd_numbers), sep=", ")
else:
    print(*odd_numbers.difference(even_numbers), sep=", ")

