from collections import deque

data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

data_copy = data.copy()

current_gas = 0
index_start_station = 0

while data_copy:
    petrol, distance = data_copy.popleft()

    current_gas += petrol

    if current_gas >= distance:
        current_gas -= distance
    else:
        data.rotate(-1)
        data_copy = data.copy()
        index_start_station += 1
        current_gas = 0

print(index_start_station)
