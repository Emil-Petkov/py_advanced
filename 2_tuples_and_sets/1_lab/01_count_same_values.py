numbers = [float(x) for x in input().split()]

dict = {}

for num in numbers:
    if num not in dict:
        dict[num] = 0
    dict[num] += 1

for key, value in dict.items():
    print(f"{key} - {value} times")
