unique_names = set()

for _ in range(int(input())):
    current_name = input()
    unique_names.add(current_name)

print("\n".join(unique_names))


######################################################

# def unique_names(n):
#     collection_unique_names = set()

#     for _ in range(n):
#         current_name = input()
#         if current_name not in collection_unique_names:
#             collection_unique_names.add(current_name)

#     for name in collection_unique_names:
#         print(name)


# unique_names(int(input()))
