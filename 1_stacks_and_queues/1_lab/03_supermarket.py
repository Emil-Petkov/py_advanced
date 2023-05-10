from collections import deque

queue = deque()

while True:
    command = input()
    if command == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)
        if command == "End":
            print(f"{len(queue) - 1} people remaining.")
            break
