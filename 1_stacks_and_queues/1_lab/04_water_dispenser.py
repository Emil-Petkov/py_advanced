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
