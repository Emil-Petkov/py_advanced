from collections import deque

quantity_food = int(input())

queue = deque()

orders = input().split()

for el in orders:
    queue.append(int(el))

print(max(queue))

while queue:
    if quantity_food >= queue[0]:
        quantity_food -= queue.popleft()
    else:
        print(f"Orders left: {' '.join(map(str, queue))}")
        exit()

print("Orders complete")
