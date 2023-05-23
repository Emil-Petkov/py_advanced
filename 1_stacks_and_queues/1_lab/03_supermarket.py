from collections import deque

people = deque()

while True:
    command = input()

    if command == "Paid":
        while people:
            print(f"{people.popleft()}")

    else:

        if command == "End":
            print(f"{len(people)} people remaining.")
            break
        else:
            people.append(command)
