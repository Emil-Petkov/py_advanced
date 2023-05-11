# numbers = input().split()
#
# numbers.reverse()
#
# print(" ".join(numbers))

######################################################

# print(" ".join(input().split()[::-1]))

######################################################

from collections import deque

numbers = deque(input().split())

while numbers:
    print(numbers.pop(), end=" ")

    
