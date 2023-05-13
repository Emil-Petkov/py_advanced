from collections import deque

clothes_in_the_box = deque([int(x) for x in input().split()])
capacity_of_the_rack = int(input())

total_capacity = capacity_of_the_rack
rack_counter = 1

while clothes_in_the_box:
    last_element = clothes_in_the_box.pop()

    if total_capacity >= last_element:
        total_capacity -= last_element

    else:
        total_capacity = capacity_of_the_rack
        rack_counter += 1
        total_capacity -= last_element

print(rack_counter)

