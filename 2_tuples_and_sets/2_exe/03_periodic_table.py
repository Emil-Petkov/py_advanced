n = int(input())
unique_elements = set()

for i in range(n):
    compounds = input().split()
    for element in compounds:
        unique_elements.add(element)

for element in unique_elements:
    print(element)