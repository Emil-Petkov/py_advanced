from collections import deque

biggest_order = 0

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():

    if food_quantity >= order:
        orders.popleft()
        food_quantity -= order

    else:
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        break

else:
    print("Orders complete")

    
