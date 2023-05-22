from collections import deque

queue = deque()

dispenser_quantity = int(input())

person_name = input()
while not person_name == "Start":
    queue.append(person_name)
    person_name = input()
while queue:
    command = input().split()

    if command[0] == "refill":
        dispenser_quantity += int(command[1])
    elif int(command[0]) <= dispenser_quantity:
        print(f"{queue.popleft()} got water")
        dispenser_quantity -= int(command[0])
    else:
        print(f"{queue.popleft()} must wait")

print(f"{dispenser_quantity} liters left")

#############################################################################

# from collections import deque

# quantity_water = int(input())

# queue = deque()

# command = input()

# while not command == "Start":
#     queue.append(command)

#     command = input()

# get_water = input().split()
# while not get_water[0] == "End":
#     if get_water[0] == "refill":
#         quantity_water += int(get_water[1])
#     else:

#         if quantity_water >= int(get_water[0]):
#             quantity_water -= int(get_water[0])
#             print(f"{queue.popleft()} got water")
#         else:
#             print(f"{queue.popleft()} must wait")

#     get_water = input().split()

# print(f"{quantity_water} liters left")
