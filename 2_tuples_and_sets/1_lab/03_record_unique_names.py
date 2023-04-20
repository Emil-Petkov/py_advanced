n_iteration = int(input())

unique_name = set()

for _ in range(n_iteration):
    current_name = input()
    if current_name not in unique_name:
        unique_name.add(current_name)

for name in unique_name:
    print(name)
