first_set = set()
second_set = set()

f_set, s_set = map(int, input().split())

[first_set.add(int(input())) for _ in range(f_set)]
[second_set.add(int(input())) for _ in range(s_set)]

print(*first_set.intersection(second_set), sep="\n")
