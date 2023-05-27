def count_same_values(numbers):
    dict = {}

    for num in numbers:
        if num not in dict:
            dict[num] = 0
        dict[num] += 1

    for k, v in dict.items():
        print(f"{k} - {v} times")


count_same_values(map(float, input().split()))

