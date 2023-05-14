# [print([float(x.replace(",", ".")) for x in input().split("-")]) for _ in range(int(input()))]
# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,1
# [0.3, 1.2]
# [2.1, 3.5]
# [6.15, 3.1]

#################################################################################

longest_intersection = set()
first_set = set()
second_set = set()

for _ in range(int(input())):
    first_data, second_data = [x.split(",") for x in input().split("-")]

    first_range = set(range(int(first_data[0]), int(first_data[1]) + 1))
    second_range = set(range(int(second_data[0]), int(second_data[1]) + 1))

    intersection = first_range.intersection(second_range)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(map(str, longest_intersection))}] with length {len(longest_intersection)}")
