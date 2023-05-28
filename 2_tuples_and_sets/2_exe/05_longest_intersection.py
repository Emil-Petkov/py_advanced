# [print([float(x.replace(",", ".")) for x in input().split("-")]) for _ in range(int(input()))]
# 3
# 0,3-1,2
# 2,10-3,5
# 6,15-3,1
# [0.3, 1.2]
# [2.1, 3.5]
# [6.15, 3.1]

#################################################################################

n_lines = int(input())

longest_intersection = []

for _ in range(n_lines):
    current_range = input().split("-")

    first_set = set()
    second_set = set()

    first_start, first_end = [int(x) for x in current_range[0].split(",")]
    second_start, second_end = [int(x) for x in current_range[1].split(",")]

    for x in range(first_start, first_end + 1):
        first_set.add(x)

    for y in range(second_start, second_end + 1):
        second_set.add(y)

    intersection = first_set.intersection(second_set)

    if len(longest_intersection) < len(intersection):
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")

