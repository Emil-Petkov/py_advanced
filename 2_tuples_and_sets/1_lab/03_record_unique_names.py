unique_names = set()

for _ in range(int(input())):
    current_name = input()
    unique_names.add(current_name)

print("\n".join(unique_names))
