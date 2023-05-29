first_sequence_of_numbers = [int(first_sequence) for first_sequence in input().split()]
second_sequence_of_numbers = [int(second_sequence) for second_sequence in input().split()]

n_lines = int(input())

first_set = set(first_sequence_of_numbers)
second_set = set(second_sequence_of_numbers)

for _ in range(n_lines):
    current_command = [command for command in input().split()]

    com = current_command[0]
    how_set = current_command[1]
    numbers = [int(el) for el in current_command if el.isdigit()]

    if current_command[0] == "Add":
        if current_command[1] == "First":
            first_set.update(num for num in numbers)

        elif current_command[1] == "Second":
            second_set.update(num for num in numbers)

    elif current_command[0] == "Remove":
        if current_command[1] == "First":
            for x in numbers:
                first_set.discard(x)

        elif current_command[1] == "Second":
            for x in numbers:
                second_set.discard(x)

    elif current_command[0] == "Check":
        if first_set.issubset(second_set):
            print(True)
        elif second_set.issubset(first_set):
            print(True)
        else:
            print(False)

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")

