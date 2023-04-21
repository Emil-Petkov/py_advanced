from collections import deque

kids = input().split()
n_toss = int(input())

queue = deque(kids)

counter = 0

while len(queue) > 1:
    counter += 1
    current_kid = queue.popleft()

    if counter == n_toss:
        print(f"Removed {current_kid}")
        counter = 0
    else:
        queue.append(current_kid)

print(f"Last is {queue[0]}")

