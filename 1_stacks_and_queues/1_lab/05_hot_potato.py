from collections import deque

kids = deque(input().split())

n_turns = int(input())

counter = 0

while len(kids) > 1:
    counter += 1
    current_kid = kids.popleft()

    if counter == n_turns:
        print(f"Removed {current_kid}")
        counter = 0

    else:
        kids.append(current_kid)

print(f"Last is {kids[0]}")

############################################################################

# from collections import deque
#
# kids = deque(input().split())
#
# n_turns = int(input()) - 1
#
# while len(kids) > 1:
#     kids.rotate(-n_turns)
#     print(f"Removed {kids.popleft()}")
#
# print(f"Last is {kids[0]}")
