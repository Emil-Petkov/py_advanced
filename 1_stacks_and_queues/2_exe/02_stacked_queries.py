from collections import deque

deque = deque()

n_iteration = int(input())

for i in range(n_iteration):
    data = input().split()
    if int(data[0]) == 1:
        deque.append(int(data[1]))

    elif int(data[0]) == 2:
        if deque:
            deque.pop()

    elif int(data[0]) == 3:
        if deque:
            print(max(deque))

    elif int(data[0]) == 4:
        if deque:
            print(min(deque))

deque.reverse()

print(*deque, sep=", ")
