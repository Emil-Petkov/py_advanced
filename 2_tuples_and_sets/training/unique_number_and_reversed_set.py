# numbers = [int(n) for n in input("Enter sequence of number separated by comma and space:\n").split(", ")]

# unique_numbers = {num for num in numbers}

numbers = {int(n) for n in input("Enter sequence of numbers separated by comma and space:\n").split(", ")}

print("\nUnique numbers in set")
print(unique_numbers)

print("_____________________________________________")

print("Reversed numbers in set")
reverse_set = list(unique_numbers)[::-1]
print(reverse_set)
