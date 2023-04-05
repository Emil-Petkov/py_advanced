from collections import deque


def add_persons_in_queue():
    peoples_data = deque()
    while True:
        name = input()

        if name == "Start":
            break
        peoples_data.append(name)

    return peoples_data


water_amount = int(input())

people_deque = add_persons_in_queue()

while True:
    command = input()

    if command == "End":
        print(f"{water_amount} liters left")
        break

    elif command.startswith("refill"):
        refill_liters = command.split()
        add_liters = refill_liters[1]
        water_amount += int(add_liters)

    else:
        person = people_deque.popleft()
        current_liters_left = int(command)

        if current_liters_left <= water_amount:
            print(f"{person} got water")
            water_amount -= current_liters_left
        else:
            print(f"{person} must wait")
