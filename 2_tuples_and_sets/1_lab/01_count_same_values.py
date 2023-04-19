numbers = list(map(float, input().split()))
checked_numbers = set()

for num in numbers:
    if num in checked_numbers:
        continue

    checked_numbers.add(num)

    print(f"{num} - {numbers.count(num)} times")
